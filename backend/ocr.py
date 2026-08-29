import os

import pytesseract
from PIL import Image


# Configure Tesseract path depending on the environment
if os.name == "nt":
    # Windows
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
else:
    # Linux / Render
    pytesseract.pytesseract.tesseract_cmd = "tesseract"


def extract_text_from_image(image: Image.Image) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Supports:
    - English
    - Hindi
    - Kannada
    """

    text = pytesseract.image_to_string(
        image,
        lang="eng+hin+kan"
    )

    return text.strip()