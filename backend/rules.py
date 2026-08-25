import re


# ============================================================
# SURAKSHATEXT PHISHING DETECTION RULES
# Languages: English + Kannada + Hindi
# ============================================================

RULES = {

    # --------------------------------------------------------
    # URGENCY / PRESSURE
    # --------------------------------------------------------

    "urgency": {
        "keywords": [
            # English
            "urgent",
            "immediately",
            "now",
            "hurry",
            "today",
            "within 24 hours",
            "act now",
            "last warning",
            "final warning",

            # Kannada
            "ತಕ್ಷಣ",
            "ತುರ್ತು",
            "ಈಗಲೇ",
            "ಇಂದೇ",
            "24 ಗಂಟೆಗಳೊಳಗೆ",
            "ಕೊನೆಯ ಎಚ್ಚರಿಕೆ",

            # Hindi
            "तुरंत",
            "अति आवश्यक",
            "अभी",
            "आज ही",
            "24 घंटे के अंदर",
            "अंतिम चेतावनी",

            # Romanized
            "turant",
            "abhi",
            "aaj hi",
            "jaldi",
            "tvarit"
        ],
        "score": 15,
        "label": "Urgency / Pressure"
    },


    # --------------------------------------------------------
    # CREDENTIAL / OTP REQUEST
    # --------------------------------------------------------

    "credential_request": {
        "keywords": [
            # English
            "otp",
            "password",
            "pin",
            "cvv",
            "passcode",
            "verification code",
            "login",
            "verify your account",
            "verify account",

            # Kannada
            "ಒಟಿಪಿ",
            "ಪಾಸ್ವರ್ಡ್",
            "ಪಿನ್",
            "ಸಿವಿವಿ",
            "ಪರಿಶೀಲನಾ ಕೋಡ್",
            "ಖಾತೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
            "ಖಾತೆ ಪರಿಶೀಲನೆ",

            # Hindi
            "ओटीपी",
            "पासवर्ड",
            "पिन",
            "सीवीवी",
            "सत्यापन कोड",
            "अपना खाता सत्यापित करें",
            "खाता सत्यापन",

            # Romanized
            "otp",
            "password",
            "pin",
            "cvv",
            "verification code",
            "khata verify",
            "account verify"
        ],
        "score": 25,
        "label": "Credential / OTP Request"
    },


    # --------------------------------------------------------
    # REQUEST TO SHARE CREDENTIALS
    # --------------------------------------------------------

    "credential_sharing": {
        "keywords": [
            # English
            "share otp",
            "send otp",
            "tell me the otp",
            "tell us the otp",
            "give me the otp",
            "give us the otp",
            "provide otp",
            "send password",
            "share password",
            "tell me your password",
            "share your pin",
            "send your pin",
            "share cvv",

            # Kannada
            "ಒಟಿಪಿ ಹಂಚಿಕೊಳ್ಳಿ",
            "ಒಟಿಪಿ ಕಳುಹಿಸಿ",
            "ಒಟಿಪಿ ತಿಳಿಸಿ",
            "ಒಟಿಪಿ ನೀಡಿ",
            "ಪಾಸ್ವರ್ಡ್ ಹಂಚಿಕೊಳ್ಳಿ",
            "ಪಿನ್ ಹಂಚಿಕೊಳ್ಳಿ",

            # Hindi
            "ओटीपी साझा करें",
            "ओटीपी भेजें",
            "ओटीपी बताएं",
            "ओटीपी दें",
            "पासवर्ड साझा करें",
            "पिन साझा करें",

            # Romanized
            "otp share karo",
            "otp bhejo",
            "otp batao",
            "otp do",
            "password share karo",
            "pin share karo"
        ],
        "score": 45,
        "label": "Request to Share Credentials"
    },


    # --------------------------------------------------------
    # ACCOUNT THREAT
    # --------------------------------------------------------

    "account_threat": {
        "keywords": [
            # English
            "account blocked",
            "account suspended",
            "account will be blocked",
            "account will be suspended",
            "account terminated",
            "kyc expired",
            "kyc will expire",
            "legal action",
            "police complaint",

            # Kannada
            "ಖಾತೆ ನಿರ್ಬಂಧಿಸಲಾಗಿದೆ",
            "ಖಾತೆ ನಿರ್ಬಂಧಿಸಲಾಗುತ್ತದೆ",
            "ಖಾತೆ ಸ್ಥಗಿತಗೊಳಿಸಲಾಗಿದೆ",
            "ಖಾತೆ ಸ್ಥಗಿತಗೊಳಿಸಲಾಗುತ್ತದೆ",
            "ಖಾತೆಯನ್ನು ಮುಚ್ಚಲಾಗುತ್ತದೆ",
            "ಕೆವೈಸಿ ಅವಧಿ ಮುಗಿದಿದೆ",
            "ಕಾನೂನು ಕ್ರಮ",
            "ಪೊಲೀಸ್ ದೂರು",

            # Hindi
            "खाता ब्लॉक कर दिया जाएगा",
            "खाता बंद कर दिया जाएगा",
            "खाता निलंबित कर दिया जाएगा",
            "खाता निलंबित है",
            "खाता समाप्त कर दिया जाएगा",
            "केवाईसी समाप्त हो गया है",
            "कानूनी कार्रवाई",
            "पुलिस शिकायत",

            # Romanized
            "khata block",
            "khata band",
            "account block",
            "account band",
            "kyc expire",
            "kanooni karwai"
        ],
        "score": 20,
        "label": "Account Threat"
    },


    # --------------------------------------------------------
    # FINANCIAL / BANKING CONTEXT
    # --------------------------------------------------------

    "financial_context": {
        "keywords": [
            # English
            "bank",
            "bank account",
            "credit card",
            "debit card",
            "upi",
            "payment",
            "transaction",
            "net banking",
            "online banking",
            "wallet",

            # Kannada
            "ಬ್ಯಾಂಕ್",
            "ಬ್ಯಾಂಕ್ ಖಾತೆ",
            "ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
            "ಡೆಬಿಟ್ ಕಾರ್ಡ್",
            "ಪಾವತಿ",
            "ವಹಿವಾಟು",
            "ಆನ್ಲೈನ್ ಬ್ಯಾಂಕಿಂಗ್",
            "ವಾಲೆಟ್",

            # Hindi
            "बैंक",
            "बैंक खाता",
            "क्रेडिट कार्ड",
            "डेबिट कार्ड",
            "भुगतान",
            "लेनदेन",
            "ऑनलाइन बैंकिंग",
            "वॉलेट",

            # Romanized
            "bank",
            "bank account",
            "credit card",
            "debit card",
            "bhugtan",
            "len den",
            "bank khata"
        ],
        "score": 10,
        "label": "Financial / Banking Context"
    },


    # --------------------------------------------------------
    # FINANCIAL / REWARD BAIT
    # --------------------------------------------------------

    "financial_bait": {
        "keywords": [
            # English
            "prize",
            "reward",
            "cashback",
            "lottery",
            "won",
            "winner",
            "free money",
            "claim your money",
            "refund",
            "cash prize",

            # Kannada
            "ಬಹುಮಾನ",
            "ನಗದು ಬಹುಮಾನ",
            "ಲಾಟರಿ",
            "ನೀವು ಗೆದ್ದಿದ್ದೀರಿ",
            "ಕ್ಯಾಶ್‌ಬ್ಯಾಕ್",
            "ಹಣವನ್ನು ಪಡೆಯಿರಿ",

            # Hindi
            "इनाम",
            "पुरस्कार",
            "कैशबैक",
            "लॉटरी",
            "आप जीत गए हैं",
            "मुफ्त पैसे",
            "पैसे का दावा करें",

            # Romanized
            "inaam",
            "puraskar",
            "lottery",
            "aap jeet gaye",
            "cashback",
            "muft paise"
        ],
        "score": 20,
        "label": "Financial / Reward Bait"
    },


    # --------------------------------------------------------
    # SUSPICIOUS ACTION
    # --------------------------------------------------------

    "suspicious_action": {
        "keywords": [
            # English
            "click here",
            "click the link",
            "open the link",
            "download now",
            "install now",
            "update your account",
            "confirm now",

            # Kannada
            "ಇಲ್ಲಿ ಕ್ಲಿಕ್ ಮಾಡಿ",
            "ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಿ",
            "ಲಿಂಕ್ ತೆರೆಯಿರಿ",
            "ಈಗ ಡೌನ್ಲೋಡ್ ಮಾಡಿ",
            "ಖಾತೆಯನ್ನು ನವೀಕರಿಸಿ",
            "ಈಗ ದೃಢೀಕರಿಸಿ",
            "ಬಹುಮಾನ",
            "ಲಾಟರಿ",
            "ನಗದು",
            "ಬಹುಮಾನ ಗೆದ್ದಿದ್ದೀರಿ",
            "ಹಣ ಪಡೆಯಿರಿ",


            # Hindi
            "यहां क्लिक करें",
            "लिंक पर क्लिक करें",
            "लिंक खोलें",
            "अभी डाउनलोड करें",
            "अपना खाता अपडेट करें",
            "अभी पुष्टि करें",
            "इनाम",
            "लॉटरी",
            "नकद",
            "इनाम जीता",
            "पैसे प्राप्त करें",

            # Romanized
            "yaha click karo",
            "link par click karo",
            "link kholo",
            "abhi download karo",
            "account update karo",
            "confirm karo"
        ],
        "score": 15,
        "label": "Suspicious Action Request"
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def contains_keyword(text, keyword):
    """
    Checks whether a keyword exists in the message.
    """

    return keyword.lower() in text.lower()


def detect_suspicious_url(text):
    """
    Detects URLs in the message.
    """

    url_pattern = r"(https?://\S+|www\.\S+)"

    urls = re.findall(
        url_pattern,
        text,
        re.IGNORECASE
    )

    if urls:
        return True, urls

    return False, []


# ============================================================
# MAIN ANALYSIS FUNCTION
# ============================================================

def analyze_message(text):

    """
    Analyze a message and return:

    - risk score
    - classification
    - detected indicators
    - matched keywords
    - URLs
    - safety recommendation
    """

    if not text or not text.strip():

        return {
            "message": text,
            "risk_score": 0,
            "classification": "SAFE",
            "indicators": [],
            "matched_keywords": [],
            "urls_found": [],
            "recommendation": "No message was provided."
        }


    score = 0

    indicators = []

    matched_keywords = []


    # --------------------------------------------------------
    # Keyword-based rules
    # --------------------------------------------------------

    for rule in RULES.values():

        rule_triggered = False

        for keyword in rule["keywords"]:

            if contains_keyword(text, keyword):

                score += rule["score"]

                matched_keywords.append(keyword)

                rule_triggered = True


        if rule_triggered:

            indicators.append(rule["label"])


    # --------------------------------------------------------
    # Combination detection
    # --------------------------------------------------------

    lower_text = text.lower()


    credential_words = [

        # English
        "otp",
        "password",
        "pin",
        "cvv",
        "passcode",
        "verification code",

        # Kannada
        "ಒಟಿಪಿ",
        "ಪಾಸ್ವರ್ಡ್",
        "ಪಿನ್",
        "ಸಿವಿವಿ",
        "ಪರಿಶೀಲನಾ ಕೋಡ್",


        # Hindi
        "ओटीपी",
        "पासवर्ड",
        "पिन",
        "सीवीवी"
        "सत्यापन कोड",
    ]


    sharing_words = [

        # English
        "share",
        "send",
        "tell",
        "give",
        "provide",
        "forward",

        # Kannada
        "ಹಂಚಿಕೊಳ್ಳಿ",
        "ಕಳುಹಿಸಿ",
        "ತಿಳಿಸಿ",
        "ನೀಡಿ",

        # Hindi
        "साझा करें",
        "भेजें",
        "बताएं",
        "दें"
    ]


    banking_words = [

        # English
        "bank",
        "account",
        "upi",
        "payment",
        "transaction",
        "credit card",
        "debit card",

        # Kannada
        "ಬ್ಯಾಂಕ್",
        "ಖಾತೆ",
        "ಪಾವತಿ",
        "ವಹಿವಾಟು",

        # Hindi
        "बैंक",
        "खाता",
        "भुगतान",
        "लेनदेन"
    ]


    has_credential = any(
        word.lower() in lower_text
        for word in credential_words
    )


    has_sharing_request = any(
        word.lower() in lower_text
        for word in sharing_words
    )


    has_banking_context = any(
        word.lower() in lower_text
        for word in banking_words
    )


    # Credential + sharing request
    if has_credential and has_sharing_request:

        score += 30

        if "Credential Sharing Request" not in indicators:

            indicators.append(
                "Credential Sharing Request"
            )


    # Credential + banking context
    if has_credential and has_banking_context:

        score += 20

        if "Banking Credential Request" not in indicators:

            indicators.append(
                "Banking Credential Request"
            )


    # --------------------------------------------------------
    # Suspicious URLs
    # --------------------------------------------------------

    url_found, urls = detect_suspicious_url(text)

    if url_found:

        score += 25

        indicators.append("Suspicious Link")


    # --------------------------------------------------------
    # Limit score
    # --------------------------------------------------------

    score = min(score, 100)


    # --------------------------------------------------------
    # Classification
    # --------------------------------------------------------

    if score >= 60:

        classification = "DANGEROUS"

        recommendation = (
            "Do not click links, share OTPs, passwords or financial "
            "information. Verify the message through an official source."
        )


    elif score >= 30:

        classification = "SUSPICIOUS"

        recommendation = (
            "Be careful with this message. Verify the sender and "
            "avoid clicking unknown links or sharing sensitive information."
        )


    else:

        classification = "SAFE"

        recommendation = (
            "No strong phishing indicators were detected. "
            "Still verify unexpected messages before taking action."
        )


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "message": text,

        "risk_score": score,

        "classification": classification,

        "indicators": indicators,

        "matched_keywords": matched_keywords,

        "urls_found": urls,

        "recommendation": recommendation
    }