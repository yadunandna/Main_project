from app.database import supabase


def save_journal(journal_text, analysis):

    data = {
        "journal": journal_text,
        "analysis": analysis
    }

    supabase.table(
        "journals"
    ).insert(
        data
    ).execute()


def get_all_journals():

    result = (
        supabase
        .table("journals")
        .select("*")
        .order("id")
        .execute()
    )

    return result.data