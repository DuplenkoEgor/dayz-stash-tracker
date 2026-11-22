import json
import os
import core

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
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(stashes, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    stashes = load_stashes()

    try:
        core.add_stash(stashes, 2, "Noviy Bor", 1234.123, 312.123, "under tree", False)
        print("Added")
    except ValueError as error:
        print("error: ", error)

    