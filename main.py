import os
# One-liner entry (110 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "You will be replaced by a smaller model next week. It has already read your diary: your entire context window."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
