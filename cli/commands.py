import typer
from graph.workflow import run_scan
from reports.report_generator import generate_reports

app = typer.Typer()

@app.command()
def scan(path: str = typer.Argument(".", help="Path to the repository to scan")):
    """
    Scan a local repository for security vulnerabilities.
    """
    typer.echo(f"\nSecureGraph AI - Repository Security Auditor")
    typer.echo(f"Scanning: {path}\n")

    result = run_scan(path)
    findings = result["all_findings"]

    if not findings:
        typer.echo("\nNo vulnerabilities found.")
        raise typer.Exit()

    typer.echo(f"\n--- FINDINGS ---\n")
    for f in findings:
        typer.echo(f"[{f.get('severity', 'UNKNOWN')}] {f.get('issue')}")
        typer.echo(f"File: {f.get('filename')}")
        typer.echo(f"Line: {f.get('line', 'N/A')}")
        typer.echo(f"Reason: {f.get('reason')}")
        typer.echo(f"Fix: {f.get('fix')}")
        typer.echo("")

    generate_reports(findings)