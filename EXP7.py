import nltk
from nltk.corpus import wordnet # nltk.download('omw-1.4') or ('wordnet)
def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()

    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())

    return synonyms, antonyms

word = input("Enter a word: ")
synonyms, antonyms = get_synonyms_antonyms(word)
print(f"Synonyms of {word}: {synonyms}")
print(f"Antonyms of {word}: {antonyms}")