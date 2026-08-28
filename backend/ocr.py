import pytesseract
from PIL import Image


# Tesseract installation path on Windows
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


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