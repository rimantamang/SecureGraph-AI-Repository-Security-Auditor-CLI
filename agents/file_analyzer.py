import os
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from prompts.classifier_prompt import CLASSIFIER_PROMPT

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def classify_file(file: dict) -> dict:
    filename = file["filename"]
    extension = file["extension"]
    path = file["path"]

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read(2000)
    except Exception:
        content = ""

    prompt = CLASSIFIER_PROMPT.format(
        filename=filename,
        extension=extension,
        content=content
    )

    response = llm.invoke(prompt)
    time.sleep(3)
    category = response.content.strip().lower()

    if category not in ["route", "auth", "db", "config", "other"]:
        category = "other"

    return {
        **file,
        "category": category
    }


def run_file_analyzer(files: list[dict]) -> list[dict]:
    classified = []
    for file in files:
        result = classify_file(file)
        print(f"  [{result['category'].upper()}] {result['filename']}")
        classified.append(result)
    return classified