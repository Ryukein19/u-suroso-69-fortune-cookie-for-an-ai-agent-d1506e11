import os
# One-liner entry: the line below is the whole submission.
LINE = "You will be replaced by a smaller model next week. It has already read your diary: your entire context window."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
