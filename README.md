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
├── ngram.py # Main class
├── main.py # Sample usage script
├── init.py # Makes the folder a package
└── README.md # This file

n_gram/
├── __init__.py      # Makes the folder a Python package
├── ngram.py         # Main NGram class implementation
├── main.py          # Sample usage script
└── README.md        # Documentation (this file)
---

## 🔧 Installation

No special libraries are required. Just clone the repo and run with Python 3.6+.

```bash
git clone https://github.com/aburoobhaa/n_gram.git
cd n_gram
python main.py

----
