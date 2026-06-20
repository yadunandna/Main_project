import json
import os
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "journals.json")


def initialize_storage():
    """
    Create data folder and json file if missing
    """

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def get_all_journals():
    """
    Returns all saved journals
    """

    initialize_storage()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return []


def save_journal(
    journal_text: str,
    analysis: str
):
    """
    Save journal entry
    """

    initialize_storage()

    journals = get_all_journals()

    entry = {
        "id": len(journals) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "journal": journal_text,
        "analysis": analysis
    }

    journals.append(entry)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            journals,
            f,
            indent=4,
            ensure_ascii=False
        )

    return entry


def get_latest_journal():

    journals = get_all_journals()

    if not journals:
        return None

    return journals[-1]


def get_recent_journals(limit=7):

    journals = get_all_journals()

    return journals[-limit:]


def delete_journal(entry_id: int):

    journals = get_all_journals()

    updated = [
        j for j in journals
        if j["id"] != entry_id
    ]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            updated,
            f,
            indent=4,
            ensure_ascii=False
        )

    return True


def total_entries():

    journals = get_all_journals()

    return len(journals)


def search_journals(keyword: str):

    journals = get_all_journals()

    results = []

    keyword = keyword.lower()

    for journal in journals:

        if (
            keyword in journal["journal"].lower()
            or keyword in journal["analysis"].lower()
        ):
            results.append(journal)

    return results


def get_journal_by_id(entry_id: int):

    journals = get_all_journals()

    for journal in journals:

        if journal["id"] == entry_id:
            return journal

    return None