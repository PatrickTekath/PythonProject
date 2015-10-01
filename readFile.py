#imports
import pandas as pd
from pprint import pprint

def readDocuments(pathTraining="train.json", pathTesting="test.json"):
    # read documents using pandas
    trainRecipes = pd.read_json(pathTraining)
    testRecipes  = pd.read_json(pathTesting)
    return trainRecipes, testRecipes

def processDocuments():
    trainRecipes, testRecipes = readDocuments()
    
    # extract ingredients for each recipe of the json file for both training and test data
    trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
    testRecipes ['ingredients_string'] = [' '.join(i).strip() for i in testRecipes ['ingredients']]
    
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