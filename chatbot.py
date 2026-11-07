"""Simple FAQ chatbot using only Python's standard library."""
import csv
import re
from difflib import SequenceMatcher
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faqs.csv"


def words(text):
    return re.findall(r"[a-z0-9]+", str(text).lower())


def score_match(user_text, question, answer):
    user_words = set(words(user_text))
    question_words = set(words(question))
    answer_words = set(words(answer))
    if not user_words:
        return 0.0
    q_overlap = len(user_words & question_words) / max(1, len(user_words | question_words))
    a_overlap = len(user_words & answer_words) / max(1, len(user_words | answer_words))
    sequence = SequenceMatcher(None, " ".join(words(user_text)),
                               " ".join(words(question))).ratio()
    return 0.65 * q_overlap + 0.15 * a_overlap + 0.20 * sequence


class FAQBot:
    def __init__(self, csv_path=FAQ_FILE, threshold=0.18):
        self.csv_path = Path(csv_path)
        self.threshold = threshold
        self.faqs = self.load_faqs()

    def load_faqs(self):
        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"Cannot find {self.csv_path.name}. Keep it beside chatbot.py."
            )
        with self.csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or not {"question", "answer"}.issubset(
                {h.strip().lower() for h in reader.fieldnames}
            ):
                raise ValueError("CSV must contain columns named question and answer.")
            rows = []
            for row in reader:
                clean = {str(k).strip().lower(): (v or "").strip()
                         for k, v in row.items() if k is not None}
                if clean.get("question") and clean.get("answer"):
                    rows.append({"question": clean["question"], "answer": clean["answer"]})
        if not rows:
            raise ValueError("No valid FAQ rows found in faqs.csv.")
        return rows

    def ask(self, text):
        if not words(text):
            return "Please type a question."
        ranked = sorted(
            ((score_match(text, faq["question"], faq["answer"]), faq)
             for faq in self.faqs),
            key=lambda item: item[0],
            reverse=True
        )
        best_score, best = ranked[0]
        if best_score < self.threshold:
            suggestions = "\n".join(f"- {faq['question']}" for _, faq in ranked[:3])
            return "Sorry, I could not find a confident answer. Try:\n" + suggestions
        return f"{best['answer']}\n(confidence: {best_score:.0%})"


def main():
    try:
        bot = FAQBot()
    except (OSError, ValueError) as exc:
        print(f"Setup error: {exc}")
        return

    print("=" * 44)
    print("           SIMPLE FAQ CHATBOT")
    print("=" * 44)
    print(f"Loaded {len(bot.faqs)} FAQs.")
    print("Ask a question. Type help for examples or quit to exit.")

    while True:
        try:
            question = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break
        if question.lower() in {"quit", "exit", "bye"}:
            print("Bot: Goodbye!")
            break
        if question.lower() == "help":
            print("Example questions:")
            for faq in bot.faqs[:5]:
                print("-", faq["question"])
        else:
            print("Bot:", bot.ask(question))


if __name__ == "__main__":
    main()
