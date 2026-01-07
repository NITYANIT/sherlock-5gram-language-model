import os
from model import NGramLanguageModel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sherlock.txt")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

model = NGramLanguageModel(n=5)
model.train(text)

prompts = [
     "the day was very", 
     "i could not help",
"it was a singular",
"holmes looked at me",
"there was a man"
]

for i, prompt in enumerate(prompts, 1):
    print(f"\nSample {i}")
    print("Input Text :", prompt)
    print("Output Text:", model.generate(prompt, max_words=40))
