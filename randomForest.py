import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import readFile as rf

import numpy as np
import pandas as pd
import sklearn.cross_validation as cv


# Create variables that include the training and the test data
trainRecipes, testRecipes = rf.readDocuments()

# extract ingredients for each recipe of the json file for both training and test data
trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
testRecipes['ingredients_string'] = [' '.join(i).strip() for i in testRecipes['ingredients']]

# convert ingredients of recipes into a panda list containing the ingredients specific a recipe
ingredientsTraining = trainRecipes['ingredients_string']
ingredientsTest = testRecipes['ingredients_string']

# initialize a Tfidf Vectorizer to determine the tf and idf
# term frequency and inverse document frequency
vectorTraining = TfidfVectorizer(stop_words='english')

# train the vectorizer on the training ingredients to determine most common ingredients
vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)

# evaluate important ingredients from the test data
vectorizedIngredientsTest = vectorTraining.transform(ingredientsTest)

# Make a copy of the different vectorized ingredients
predictors_Test = vectorizedIngredientsTest
predictors_Training = vectorizedIngredients

# contains the cuisine for each recipe
cuisine = trainRecipes['cuisine']

# initialize a SVM 
linSVM = SVC(kernel = 'linear', C=1)

# fit the svm to the data
linSVM.fit(predictors_Training, cuisine)

# predict the data
predictions = linSVM.predict(predictors_Test)

# store the predictions into a DataFrame
testRecipes['cuisine'] = predictions

subID = testRecipes['id']
subCuisine = testRecipes['cuisine']

# write results to csv file to be able to submit it to kaggle
testRecipes[['id','cuisine']].to_csv('results.csv', index = False)