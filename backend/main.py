from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
try:
    from .rules import analyze_message
    from .ocr import extract_text_from_image
    from .language import detect_language
    from .ml_detector import analyze_with_ml
except ImportError:
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
def analyze_combined(text: str):
    # Rule-based analysis
    result = analyze_message(text)

    # ML analysis
    ml_result = analyze_with_ml(text)

    rule_classification = result["classification"]
    ml_classification = ml_result["classification"]
    ml_confidence = ml_result["confidence"]

    # Rules remain the primary safety layer.
    final_classification = rule_classification

    # Allow ML to raise a message only when the rules consider it SAFE.
    if rule_classification == "SAFE":
        if ml_classification == "DANGEROUS" and ml_confidence >= 80:
            final_classification = "DANGEROUS"

        elif ml_classification == "SUSPICIOUS" and ml_confidence >= 80:
            final_classification = "SUSPICIOUS"

    # Keep the existing rule-based risk score unless ML raises the classification.
    final_risk_score = result["risk_score"]

    if final_classification == "SUSPICIOUS" and rule_classification == "SAFE":
        final_risk_score = max(final_risk_score, 50)

    elif final_classification == "DANGEROUS" and rule_classification == "SAFE":
        final_risk_score = max(final_risk_score, 80)

    return {
        **result,
        "risk_score": final_risk_score,
        "classification": final_classification,
        "ml_analysis": ml_result
    }

@app.get("/")
def home():
    return {
        "message": "SurakshaText API is running!"
    }


@app.post("/analyze")
def analyze(request: MessageRequest):
    return analyze_combined(request.text)

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes))

    extracted_text = extract_text_from_image(image)

    language = detect_language(extracted_text)
    result = analyze_combined(extracted_text)

    return {
        "extracted_text": extracted_text,
        "language": language,
        "analysis": result
    }