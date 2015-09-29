from readFile import *
import nltk
from nltk.metrics.distance import edit_distance

def extractIngredientsFromRecipe(data, recipeNumber):#Extracts the ingredients from a recipe into a list
	ingredients = (data[::][recipeNumber]['ingredients'][x] for x in range (0, len(data[::][recipeNumber]['ingredients'])))
	return list(ingredients)

def extractCuisineFromRecipe(data, recipeNumber):#Extracts the ingredients from a recipe into a list
	cuisine = (data[recipeNumber]['cuisine'])
	return (cuisine)

def normalizeIngredientsOld(ingredients):#Normalizes the ingredients in a given list
	#data structures to hold ingredients with one or multiple tokens respectively
	oneToken = []
	moreTokens = []

	#iterating over every ingredient in the recipe
	for ingredient in ingredients:
		#check if the ingredient only has one token; if so, add to "one token" list
		if ingredient == ingredient.split(" ")[0]:
			oneToken.append(ingredient)
		#else the ingredient has more than one token and may need to be normalized
		else:
			moreTokens.append(ingredient)
		
	#Since they need no normalization, all single token ingredients are added to the normalized Ingredients list
	normalizedIngredients = oneToken
			
	#all multiple token ingredients are split into their respective tokens
	for ingredient in moreTokens:
		normalizedIngredient = []
		ingredientTokenList = ingredient.split(" ")
	
		#Those tokens are discarded if they look like an adjective or irrelevant addition; else they are kept 
		for token in ingredientTokenList:
			if token.endswith("ed"): pass
			elif token.endswith("ing"): pass
			elif token.endswith("boneless"): pass
			elif token.endswith("skinless"): pass
			else : normalizedIngredient.append(token)
	
		#the list is converted back to a String
		normalizedIngredientString = normalizedIngredient[0]
		del(normalizedIngredient[0])
		for token in normalizedIngredient:
			normalizedIngredientString = normalizedIngredientString + " " + token
			
		#The normalized String is added back to the normalized Ingredient list		
		normalizedIngredients.append(normalizedIngredientString)

	return normalizedIngredients


#Testing ground
#data = readTrainingData()
#ingredients = extractIngredientsFromRecipe(data, 549)
#normal = normalizeIngredients(ingredients)
#print normal

#print edit_distance("oil", "cooking oil")

def normalizeIngredients(ingredients):#normalizes the ingredients in a given list using nltk
		
	normalizedIngredients=[]
	
	for ingredient in ingredients:
		normalizedIngredients.append(cleanIngredient(ingredient))
		
	return normalizedIngredients
	
def cleanIngredient(ingredient):#cleans a given ingredient from unneeded parts using nltk
	
	#data structure to hold the cleaned tokens
	cleaned_tokens = []
	
	#tokenize the ingredient
	tokens = nltk.word_tokenize(ingredient)
	
	#tag the ingredient
	tagged_tokens = nltk.pos_tag(tokens)
	
	#iterate the tokens and remove unneeded words
	for i in range(0,len(tagged_tokens)):
		if ((tagged_tokens[i][1])!='JJ' and (tagged_tokens[i][1])!='VBD' and (tagged_tokens[i][1])!='VBG'): cleaned_tokens.append(tagged_tokens[i][0])
	
	#check if any words made it through; if not, just use the original tokens
	if not cleaned_tokens:
		for i in range(0,len(tagged_tokens)): cleaned_tokens.append(tagged_tokens[i][0])
	
	#create a new string to store the cleaned ingredient
	cleaned_ingredient = ""
	
	#add all cleaned tokens to the string
	for token in cleaned_tokens:
		cleaned_ingredient += token
		cleaned_ingredient += '+'
		
	#return the string without the ending whitespace
	return cleaned_ingredient[:-1]

#data = readTrainingDataMod()
#9: Garlic
#recipe_number=0
#print extractIngredientsFromRecipe(data, recipe_number)
#print normalizeIngredients(extractIngredientsFromRecipe(data, recipe_number))
#print normalizeIngredientsOld(extractIngredientsFromRecipe(data, 9))

def normalizePandas(pandas_dataframe):#normalizes pandas ingredient list and returns a pandas ingredient dataframe
	df2list = list(pandas_dataframe['ingredients_string'])

	for i in range(len(df2list)):
		df2list[i] = normalizeIngredients(df2list[i])

	result = [' '.join(i).strip() for i in ingredientsTest]
	
	return result