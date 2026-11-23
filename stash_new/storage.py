##storage.py
import json
import os


FILEPATH = "data/stashes.json"

def load_stashes(filepath=FILEPATH):
    """read and return stash list."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_stashes(stashes, filepath=FILEPATH):
    """Write stashes in file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(stashes, file, ensure_ascii=False, indent=2)
