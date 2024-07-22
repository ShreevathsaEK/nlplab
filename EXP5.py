from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


documents = [
    ("fun, couple, love, love", "comedy"),
    ("fast, furious, shoot", "action"),
    ("couple, fly, fast, fun, fun", "comedy"),
    ("furious, shoot, shoot, fun", "action"),
    ("fly, fast, shoot, love", "action")
]

D="fast, couple, shoot, fly"

texts, labels =zip(*documents)
model=make_pipeline(CountVectorizer(tokenizer=lambda x:x.split(', ')),MultinomialNB())
model.fit(texts,labels)

pc=model.predict([D])[0]
pcp=model.predict_proba([D])[0]

print(pc)
print(pcp)