from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import IngredientManipulations

import numpy as np
import pandas as pd

# Create variables that include the training and the test data
#trainRecipes = pd.read_json("train.json")
testRecipes = pd.read_json("train.json")

# extract ingredients for each recipe of the json file for both training and test data
#trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
#testRecipes['ingredients_string'] = [' '.join(i).strip() for i in testRecipes['ingredients']]
testRecipes['ingredients_string'] = [i for i in testRecipes['ingredients']]

# convert ingredients of recipes into a panda list containing the ingredients specific a recipe
#ingredientsTraining = trainRecipes['ingredients_string']



ingredientsTest = list(testRecipes['ingredients_string'])

#print ingredientsTest[0]

for i in range(len(ingredientsTest)):
    ingredientsTest[i] = IngredientManipulations.normalizeIngredients(ingredientsTest[i])

#print ingredientsTest[0]

testRecipes['ingredients_string'] = [' '.join(i).strip() for i in ingredientsTest]
ingredientsTest = testRecipes['ingredients_string']


#ingredientsTest = pd.Series.from_csv('ingredientsTest.csv', encoding='utf-8')
print ingredientsTest

ingredientsTest.to_csv('ingredientsTrain.csv', encoding='utf-8')