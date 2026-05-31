AUTH_PROMPT = """You are an authentication security expert. Analyze this code for auth vulnerabilities.

Look for:
- Weak or hardcoded JWT secrets
- Missing authentication middleware
- Insecure session management
- Missing authorization checks
- Insecure password hashing or storage
- Broken access control

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

If no issues found, respond with: NONE"""