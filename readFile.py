#imports
import json
from pprint import pprint

def readTrainingData():
    #open json files in data
    with open('train.json') as data_file:
        data = json.load(data_file)
    return data

def readTrainingDataMod():
    #open json files in data
    with open('train_mod.json') as data_file:
        data = json.load(data_file)
    return data

def extractUniqueCuisines(data):
    #read all cuisines into a set
    uniqueCuisines = {data[::][i]['cuisine'] for i in range(0,len(data))}
    return uniqueCuisines

def extractAllIngredients(data):
    ingredients = (data[::][i]['ingredients'][j] for i in range(0, len(data)) for j in range(0, len(data[::][i]['ingredients'])))
    ingredients = list(ingredients)
    return ingredients

def extractAllCuisines(data):
    cuisines = (data[::][i]['cuisine'][0] for i in range(0, len(data)))
    cuisines = list(cuisines)
    return cuisines




#print last ingredient of first recipe
#pprint(data[0]['ingredients'][len(data[0]['ingredients'])-1])

#data = readTrainingData()
#uniqueCuisines = extractUniqueCuisines(data)
#ingredients = (data[::][i]['ingredients'][j] for i in range(0, len(data)-1) for j in range(0, len(data[::][i]['ingredients'])))
#ingredients = list(ingredients)