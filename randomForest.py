from itertools import chain

import nltk
from pandas import Series, DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import sklearn.metrics

import matplotlib.pylab as plt
import numpy as np
import pandas as pd

# is most likely to get programmed
# make training files
trainRecipes = pd.read_json("train.json")
trainRecipes['ingredients_string'] = [' '.join(z).strip() for z in trainRecipes['ingredients']]

# make test files
testRecipes = pd.read_json("test.json")
testRecipes['ingredients_string'] = [' '.join(z).strip() for z in testRecipes['ingredients']]

# create a copy of trainRecipes and only filter out the ingredients
copyOfIngredients_Training = trainRecipes['ingredients_string']
copyOfIngredients_Test = testRecipes['ingredients_string']

print copyOfIngredients_Training[1]