from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import readFile as rf

import numpy as np
import pandas as pd
import sklearn.cross_validation as cv

def main():
    # Create variables that include the training and the test data
    trainRecipes, testRecipes = rf.readDocuments()
    predictors_Training, predictors_Test, cuisine = rf.processDocuments()
    
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
main()