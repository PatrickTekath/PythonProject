#imports
import pandas as pd
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.cross_validation as cv

'''
This method is used to read the json documents containing the training and test data
'''
def readDocuments(pathTraining="train_mod.json", pathTesting="test_mod.json", splitData=False, splitRatio=0.25):
    '''read documents using pandas'''
    if(splitData == True):
        trainRecipes = pd.read_json(pathTraining)
        training, testing = cv.train_test_split(trainRecipes, test_size=splitRatio)
        training = pd.DataFrame(training)
        testing  = pd.DataFrame(testing)
        cuisineTraining = training['cuisine']
        cuisineTesting = testing['cuisine']
        return training, testing, cuisineTraining, cuisineTesting
    else:
        trainRecipes = pd.read_json(pathTraining)
        testRecipes  = pd.read_json(pathTesting)
        return trainRecipes, testRecipes

'''
This procedure uses the training and test data and converts 
'''
def processDocuments(pathTraining="train_mod.json", pathTesting="test_mod.json", splitData=False, splitRatio=0.25):
    trainRecipes, testRecipes, cuisineTraining, cuisineTesting = readDocuments(pathTraining, pathTesting, splitData, splitRatio)
    
    '''extract ingredients for each recipe of the json file for both training and test data'''
    trainRecipes['ingredients_string'] = [' '.join(i).strip() for i in trainRecipes['ingredients']]
    testRecipes ['ingredients_string'] = [' '.join(i).strip() for i in testRecipes ['ingredients']]

    '''convert ingredients of recipes into a panda list containing the ingredients specific a recipe'''
    ingredientsTraining = trainRecipes['ingredients_string']
    ingredientsTest     = testRecipes ['ingredients_string']
    
    '''initialize a Tfidf Vectorizer to determine the tf and idf
    term frequency and inverse document frequency'''
    vectorTraining = TfidfVectorizer(stop_words='english')
    
    '''train the vectorizer on the training ingredients to determine most common ingredients'''
    vectorizedIngredients = vectorTraining.fit_transform(ingredientsTraining)
    
    '''evaluate important ingredients from the test data'''
    vectorizedIngredientsTest = vectorTraining.transform(ingredientsTest)
    
    '''Make a copy of the different vectorized ingredients'''
    predictors_Test = vectorizedIngredientsTest
    predictors_Training = vectorizedIngredients
    
    '''contains the cuisine for each recipe'''
    cuisine = trainRecipes['cuisine']
    return predictors_Training, predictors_Test, cuisine