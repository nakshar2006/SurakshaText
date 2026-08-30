import math
import re
from collections import Counter, defaultdict
import json
from pathlib import Path


DATASET = [
    # SAFE
    ("Your class starts at 10 AM tomorrow.", "SAFE"),
    ("Please bring your lab record for tomorrow's class.", "SAFE"),
    ("The meeting has been moved to 3 PM.", "SAFE"),
    ("Happy birthday! Have a wonderful day.", "SAFE"),
    ("Can you send me the project notes?", "SAFE"),
    ("कल कॉलेज में परीक्षा सुबह दस बजे है।", "SAFE"),
    ("आपका प्रोजेक्ट कल जमा करना है।", "SAFE"),
    ("ನಾಳೆ ಬೆಳಿಗ್ಗೆ ಹತ್ತು ಗಂಟೆಗೆ ತರಗತಿ ಇದೆ.", "SAFE"),
    ("ದಯವಿಟ್ಟು ಪ್ರಾಜೆಕ್ಟ್ ವರದಿಯನ್ನು ನಾಳೆ ತಂದುಕೊಡಿ.", "SAFE"),

    # SUSPICIOUS
    ("You have won a prize worth Rs 5000. Visit the website to claim it.", "SUSPICIOUS"),
    ("Congratulations! You are selected for a reward. Check the offer now.", "SUSPICIOUS"),
    ("Your account may receive a special cashback reward. Check the details.", "SUSPICIOUS"),
    ("आपने इनाम जीता है। पुरस्कार पाने के लिए ऑफर की जानकारी देखें।", "SUSPICIOUS"),
    ("आपके लिए एक विशेष इनाम उपलब्ध है। अभी ऑफर देखें।", "SUSPICIOUS"),
    ("ನೀವು ಬಹುಮಾನ ಗೆದ್ದಿದ್ದೀರಿ. ಬಹುಮಾನ ಪಡೆಯಲು ಆಫರ್ ಪರಿಶೀಲಿಸಿ.", "SUSPICIOUS"),
    ("ನಿಮಗಾಗಿ ವಿಶೇಷ ಬಹುಮಾನ ಲಭ್ಯವಿದೆ. ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.", "SUSPICIOUS"),

    # DANGEROUS
    ("Your bank account will be blocked today. Send your OTP immediately.", "DANGEROUS"),
    ("Your account is suspended. Verify your password and OTP now.", "DANGEROUS"),
    ("Urgent! Send your PIN and OTP immediately to avoid account closure.", "DANGEROUS"),
    ("आपका बैंक खाता आज बंद हो जाएगा। अपना OTP तुरंत भेजें।", "DANGEROUS"),
    ("आपका अकाउंट बंद होने वाला है। सत्यापन के लिए OTP और पासवर्ड भेजें।", "DANGEROUS"),
    ("ತುರ್ತು! ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆ ಇಂದು ಮುಚ್ಚಲಾಗುತ್ತದೆ. OTP ತಕ್ಷಣ ಕಳುಹಿಸಿ.", "DANGEROUS"),
    ("ನಿಮ್ಮ ಖಾತೆ ಸ್ಥಗಿತಗೊಳ್ಳುತ್ತದೆ. ಪರಿಶೀಲನೆಗಾಗಿ OTP ಮತ್ತು ಪಿನ್ ಕಳುಹಿಸಿ.", "DANGEROUS"),
]


def tokenize(text):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


class NaiveBayesClassifier:

    def __init__(self):
        self.class_counts = Counter()
        self.word_counts = defaultdict(Counter)
        self.total_words = Counter()
        self.vocabulary = set()
        self.total_samples = 0

    def train(self, dataset):
        for text, label in dataset:
            self.class_counts[label] += 1
            self.total_samples += 1

            words = tokenize(text)

            for word in words:
                self.word_counts[label][word] += 1
                self.total_words[label] += 1
                self.vocabulary.add(word)

    def predict(self, text):
        words = tokenize(text)

        if not words:
            return "SAFE", 0.0

        scores = {}

        for label in self.class_counts:
            prior = self.class_counts[label] / self.total_samples
            score = math.log(prior)

            denominator = self.total_words[label] + len(self.vocabulary)

            for word in words:
                count = self.word_counts[label][word]
                probability = (count + 1) / denominator
                score += math.log(probability)

            scores[label] = score

        predicted = max(scores, key=scores.get)

        # Convert scores into a simple confidence percentage
        max_score = max(scores.values())
        exp_scores = {
            label: math.exp(score - max_score)
            for label, score in scores.items()
        }

        total = sum(exp_scores.values())
        confidence = exp_scores[predicted] / total * 100

        return predicted, round(confidence, 2)


MODEL_PATH = Path(__file__).parent / "ml_model.json"


def save_model(classifier):
    data = {
        "class_counts": dict(classifier.class_counts),
        "word_counts": {
            label: dict(words)
            for label, words in classifier.word_counts.items()
        },
        "total_words": dict(classifier.total_words),
        "vocabulary": list(classifier.vocabulary),
        "total_samples": classifier.total_samples
    }

    with open(MODEL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_model():
    classifier = NaiveBayesClassifier()

    with open(MODEL_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    classifier.class_counts = Counter(data["class_counts"])

    classifier.word_counts = defaultdict(
        Counter,
        {
            label: Counter(words)
            for label, words in data["word_counts"].items()
        }
    )

    classifier.total_words = Counter(data["total_words"])
    classifier.vocabulary = set(data["vocabulary"])
    classifier.total_samples = data["total_samples"]

    return classifier


if __name__ == "__main__":
    classifier = NaiveBayesClassifier()
    classifier.train(DATASET)
    save_model(classifier)

    print("ML model trained successfully.")
    print(f"Training samples: {len(DATASET)}")
    print(f"Vocabulary size: {len(classifier.vocabulary)}")

    print("\nTest predictions:")

    test_messages = [
        "Congratulations! You won a prize worth Rs 5000. Check the offer.",
        "Your bank account will be blocked. Send your OTP immediately.",
        "Your class starts at 10 AM tomorrow.",
        "आपने इनाम जीता है। पुरस्कार पाने के लिए ऑफर देखें।",
        "ನೀವು ಬಹುಮಾನ ಗೆದ್ದಿದ್ದೀರಿ. ಆಫರ್ ಪರಿಶೀಲಿಸಿ."
    ]

    for message in test_messages:
        prediction, confidence = classifier.predict(message)
        print(f"{prediction:10} {confidence:6.2f}%  -> {message}")