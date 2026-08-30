def detect_language(text: str) -> str:
    """
    Detect language based on Unicode script.

    Supports:
    - English
    - Hindi
    - Kannada
    """

    if not text or not text.strip():
        return "Unknown"

    hindi_count = 0
    kannada_count = 0
    english_count = 0

    for char in text:
        code = ord(char)

        # Devanagari: Hindi
        if 0x0900 <= code <= 0x097F:
            hindi_count += 1

        # Kannada
        elif 0x0C80 <= code <= 0x0CFF:
            kannada_count += 1

        # English alphabet
        elif ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            english_count += 1

    if hindi_count > kannada_count and hindi_count > english_count:
        return "Hindi"

    if kannada_count > hindi_count and kannada_count > english_count:
        return "Kannada"

    if english_count > 0:
        return "English"

    return "Unknown"