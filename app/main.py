import json

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.ai import analyze_journal, wellness_chat
from app.storage import (
    save_journal,
    get_all_journals,
)
from app.utils import (
    calculate_burnout_risk,
    get_stress_trend,
)

app = FastAPI(
    title="ExamPulse AI",
    description="AI Mental Wellness Tracker for Students",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Templates
templates = Jinja2Templates(directory="templates")


# ==================================================
# HOME PAGE
# ==================================================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    journals = get_all_journals()

    latest_analysis = ""

    if journals:
        latest_analysis = journals[-1].get(
            "analysis",
            ""
        )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "latest_analysis": latest_analysis
        }
    )


# ==================================================
# ANALYZE JOURNAL
# ==================================================
@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    journal: str = Form(...)
):

    if len(journal.strip()) < 10:

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "error": "Journal entry is too short."
            }
        )

    if len(journal) > 3000:

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "error": "Journal exceeds maximum length."
            }
        )

    try:

        ai_result = analyze_journal(journal)

        save_journal(
            journal_text=journal,
            analysis=ai_result
        )

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "result": ai_result,
                "success": "Journal analyzed successfully."
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "error": str(e)
            }
        )


# ==================================================
# DASHBOARD
# ==================================================
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    journals = get_all_journals()

    burnout_risk = calculate_burnout_risk(
        journals
    )

    stress_trend = get_stress_trend(
        journals
    )

    total_entries = len(journals)

    stress_trend_json = json.dumps(
        stress_trend
    )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "entries": journals,
            "total_entries": total_entries,
            "burnout_risk": burnout_risk,
            "stress_trend": stress_trend,
            "stress_trend_json": stress_trend_json
        }
    )


# ==================================================
# CHAT PAGE
# ==================================================
@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={}
    )


# ==================================================
# CHAT API
# ==================================================
@app.post("/chat")
async def chat(
    message: str = Form(...)
):

    try:

        ai_response = wellness_chat(
            message
        )

        return JSONResponse(
            {
                "success": True,
                "response": ai_response
            }
        )

    except Exception as e:

        return JSONResponse(
            {
                "success": False,
                "response": str(e)
            }
        )


# ==================================================
# HEALTH CHECK
# ==================================================
@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "service": "ExamPulse AI"
    }


# ==================================================
# GET JOURNALS
# ==================================================
@app.get("/api/journals")
async def journals():

    return get_all_journals()


# ==================================================
# STATS API
# ==================================================
@app.get("/api/stats")
async def stats():

    journals = get_all_journals()

    return {
        "total_entries": len(journals),
        "burnout_risk": calculate_burnout_risk(
            journals
        ),
        "stress_trend": get_stress_trend(
            journals
        )
    }


# ==================================================
# ROOT API TEST
# ==================================================
@app.get("/ping")
async def ping():

    return {
        "message": "ExamPulse AI Running"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )