from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import IngredientManipulations

import numpy as np
import pandas as pd

# Create variables that include the training and the test data
trainRecipes = pd.read_json("train.json")
testRecipes = pd.read_json("test.json")

# extract ingredients for each recipe of the json file for both training and test data
#trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
#testRecipes['ingredients_string'] = [' '.join(i).strip() for i in testRecipes['ingredients']]

# convert ingredients of recipes into a panda list containing the ingredients specific a recipe
#ingredientsTraining = trainRecipes['ingredients_string']
#ingredientsTraining = IngredientManipulations.normalizePandas(trainRecipes)
#ingredientsTest = testRecipes['ingredients_string']
#ingredientsTest = IngredientManipulations.normalizePandas(testRecipes)

#Load normalized ingredients from csv to save time
ingredientsTest = pd.Series.from_csv('ingredientsTest.csv', encoding='utf-8')
ingredientsTraining = pd.Series.from_csv('ingredientsTrain.csv', encoding='utf-8')

# initialize a Tfidf Vectorizer to determine the tf and idf
# term frequency and inverse document frequency
vectorTraining = TfidfVectorizer(stop_words='english')

# train the vectorizer on the training ingredients to determine most common ingredients
vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)
#train the vectorizer on the test ingredients
vectorizedIngredientsTest = vectorTraining.transform(ingredientsTest)

#Make a copy of the different vectorized ingredients
predictors_Test = vectorizedIngredientsTest
predictors_Training = vectorizedIngredients

# contains the cuisine for each recipe
cuisine = trainRecipes['cuisine']

# Initialize a random forest classifier
forestCLS = RandomForestClassifier(n_estimators=1000, n_jobs=-1)

# train the Classifier with the data for the ingredients and the cuisines
forestCLS.fit(predictors_Training,cuisine)

# predict the data
predictions = forestCLS.predict(predictors_Test)

# store the predictions into a DataFrame
testRecipes['cuisine'] = predictions

# print predictions
# print (testRecipes['cuisine'])

# Save predictions to csv file
testRecipes[['id','cuisine']].to_csv('results.csv', index=False)