import pandas as pd
import numpy as np
import json
import nltk
import re
import csv
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from IPython import get_ipython
%matplotlib inline
#get_ipython().run_line_magic('matplotlib', 'inline') 

# So you have to explicitely import the module into the namespace
pd.set_option('display.max_colwidth', 300)
#since the data file is tab separated .tsv, we read it using \t as separator 
meta = pd.read_csv("/Users/srijon/Projects/CS129 Final Project/MovieSummaries/movie.metadata.tsv", sep = '\t', header = None)
meta.head()

#name first col --> id, second col -> mov_name, eight col-> genre 
meta.columns = ["id", 1,"name",3,4,5,6,7,"genre"]

#read plot summary from textfile in dataset -- row has id and plot -- read by line
plots = []

with open("/Users/srijon/Projects/CS129 Final Project/MovieSummaries/plot_summaries.txt", 'r') as f:
       reader = csv.reader(f, dialect='excel-tab') 
       for row in tqdm(reader):
            plots.append(row)

#split into two lists -- ids and plots 
movie_id = []
plot = []

#obtain these from lines read 
for i in tqdm(plots):
    movie_id.append(i[0])
    plot.append(i[0])
#create data frame 
movies = pd.DataFrame({'movie_id': movie_id, 'plot': plot})
movies.head()
 