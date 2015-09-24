#imports
import json
from pprint import pprint

#open json files in data
with open('train.json') as data_file:
    data = json.load(data_file)

#print last ingredient of first recipe
#pprint(data[0]['ingredients'][len(data[0]['ingredients'])-1])

uniqueCuisine = set(cuisine for cuisine in data[::]['cuisine'])
