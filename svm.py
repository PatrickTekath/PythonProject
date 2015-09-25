from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

# Create variables that include the training and the test data
trainRecipes = pd.read_json("train.json")
testRecipes = pd.read_json("test.json")

trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
testRecipes['ingredients_string'] = [' '.join(i).strip() for i in testRecipes['ingredients']]

ingredientsTraining = trainRecipes['ingredients']
ingredientsTest = testRecipes['ingredients']

vectorizertr = TfidfVectorizer(stop_words='english')
vectorizedIngredients = vectorizertr.fit_transform(trainRecipes)

predictors_Training = vectorizedIngredients

cuisine = trainRecipes['cuisine']

cuisineArray = np.array(pd.Series.get_values(cuisine))

forestCLS = RandomForestClassifier(n_estimators=15)

'''
xtraining = np.random.standard_normal((100,2))
xtest = np.random.standard_normal((100000,2))

ytraining = np.empty(100)
ytest = np.empty(100000)

for i in range(0,100,1):
    ytraining[i] = np.sign(xtraining[i][0])

for i in range(0,100000,1):
    ytest[i] = np.sign(xtest[i][0])

print type(xtraining)
print type(ytraining) 

forestCLS = RandomForestClassifier(n_estimators= 15)

forestCLS.fit(xtraining,ytraining)
forestCLS.predict(xtest)
#print(forestCLS.score(xtest,ytest))
'''