import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import re
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem import SnowballStemmer ,WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import xgboost as xg
from sklearn.metrics import *

print("All Imports Successfull")
data = pd.read_csv("https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/tweet_emotions.csv")
print("Data Import Successful")

print(data.head)

print(data.describe())
