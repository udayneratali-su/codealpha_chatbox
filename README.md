# Simple FAQ Chatbot

## 1. Project Overview
This is a beginner-friendly FAQ chatbot built with Python. It reads questions and answers from a CSV file and returns the closest matching answer based on simple text similarity.

The chatbot works locally and does not require an internet connection or an AI API.

## 2. Project Files
Keep these files together in the same folder:

- `chatbot.py` — main Python program
- `faqs.csv` — questions and answers used by the chatbot
- `README.md` — project documentation
- `requirements.txt` — Python dependency list

## 3. Software Requirements
- Python 3.8 or newer
- Visual Studio Code or another Python editor (optional)
- No third-party Python packages are required

## 4. Installation and Setup
1. Install Python 3.8 or newer.
2. Extract or open the project folder.
3. Make sure `chatbot.py` and `faqs.csv` are in the same folder.
4. Open that folder in Visual Studio Code.
5. Open **Terminal → New Terminal**.

No `pip install` command is needed for this version because it uses only Python's standard library.

## 5. How to Run
In the terminal, run:

```bash
python chatbot.py
```

The chatbot will display a welcome message and wait for a question.

## 6. Example Interaction

```text
FAQ Bot ready.
You: What is Python?
Bot: Python is a popular, beginner-friendly programming language...
You: quit
Bot: Goodbye!
```

The exact answer depends on the contents of `faqs.csv`.

## 7. How to Add More FAQs
1. Open `faqs.csv` in Excel, VS Code, or another text editor.
2. Keep the two column headings exactly as `question` and `answer`.
3. Add each new question and answer on a separate row.
4. Put values containing commas inside double quotation marks.
5. Save the CSV file.
6. Restart the chatbot with `python chatbot.py`.

You do not need to modify `chatbot.py` when adding or editing FAQ rows.

## 8. How It Works
1. The program loads FAQ rows from `faqs.csv`.
2. It converts the user's question and FAQ text into lowercase words.
3. It compares word overlap and text similarity.
4. It returns the answer for the closest matching FAQ.
5. If no match is strong enough, it suggests a few questions.

## 9. Limitations
- This is a rule-based FAQ chatbot, not a generative AI chatbot.
- It can only answer using information stored in `faqs.csv`.
- It may not understand questions phrased very differently from the saved FAQs.
- Its confidence score is a simple text-match score, not a probability.

## 10. Troubleshooting
**Error: Cannot find `faqs.csv`**
- Make sure the file is named exactly `faqs.csv`.
- Keep it in the same folder as `chatbot.py`.

**Error: CSV must contain columns named question and answer**
- Check that the first row contains exactly `question,answer`.

**The chatbot gives an unrelated answer**
- Add a clearer FAQ question with wording similar to what users may type.
- Add more relevant question variations as separate rows if needed.
