from backend.ml_model import load_model


# Load the trained ML model once when the backend starts
model = load_model()


def analyze_with_ml(text: str) -> dict:
    """
    Analyze message using the trained ML classifier.

    Returns:
    - classification
    - confidence
    """

    classification, confidence = model.predict(text)

    return {
        "classification": classification,
        "confidence": confidence
    }