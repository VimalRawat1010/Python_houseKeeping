#!/usr/bin/python
import math
import random
import re
from openpyxl import load_workbook
import numpy as np
import csv
import pandas as pd




# The panda Series Data Structure

animal =['Tiger', 'Bear', 'Moose'] 
pd.Series(animal)

number = [1,2,3]
pd.Series(number)
 
np.nan ==None


sports = {'Archery': 'Bhutan',
            'Golf':'Scotland',
            'Sumo': 'Japan',
            'Taekwondo': 'South Korea'}

s =pd.Series(sports)

s.index


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s.index


sports = {'Archery': 'Bhutan',
            'Golf':'Scotland',
            'Sumo': 'Japan',
            'Taekwondo': 'South Korea'}

s =pd.Series(sports)


# Querying a Series


# Quesry by index
s.iloc[0]

# Quesry by key
s.loc['Golf']

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s[0]


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# The DataFrame Data Structure


