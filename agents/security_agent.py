import os
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from prompts.security_prompt import SECURITY_PROMPT

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_security(file: dict) -> list[dict]:
    path = file["path"]
    filename = file["filename"]

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read(3000)
    except Exception:
        return []

    prompt = SECURITY_PROMPT.format(
        filename=filename,
        content=content
    )

    response = llm.invoke(prompt)
    time.sleep(3)
    output = response.content.strip()

    if output == "NONE" or "NONE" in output:
        return []

    findings = []
    blocks = output.split("---")

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        finding = {"file": path, "filename": filename}
        for line in block.splitlines():
            if line.startswith("SEVERITY:"):
                finding["severity"] = line.replace("SEVERITY:", "").strip()
            elif line.startswith("ISSUE:"):
                finding["issue"] = line.replace("ISSUE:", "").strip()
            elif line.startswith("LINE:"):
                finding["line"] = line.replace("LINE:", "").strip()
            elif line.startswith("REASON:"):
                finding["reason"] = line.replace("REASON:", "").strip()
            elif line.startswith("FIX:"):
                finding["fix"] = line.replace("FIX:", "").strip()

        if "issue" in finding:
            findings.append(finding)

    return findings


def run_security_agent(files: list[dict]) -> list[dict]:
    all_findings = []
    for file in files:
        findings = analyze_security(file)
        if findings:
            for f in findings:
                print(f"  [{f.get('severity', 'UNKNOWN')}] {f.get('issue')} in {f.get('filename')}")
        all_findings.extend(findings)
    return all_findings