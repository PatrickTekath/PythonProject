from readFile import *
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import json
from sympy.ntheory import factor_
from statsmodels.sandbox.formula import Factor

#Wird am wahrscheinlichsten weitergefuehrt
with open('train.json') as data_file:
    data = json.load(data_file)

#print ingredients from recipe 0
stringOfIngredients = ''
ingredients = data[1]['ingredients']
for ingredient in ingredients:
    stringOfIngredients += ingredient + ','
print stringOfIngredients