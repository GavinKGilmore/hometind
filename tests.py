# This is a test file for the backend logic of hometind
"""
Although the backend of this application will not be written in python many of the tests and prototyping will be done in a python
environment in order to validate some of the larger ideas.
"""

import pandas as pd
from pandasql import sqldf

drinks = pd.read_csv('./all_drinks.csv')

print(drinks)

print(sqldf("SELECT strDrink FROM drinks WHERE strCategory='Cocktail'"))

# We will need to somehow iterate through all ingredients in order to sort by ingredient
