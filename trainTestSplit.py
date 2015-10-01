"""
Method is used to test various classifiers
"""

from skimage.feature.tests.test_register_translation import test_size_one_dimension_input
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.forest import ExtraTreesClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

import numpy as np
import pandas as pd
import readFile as rf
import sklearn.cross_validation as cv
import sklearn.cross_validation as cv


def testClassifiers(predTraining, predTesting, cuisinesTraining, cuisinesTesting, duration=1, classifier='s'):
    if(classifier == 's'):
        sumSVM = []
        for i in range(0,duration):
            linSVM = SVC(kernel='linear')
            try:
                linSVM.fit(predTraining, cuisinesTraining)
            except ValueError:
                print("Data could not be fitted. Please check your data files. Method aborted")
            sumSVM.append(linSVM.score(predTesting, cuisinesTesting))
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

predTraining, predTesting, cuisinesTraining, cuisinesTesting = rf.processDocuments(split = True)
print(testClassifiers(predTraining, predTesting, cuisinesTraining, cuisinesTesting))