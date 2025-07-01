class NGramModel:
    """
    A simple N-Gram language model implemented from scratch.
    Supports unigram, bigram, trigram generation, probability calculation, and next-word prediction.
    """

    def __init__(self, text: str):
        # Initialize with input text
        self.text = text
        self.tokens = self._tokenize(text)

        # Generate n-grams
        self.unigrams = self._generate_ngrams(1)
        self.bigrams = self._generate_ngrams(2)
        self.trigrams = self._generate_ngrams(3)

        # Frequency counts
        self.unigram_freq = self._count_ngrams(self.unigrams)
        self.bigram_freq = self._count_ngrams(self.bigrams)
        self.trigram_freq = self._count_ngrams(self.trigrams)

        # Probability model
        self.bigram_probs = self._compute_bigram_probabilities()

    def _tokenize(self, text: str) -> list:
        """
        Lowercase and split the text into tokens, handling basic punctuation.
        """
        punctuations = ".,!?;:"
        for p in punctuations:
            text = text.replace(p, f" {p} ")
        return text.lower().split()

    def _generate_ngrams(self, n: int) -> list:
        """
        Generate n-grams from token list.
        """
        return [tuple(self.tokens[i:i+n]) for i in range(len(self.tokens) - n + 1)]

    def _count_ngrams(self, ngrams_list: list) -> dict:
        """
        Count frequency of each n-gram.
        """
        counts = {}
        for gram in ngrams_list:
            counts[gram] = counts.get(gram, 0) + 1
        return counts

    def _compute_bigram_probabilities(self) -> dict:
        """
        Calculate conditional probability for each bigram: P(w2 | w1)
        """
        probs = {}
        for (w1, w2), count in self.bigram_freq.items():
            unigram_count = self.unigram_freq.get((w1,), 1)
            probs[(w1, w2)] = count / unigram_count
        return probs

    def show_ngrams(self):
        """
        Display all unigrams, bigrams, and trigrams.
        """
        print("\nUnigrams:", self.unigrams)
        print("Bigrams:", self.bigrams)
        print("Trigrams:", self.trigrams)

    def show_bigram_probabilities(self):
        """
        Print each bigram and its probability.
        """
        print("\nBigram Probabilities:")
        for pair, prob in self.bigram_probs.items():
            print(f"{pair}: {prob:.4f}")

    def predict_nextword(self, prev_word: str, top_n: int = 3) -> list:
        """
        Predict the top N most likely next words given the previous word.
        """
        candidates = [(w2, prob) for (w1, w2), prob in self.bigram_probs.items() if w1 == prev_word]
        candidates.sort(key=lambda x: x[1], reverse=True)
        return [word for word, _ in candidates[:top_n]]
