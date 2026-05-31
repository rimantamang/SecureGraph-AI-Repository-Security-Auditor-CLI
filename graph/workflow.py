from typing import TypedDict
from langgraph.graph import StateGraph, END
from scanner.file_scanner import scan_repository
from agents.file_analyzer import run_file_analyzer
from agents.security_agent import run_security_agent
from agents.secrets_agent import run_secrets_agent
from agents.auth_agent import run_auth_agent


# Define the state that flows through the graph
class ScanState(TypedDict):
    path: str
    files: list
    classified_files: list
    security_findings: list
    secrets_findings: list
    auth_findings: list
    all_findings: list


# Node functions
def scan_node(state: ScanState) -> ScanState:
    print("\n[1/5] Scanning repository...")
    files = scan_repository(state["path"])
    print(f"  Found {len(files)} files.")
    return {**state, "files": files}


def classify_node(state: ScanState) -> ScanState:
    print("\n[2/5] Classifying files...")
    classified = run_file_analyzer(state["files"])
    return {**state, "classified_files": classified}


def security_node(state: ScanState) -> ScanState:
    print("\n[3/5] Running security analysis...")
    findings = run_security_agent(state["classified_files"])
    return {**state, "security_findings": findings}


def secrets_node(state: ScanState) -> ScanState:
    print("\n[4/5] Running secrets detection...")
    findings = run_secrets_agent(state["classified_files"])
    return {**state, "secrets_findings": findings}


def auth_node(state: ScanState) -> ScanState:
    print("\n[5/5] Running auth analysis...")
    findings = run_auth_agent(state["classified_files"])
    return {**state, "auth_findings": findings}


def aggregate_node(state: ScanState) -> ScanState:
    all_findings = (
        state["security_findings"] +
        state["secrets_findings"] +
        state["auth_findings"]
    )
    return {**state, "all_findings": all_findings}


# Build the graph
def build_graph():
    graph = StateGraph(ScanState)

    graph.add_node("scan", scan_node)
    graph.add_node("classify", classify_node)
    graph.add_node("security", security_node)
    graph.add_node("secrets", secrets_node)
    graph.add_node("auth", auth_node)
    graph.add_node("aggregate", aggregate_node)

    graph.set_entry_point("scan")
    graph.add_edge("scan", "classify")
    graph.add_edge("classify", "security")
    graph.add_edge("security", "secrets")
    graph.add_edge("secrets", "auth")
    graph.add_edge("auth", "aggregate")
    graph.add_edge("aggregate", END)

    return graph.compile()


def run_scan(path: str) -> dict:
    """
    Entry point to run the full scan workflow.
    """
    graph = build_graph()

    initial_state = {
        "path": path,
        "files": [],
        "classified_files": [],
        "security_findings": [],
        "secrets_findings": [],
        "auth_findings": [],
        "all_findings": [],
    }

    result = graph.invoke(initial_state)
    return result