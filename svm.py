from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
import pandas as pd

# Create variables that include the training and the test data
trainRecipes = pd.read_json("train_mod.json")
testRecipes = pd.read_json("test_mod.json")

# extract ingredients for each recipe of the json file for both training and test data
trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
testRecipes['ingredients_string'] = [' '.join(i).strip() for i in testRecipes['ingredients']]

# convert ingredients of recipes into a panda list containing the ingredients specific a recipe
ingredientsTraining = trainRecipes['ingredients_string']
ingredientsTest = testRecipes['ingredients_string']

# initialize a Tfidf Vectorizer to determine the tf and idf
# term frequency and inverse document frequency
vectorTraining = TfidfVectorizer()
vectorTest = TfidfVectorizer()

# train the vectorizer on the training ingredients to determine most common ingredients
vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)

#train the vectorizer on the test ingredients
# vectorizedIngredientsTest = vectorTest.fit(ingredientsTest)
vectorizedIngredientsTest = vectorTest.transform(ingredientsTest)

# contains the cuisine for each recipe
cuisine = trainRecipes['cuisine']

# Initialize a random forest classifier
forestCLS = RandomForestClassifier(n_estimators=15)

# train the Classifier with the data for the ingredients and the cuisines
forestCLS.fit(vectorizedIngredients,cuisine)

print vectorizedIngredients.shape
print
print vectorizedIngredientsTest.shape

# predict the data
predictions = forestCLS.predict(vectorizedIngredients)

# store the predictions into a DataFrame
trainRecipes['predictions'] = predictions

# print predictions
print (trainRecipes['predictions'])