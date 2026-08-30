from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rules import analyze_message
from ocr import extract_text_from_image
from language import detect_language
from ml_detector import analyze_with_ml

from PIL import Image
import io

app = FastAPI(
    title="SurakshaText API",
    description="Regional-language phishing detection API",
    version="1.0.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "https://suraksha-text.vercel.app"
],
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
    ml_result = analyze_with_ml(request.text)

    return {
        **result,
        "ml_analysis": ml_result
    }

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes))

    extracted_text = extract_text_from_image(image)

    language = detect_language(extracted_text)
    result = analyze_message(extracted_text)
    ml_result = analyze_with_ml(extracted_text)

    return {
        "extracted_text": extracted_text,
        "language": language,
        "analysis": result,
        "ml_analysis": ml_result
    }