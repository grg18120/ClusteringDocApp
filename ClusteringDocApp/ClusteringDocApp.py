from sklearn.feature_extraction.text import TfidfVectorizer

dataset = [
    "The car is driven on the road",
    "The truck is driven on the highway"
    ]

#
vectorizer = TfidfVectorizer()

# Vectors
docVectors = vectorizer.fit_transform(dataset)
print(type(docVectors))
print(docVectors.shape)

featureNames = vectorizer.get_feature_names_out()
print(featureNames)

dense = docVectors.todense()
denseList = dense.tolist()
print(denseList)

parametres = vectorizer.get_params(deep=True)
print(parametres)


