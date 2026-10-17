from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AIO AI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


@app.get("/")
def root():
    return {"name": "AIO AI Backend", "status": "running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        return {
            "reply": "စာတစ်ခုခု ရေးပို့ပေးပါ။",
            "session_id": request.session_id,
            "model_connected": False,
        }

    return {
        "reply": (
            "AIO AI Backend ကို အောင်မြင်စွာ ချိတ်ဆက်နိုင်ပါပြီ။ "
            "AI Model အစစ် မချိတ်ဆက်ရသေးတဲ့အတွက် "
            "ဒီအဖြေဟာ စမ်းသပ်အဖြေဖြစ်ပါတယ်။"
        ),
        "session_id": request.session_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_connected": False,
    }


@app.get("/memory/{session_id}")
def get_memory(session_id: str):
    return {
        "session_id": session_id,
        "messages": [],
        "storage_connected": False,
    }


@app.delete("/memory/{session_id}")
def clear_memory(session_id: str):
    return {
        "session_id": session_id,
        "cleared": False,
        "message": "Memory database is not configured yet.",
    }