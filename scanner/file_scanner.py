import os
from pathlib import Path

IGNORED_DIRS = {
    "node_modules", "venv", ".git", "build",
    "dist", "__pycache__", ".venv", ".env"
}

SUPPORTED_EXTENSIONS = {
    ".py", ".js", ".ts", ".env",
}

SUPPORTED_FILENAMES = {
    "requirements.txt", "package.json"
}

IGNORED_FILES = {
    "__init__.py"
}


def scan_repository(root_path: str) -> list[dict]:
    root = Path(root_path).resolve()
    collected_files = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]

        for filename in filenames:
            file_path = Path(dirpath) / filename
            extension = file_path.suffix.lower()

            if (extension in SUPPORTED_EXTENSIONS or filename in SUPPORTED_FILENAMES) and filename not in IGNORED_FILES:
                collected_files.append({
                    "path": str(file_path),
                    "filename": filename,
                    "extension": extension,
                })

    return collected_files