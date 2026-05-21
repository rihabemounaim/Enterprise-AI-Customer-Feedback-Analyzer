from pathlib import Path


def load_prompt(prompt_path: str) -> str:
    """
    Load a prompt template from file.
    """

    path = Path(prompt_path)

    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return path.read_text(encoding="utf-8")
