#Eoin Lees
#initial creation for project 2020

# Import necessary modules to python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("iris.csv")


# Histogram for each variable : https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

# Sepal Length Histogram
plt.figure(figsize = (20, 10)) 
x = df.sepal_length
  
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Sepal length Histogram") 
plt.xlabel("Sepal length (cm)") 
plt.ylabel("Count") 
  
plt.savefig("sepal_length_hist.png")
plt.clf()

# Sepal Width Histogram
plt.figure(figsize = (20, 10)) 
x = df.sepal_width
  
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Sepal Width Histogram") 
plt.xlabel("Sepal Width (cm)") 
plt.ylabel("Count") 
  
plt.savefig("sepal_width_hist.png")
plt.clf()

# Petal Length Histogram
plt.figure(figsize = (20, 10)) 
x = df.petal_length
  
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Petal Length Histogram") 
plt.xlabel("Petal Length (cm)") 
plt.ylabel("Count") 
  
plt.savefig("petal_length_hist.png")
plt.clf()

# Petal Width Histogram
plt.figure(figsize = (20, 10)) 
x = df.petal_width
  
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Petal Width Histogram") 
plt.xlabel("Petal Width (cm)") 
plt.ylabel("Count") 
  
plt.savefig("petal_width_hist.png")
plt.clf()



# Scatter plot sepal length vs width
plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title("Sepal length vs. Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("all_sepal_length_vs_sepal_width.png")
plt.clf()

# Scatter plot petal length vs width
plt.scatter(df['petal_length'], df['petal_width'])
plt.title("Petal length vs. Petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.savefig("all_petal_length_vs_petal_width.png")
plt.clf()

# use seaborn module to plot matrix of plots
sns.set_style("whitegrid")
sns.pairplot(df, hue="species")
plt.savefig("iris_pairplot")
plt.clf()



# Edit this one to work with savefig
sns.FacetGrid(df, hue="species", height=5).map(plt.scatter,"sepal_length","sepal_width").add_legend()
#plt.show()
plt.clf()

sns.FacetGrid(df, hue="species", height=5).map(plt.scatter,"petal_length","petal_width").add_legend()
#plt.show()

# Describe statistical summary - This version not needed
#print(df.describe())

#Display in neater orientation : https://github.com/RitRa/Project2018-iris

file = open("iris_summaries.txt", "w") 

summary = df.describe()
summary = summary.transpose()
summary.head()

file.write("The Following is the complete data set:")
file.write("\n")
file.write(str(df))
file.write("\n")
file.write(str(summary.head())) 
file.write("\n")
file.write(str(df.groupby('species').size()))
file.write("\n")
file.write("\n")

file.close() 


# Import andrews curves to visualise 
from pandas.plotting import andrews_curves
plt.figure()
andrews_curves(df, 'species')
#plt.show()


#Histograms allow us to isolate setosa species in the data for petal length and width
# source : https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

plt.figure(figsize = (20, 10)) 
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"petal_length").add_legend()
plt.savefig("petal_length_species.png")
plt.clf()

plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"petal_width").add_legend()
plt.savefig("petal_width_species.png")
plt.clf()

plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"sepal_length").add_legend()
plt.savefig("sepal_length_species.png")
plt.clf()

plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"sepal_width").add_legend()
plt.savefig("sepal_width_species.png")
plt.clf()




print("Analysis Complete")
  
#plt.hist(x, bins = 30, color = "dodgerblue") 