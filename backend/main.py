from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rules import analyze_message


app = FastAPI(
    title="SurakshaText API",
    description="Regional-language phishing detection API",
    version="1.0.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "SurakshaText API is running!"
    }


@app.post("/analyze")
def analyze(request: MessageRequest):

    result = analyze_message(request.text)

    return result
