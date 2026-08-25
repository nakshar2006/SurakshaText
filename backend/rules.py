import re


# Keywords and their risk weights
RULES = {
    "urgency": {
        "keywords": [
            "urgent",
            "immediately",
            "now",
            "hurry",
            "today",
            "within 24 hours",
            "act now",
            "last warning",
            "final warning"
        ],
        "score": 15,
        "label": "Urgency / Pressure"
    },

    "credential_request": {
        "keywords": [
            "otp",
            "password",
            "pin",
            "cvv",
            "passcode",
            "verification code",
            "login",
            "verify your account",
            "verify account"
        ],
        "score": 25,
        "label": "Credential / OTP Request"
    },

    "account_threat": {
        "keywords": [
            "account blocked",
            "account suspended",
            "account will be blocked",
            "account will be suspended",
            "account terminated",
            "kyc expired",
            "kyc will expire",
            "legal action",
            "police complaint"
        ],
        "score": 20,
        "label": "Account Threat"
    },

    "financial_bait": {
        "keywords": [
            "prize",
            "reward",
            "cashback",
            "lottery",
            "won",
            "winner",
            "free money",
            "claim your money",
            "refund",
            "cash prize"
        ],
        "score": 20,
        "label": "Financial / Reward Bait"
    },

    "suspicious_action": {
        "keywords": [
            "click here",
            "click the link",
            "open the link",
            "download now",
            "install now",
            "update your account",
            "confirm now"
        ],
        "score": 15,
        "label": "Suspicious Action Request"
    }
}


def contains_keyword(text, keyword):
    """
    Checks whether a keyword exists in the message.
    """
    return keyword.lower() in text.lower()


def detect_suspicious_url(text):
    """
    Detects URLs and gives additional risk if a message
    contains a link.
    """

    url_pattern = r"(https?://\S+|www\.\S+)"
    urls = re.findall(url_pattern, text, re.IGNORECASE)

    if urls:
        return True, urls

    return False, []


def analyze_message(text):
    """
    Analyze a message and return:
    - risk score
    - classification
    - detected indicators
    - matched keywords
    - safety recommendation
    """

    if not text or not text.strip():
        return {
            "message": text,
            "risk_score": 0,
            "classification": "SAFE",
            "indicators": [],
            "matched_keywords": [],
            "recommendation": "No message was provided."
        }

    score = 0
    indicators = []
    matched_keywords = []

    # Check keyword-based rules
    for rule in RULES.values():

        rule_triggered = False

        for keyword in rule["keywords"]:

            if contains_keyword(text, keyword):

                score += rule["score"]
                matched_keywords.append(keyword)

                rule_triggered = True

        if rule_triggered:
            indicators.append(rule["label"])

    # Check suspicious URLs
    url_found, urls = detect_suspicious_url(text)

    if url_found:
        score += 25
        indicators.append("Suspicious Link")

    # Prevent score from exceeding 100
    score = min(score, 100)

    # Classification
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

    return {
        "message": text,
        "risk_score": score,
        "classification": classification,
        "indicators": indicators,
        "matched_keywords": matched_keywords,
        "urls_found": urls,
        "recommendation": recommendation
    }
