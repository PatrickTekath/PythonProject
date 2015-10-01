#imports
from pprint import pprint

from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
import sklearn.cross_validation as cv

"""
Method to read the single data file used for splitting the data
"""
def readTrainingDocument(pathTraining="train.json"):
    trainRecipes = pd.read_json(pathTraining)
    return trainRecipes

"""
Method to read the data files
"""
def readDocuments(pathTraining="train_mod.json", pathTesting="test_mod.json"):
    """read documents using pandas"""
    trainRecipes = pd.read_json(pathTraining)
    testRecipes  = pd.read_json(pathTesting)
    return trainRecipes, testRecipes

"""
Function to split the training data into a training and a test set
"""
def splitData(splitRatio):
    trainRecipes = readTrainingDocument('train.json')
    training, testing = cv.train_test_split(trainRecipes, test_size=splitRatio)
    training = pd.DataFrame(training)
    testing = pd.DataFrame(testing)
    return training, testing

"""
This procedure uses the training and test data and converts them into training and test data
to be able to fit Classifiers on it
"""
def processDocuments(split=False, splitRatio=0.25, extTrainingFile='', extTestFile=''):
    trainRecipes = readTrainingDocument("train_mod.json")
    if(split == False):
        if(extTrainingFile):
            ingredientsTraining = pd.Series.from_csv(extTrainingFile, encoding='utf-8')
        else:
            trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
            ingredientsTraining = trainRecipes['ingredients_string']
        if(extTestFile):
            ingredientsTest = pd.Series.from_csv(extTestFile, encoding='utf-8')
        else:
            testRecipes = readTrainingDocument('test_mod.json')
            # extract ingredients for each recipe of the json file for both training and test data
            testRecipes ['ingredients_string'] = [' '.join(i).strip() for i in testRecipes ['ingredients']]
            # convert ingredients of recipes into a panda list containing the ingredients specific a recipe
            ingredientsTest = testRecipes ['ingredients_string']
            
        # initialize a Tfidf Vectorizer to determine the tf and idf
        # term frequency and inverse document frequency
        vectorTraining = TfidfVectorizer(stop_words='english')
        # train the vectorizer on the training ingredients to determine most common ingredients
        vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)
        # evaluate important ingredients from the test data
        vectorizedIngredientsTest = vectorTraining.transform(ingredientsTest)
        # Make a copy of the different vectorized ingredients
        predictors_Training = vectorizedIngredients
        predictors_Test = vectorizedIngredientsTest
        # contains the cuisine for each recipe
        cuisine = trainRecipes['cuisine']
        return testRecipes, cuisine, predictors_Training, predictors_Test

    else:
        trainRecipes = readTrainingDocument("train_mod.json")
        if(extTrainingFile):
            ingredientsTraining = pd.Series.from_csv(extTrainingFile, encoding='utf-8')
            
        
        else:
            training, testing = splitData(splitRatio)
       
            training['ingredients_string'] = [' '.join(i).strip() for i in training['ingredients']]
            testing['ingredients_string'] = [' '.join(i).strip() for i in testing['ingredients']]
        
            ingredientsTraining = training['ingredients_string']
            ingredientsTesting = testing['ingredients_string']
        
            cuisinesTraining = training['cuisine']
            cuisinesTesting = testing['cuisine']
        
        vectorTraining = TfidfVectorizer(stop_words='english')
        vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)
        vectorizedIngredientsTest = vectorTraining.transform(ingredientsTesting)
        
        predTraining = vectorizedIngredients
        predTesting = vectorizedIngredientsTest
       
        return predTraining, predTesting, cuisinesTraining, cuisinesTesting