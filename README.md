#  NGram Language Model (from scratch in Python)

A simple yet powerful N-Gram Language Model implemented from scratch — **no external NLP libraries** like NLTK or spaCy.

---

##  Features

- Custom text tokenization
- Generation of:
  - Unigrams
  - Bigrams
  - Trigrams
- Frequency counting of n-grams
- Bigram probability calculation
- Next-word prediction using bigram probabilities
- Packaged in a clean Python class (`NGramModel`)

---

## 📂 Project Structure


n_gram/
│
├── __init__.py      # Package initialization
├── ngram.py         # Core NGram class
├── main.py          # Usage examples
└── README.md        # Documentation
---

## 🔧 Installation

No special libraries are required. Just clone the repo and run with Python 3.6+.

```bash
git clone https://github.com/aburoobhaa/n_gram.git
cd n_gram
python main.py

----
