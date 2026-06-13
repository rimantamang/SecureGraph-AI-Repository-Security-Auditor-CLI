SecureGraph AI — Repository Security Auditor CLI

An AI-powered CLI tool that scans your code repositories for security vulnerabilities, exposed secrets, and authentication issues. Built with LangGraph multi-agent architecture and powered by Groq's LLM API.


Features


Multi-agent security analysis using LangGraph workflow
File scanning — detects sensitive files and risky patterns
Secret detection — finds exposed API keys, tokens, and credentials
Auth review — analyzes authentication and authorization logic
Automated reports — outputs results in both report.json and report.md
Fast inference via Groq API (llama-3.1-8b-instant)



Tech Stack

ToolPurposePython 3.12Core languageLangGraphMulti-agent workflow orchestrationLangChainLLM integration layerGroq APILLM backend (llama-3.1-8b-instant)TyperCLI interfacepython-dotenvEnvironment variable management


Project Structure

SecureGraph-AI/
├── scanner/
│   └── file_scanner.py        # Scans repo files
├── agents/
│   ├── file_analyzer.py       # Analyzes file contents
│   ├── security_agent.py      # Detects general vulnerabilities
│   ├── secrets_agent.py       # Detects exposed secrets/keys
│   └── auth_agent.py          # Reviews authentication logic
├── graph/
│   └── workflow.py            # LangGraph agent workflow
├── prompts/                   # LLM prompt templates (4 files)
├── reports/
│   └── report_generator.py    # Generates report.json and report.md
├── cli/
│   └── commands.py            # CLI command definitions
├── main.py                    # Entry point
├── pyproject.toml             # Package configuration
└── .env                       # API keys (not committed)


Installation

1. Clone the repository

bashgit clone https://github.com/rimantamang/SecureGraph-AI-Repository-Security-Auditor-CLI.git
cd SecureGraph-AI-Repository-Security-Auditor-CLI

2. Create and activate a conda environment

bashconda create -n securegraph python=3.12
conda activate securegraph

3. Install the package

bashpip install -e .

4. Set up your API key

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

You can get a free Groq API key at console.groq.com.


Usage

Run the tool from the project root, pointing it at any directory:

bash# Scan the current directory
securegraph .

# Or using Python directly
python main.py .

# Scan a specific path
securegraph /path/to/your/repo

After the scan completes, reports are saved as:


report.md — human-readable Markdown report
report.json — structured JSON for programmatic use



Example Output

🔍 Scanning repository...
✅ File scan complete — 24 files found
🤖 Running security agents...
⚠️  Potential exposed secret detected in config.py
⚠️  Weak authentication pattern found in auth.py
📄 Report saved to report.md and report.json


Agents Overview

AgentWhat it doesfile_analyzerReads and categorizes files in the reposecurity_agentChecks for general security vulnerabilitiessecrets_agentDetects hardcoded API keys, tokens, passwordsauth_agentReviews authentication and access control patterns


Notes


The tool uses time.sleep(3) between LLM calls to respect Groq API rate limits
Make sure your .env file is never committed to GitHub — it's in .gitignore
Tested on Windows with conda and VSCode



Author

Riman Tamang


GitHub: @rimantamang
LinkedIn: riman-tamang
