import pandas as pd
import numpy as np
import sklearn.cross_validation as cv
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import readFile as rf
import sklearn.cross_validation as cv

'''
Method is used to test various classifiers
'''
def testClassifiers(predTraining, predTesting, cuisinesTraining, cuisinesTesting, duration=10, classifier='s'):
    print("Entering method")
    if(classifier == 's'):
        print("initialize SVM")
        sumSVM = []
        for i in range(0,duration):
            print(i)
            linSVM = SVC(kernel='linear')
            print("SVM created")
            linSVM.fit(predTraining, cuisinesTraining)
            print("data fitted")
            sumSVM.append(linSVM.score(predTesting, cuisinesTesting))
            print("score calculated")
        print("done")
        return np.mean(sumSVM)
    elif(classifier=='e'):
        sumET = []
        for i in range(1,duration):
            etTraining = ExtraTreesClassifier(n_estimators=10, max_features='auto', criterion='gini', n_jobs=-1, warm_start=False)
            etTraining.fit(predTraining, cuisinesTraining)
            sumET.append(etTraining.score(predTesting, cuisinesTesting))
        return np.mean(sumET)
    elif(classifier=='r'):
        sumRF = []
        for i in range(0,duration):
            rfcTraining = RandomForestClassifier(n_estimators=10, max_features='auto', criterion='gini', n_jobs=-1, warm_start=False)
            rfcTraining.fit(predTraining, cuisinesTraining)
            sumRF.append(rfcTraining.score(predTesting, cuisinesTesting))
        return np.mean(sumRF)
    else:
        print("A Classifier has not been given. Please name a Classifier using the characters s(SVM), e(ExtraTrees) and r(RandomForest). By default it is s.")

def main():
    training, testing, cuisinesTraining, cuisinesTesting = rf.readDocuments(splitData=True, splitRatio=0.33)
    predictors_Training, predictors_Test, cuisine = rf.processDocuments(splitData=True, splitRatio=0.33)
    print(testClassifiers(predictors_Training, predictors_Test, cuisinesTraining, cuisinesTesting, 2))
main()
    
