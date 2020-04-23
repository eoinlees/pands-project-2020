#Eoin Lees
#initial creation for project 2020

# Import necessary modules to python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("iris.csv")

# Define Variables

sepL = df.sepal_length
sepW = df.sepal_width
petL = df.petal_length
petW = df.petal_width
species = df.species

#Test variables
#print(sepL)
#print(sepW)
#print(petL)
#print(petW)
#print(species)

# Scatter plot sepal length vs width
#plt.scatter(df['sepal_length'], df['sepal_width'])
#plt.title("Sepal length vs. Sepal width")
#plt.xlabel("Sepal Length")
#plt.ylabel("Sepal Width")
#plt.show()

# Scatter plot petal length vs width
#plt.scatter(df['petal_length'], df['petal_width'])
#plt.title("Petal length vs. Petal width")
#plt.xlabel("Petal Length")
#plt.ylabel("Petal Width")
#plt.show()

# use seaborn module to plot matrix of plots
#sns.pairplot(df, hue="species")
#plt.show()

sns.FacetGrid(df, hue="species", height=5).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()

sns.FacetGrid(df, hue="species", height=5).map(plt.scatter,"petal_length","petal_width").add_legend()
plt.show()

# Describe statistical summary
print(df.describe())

# 
print(df.groupby('species').size())

# Import andrews curves to visualise 
from pandas.plotting import andrews_curves
plt.figure()
andrews_curves(df, 'species')
plt.show()
