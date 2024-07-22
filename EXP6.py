import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean,cityblock
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
]

query = input("Enter a query sentence: ")

vec=CountVectorizer(stop_words="english")
X=vec.fit_transform(documents+[query]).toarray()
docv,qv=X[:-1],X[-1]

euclidean_distances = [euclidean(doc, qv) for doc in docv]
manhattan_distances = [cityblock(doc, qv) for doc in docv]

cosine_similarities = cosine_similarity(docv, qv.reshape(1, -1)).flatten()

top_2_euclidean = np.argsort(euclidean_distances)[:2] + 1
top_2_manhattan = np.argsort(manhattan_distances)[:2] + 1
top_2_cosine = np.argsort(-cosine_similarities)[:2] + 1

print("Euclidean Distance:", euclidean_distances,"\nTop 2 documents", top_2_euclidean)
print("Manhattan Distance:", manhattan_distances, "\nTop 2 documents",top_2_manhattan)
print("Cosine Similarity:", cosine_similarities,"\nTop 2 documents",top_2_cosine )