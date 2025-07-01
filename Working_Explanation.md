##  How It Works (Flow)

### Input
You enter a sentence like:

```text
I want to explore language modeling.

```

---

###  Tokenization

- Converts the sentence to **lowercase**
- Adds space around **punctuation**
- Splits the sentence into **tokens**

```python
['i', 'want', 'to', 'explore', 'language', 'modeling', '.']
```

---

###  N-Gram Generation

- **Unigrams**:
  ```python
  [('i',), ('want',), ('to',), ('explore',), ('language',), ('modeling',), ('.',)]
  ```

- **Bigrams**:
  ```python
  [('i', 'want'), ('want', 'to'), ('to', 'explore'), ('explore', 'language'), ('language', 'modeling'), ('modeling', '.')]
  ```

- **Trigrams**:
  ```python
  [('i', 'want', 'to'), ('want', 'to', 'explore'), ('to', 'explore', 'language'), ('explore', 'language', 'modeling'), ('language', 'modeling', '.')]
  ```

---

###  Counting

- Counts how many times each n-gram appears
- Stored as a dictionary: `{ ngram: frequency }`

---

### Probability Calculation

Calculates conditional probability of each bigram:

\[
P(w_2 \mid w_1) = \frac{\text{count}(w_1, w_2)}{\text{count}(w_1)}
\]

Example:
```text
P('love' | 'i') = Count('i', 'love') / Count('i')
```

---

###  Next-Word Prediction

- You input a word (e.g., `'want'`)
- The model returns the most likely next words using **bigram probabilities**

---

## Example Output

```text
Enter a sentence: I love natural language processing.
Unigrams: [('i',), ('love',), ('natural',), ('language',), ('processing',), ('.',)]
Bigrams: [('i', 'love'), ('love', 'natural'), ('natural', 'language'), ('language', 'processing'), ('processing', '.')]
Bigram Probabilities:
('i', 'love'): 1.0000
('love', 'natural'): 1.0000
('natural', 'language'): 1.0000
...

Enter a word to predict the next word: love
Predicted next words for 'love': ['natural']
```

---

##  Usage (main.py)

```python
from ngram_model import NGramModel

text = input("Enter a sentence: ")
model = NGramModel(text)

model.show_ngrams()
model.show_bigram_probabilities()

word = input("Enter a word to predict the next word: ")
print(model.predict_next_word(word))
```
