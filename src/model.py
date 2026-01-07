import random
import re
from collections import defaultdict

class NGramLanguageModel:
    def __init__(self, n=5):
        self.n = n
        self.model = defaultdict(lambda: defaultdict(int))

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z.\s]", "", text)
        return text.split()

    def train(self, text):
        tokens = self.preprocess(text)
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i + self.n - 1])
            next_word = tokens[i + self.n - 1]
            self.model[context][next_word] += 1

    def generate(self, seed_text, max_words=40):
        seed_tokens = self.preprocess(seed_text)

        if len(seed_tokens) < self.n - 1:
            raise ValueError("The text in /data must have at least 4 words for a 5-gram model.")

        generated = seed_tokens[:]
        context = tuple(seed_tokens[-(self.n - 1):])

        for _ in range(max_words):
            if context not in self.model:
                context = random.choice(list(self.model.keys()))

            next_words = self.model[context]
            words = list(next_words.keys())
            weights = list(next_words.values())

            next_word = random.choices(words, weights=weights)[0]
            generated.append(next_word)
            
            if next_word.endswith("."):
                break

            context = tuple(generated[-(self.n - 1):])

        return " ".join(generated)
