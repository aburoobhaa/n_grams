from ngram import NGramModel

# Input text
text = input("Enter a sentence: ")
model = NGramModel(text)

# Ngrams
model.show_ngrams()

# Probabilities
model.show_bigram_probabilities()

# Prediction 
word = input("\nEnter a word to predict the next word: ").strip().lower()
predictions = model.predict_next_word(word)
print(f"Predicted next words for '{word}': {predictions}")
