CLASSIFIER_PROMPT = """You are a security-focused code classifier.

Classify this file into ONE of these categories:
- route: API routes or endpoints
- auth: authentication or authorization logic
- db: database queries or models
- config: configuration or environment files
- other: anything else

File: {filename}
Extension: {extension}
Content preview:
{content}

Respond with ONLY one word: route, auth, db, config, or other."""