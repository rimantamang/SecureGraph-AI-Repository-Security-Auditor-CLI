import json
import os
from datetime import datetime


def generate_reports(findings: list[dict], output_dir: str = "reports"):
    """
    Generates report.json and report.md from findings.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    generate_json_report(findings, output_dir, timestamp)
    generate_md_report(findings, output_dir, timestamp)

    print(f"\nReports saved to {output_dir}/report.json and {output_dir}/report.md")


def generate_json_report(findings: list[dict], output_dir: str, timestamp: str):
    report = {
        "tool": "SecureGraph AI",
        "timestamp": timestamp,
        "total_findings": len(findings),
        "findings": findings
    }

    path = os.path.join(output_dir, "report.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)


def generate_md_report(findings: list[dict], output_dir: str, timestamp: str):
    lines = []
    lines.append("# SecureGraph AI - Security Report\n")
    lines.append(f"**Generated:** {timestamp}\n")
    lines.append(f"**Total Findings:** {len(findings)}\n")
    lines.append("---\n")

    if not findings:
        lines.append("No vulnerabilities found.\n")
    else:
        for i, f in enumerate(findings, 1):
            lines.append(f"## [{f.get('severity', 'UNKNOWN')}] {f.get('issue', 'Unknown Issue')}\n")
            lines.append(f"- **File:** {f.get('filename', 'N/A')}")
            lines.append(f"- **Line:** {f.get('line', 'N/A')}")
            lines.append(f"- **Reason:** {f.get('reason', 'N/A')}")
            lines.append(f"- **Fix:** {f.get('fix', 'N/A')}")
            lines.append("")

    path = os.path.join(output_dir, "report.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))