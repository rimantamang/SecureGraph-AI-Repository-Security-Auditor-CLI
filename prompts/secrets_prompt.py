SECRETS_PROMPT = """You are a secrets detection expert. Analyze this code for hardcoded secrets.

Look for:
- Hardcoded API keys or tokens
- Hardcoded passwords or credentials
- Hardcoded private keys or certificates
- Hardcoded database connection strings
- Any other exposed sensitive information

File: {filename}
Code:
{content}

Respond ONLY in this exact format for each finding (if any):
SEVERITY: HIGH or MEDIUM or LOW
ISSUE: name of the issue
LINE: best guess at line number or 0 if unknown
REASON: one sentence explanation
FIX: one sentence fix suggestion
---

If no secrets found, respond with: NONE"""