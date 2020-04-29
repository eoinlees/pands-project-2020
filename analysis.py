#Eoin Lees
#initial creation for project 2020

# Import necessary modules to python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("iris.csv")

# Histogram for each variable:
# Combine histograms in subplots to one png. 
sns.set(style="whitegrid")
plt.figure(figsize=(20,10))
# Petal Width
plt.subplot(2,2,1)
x = df.petal_width
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Petal Width Histogram") 
plt.xlabel("Petal Width (cm)") 
plt.ylabel("Count")
# Petal Length
plt.subplot(2,2,2)
x = df.petal_length
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Petal Length Histogram") 
plt.xlabel("Petal Length (cm)") 
plt.ylabel("Count") 
# Sepal Width
plt.subplot(2,2,3)
x = df.sepal_width
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Sepal Width Histogram") 
plt.xlabel("Sepal Width (cm)") 
plt.ylabel("Count")
# Sepal Length
plt.subplot(2,2,4)
x = df.sepal_length
plt.hist(x, bins = 30, color = "dodgerblue") 
plt.title("Sepal length Histogram") 
plt.xlabel("Sepal length (cm)") 
plt.ylabel("Count") 
# Save plot to .png
plt.savefig("subplothistograms.png")
plt.clf()


#Box plot of variables
# https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40
sns.set(style="ticks") 
plt.figure(figsize=(20,10))
plt.subplot(2,2,1)
sns.boxplot(x='species',y='sepal_length',data=df)
plt.subplot(2,2,2)
sns.boxplot(x='species',y='sepal_width',data=df)
plt.subplot(2,2,3)
sns.boxplot(x='species',y='petal_length',data=df)
plt.subplot(2,2,4)
sns.boxplot(x='species',y='petal_width',data=df)
plt.savefig("boxplot.png")
plt.clf()

#Violin plot of variables
# Read info from this : https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e
sns.set(style="whitegrid")
plt.figure(figsize=(20,10))
plt.subplot(2,2,1)
sns.violinplot(x='species',y='sepal_length',data=df)
plt.subplot(2,2,2)
sns.violinplot(x='species',y='sepal_width',data=df)
plt.subplot(2,2,3)
sns.violinplot(x='species',y='petal_length',data=df)
plt.subplot(2,2,4)
sns.violinplot(x='species',y='petal_width',data=df)
plt.savefig("violinplot.png")
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

# Scatter plots combined side by side with species hue added using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
sns.scatterplot(df['petal_length'], df['petal_width'],hue=df['species'])
plt.title("Petal length vs. Petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.subplot(1,2,2)
sns.scatterplot(df['sepal_length'], df['sepal_width'],hue=df['species'])
plt.title("Sepal length vs. Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("scatterplot_species.png")
plt.clf()

# Clear all plots to speed up program
plt.close('all')

# use seaborn module to plot matrix of plots
sns.set_style("whitegrid")
sns.pairplot(df, hue="species")
plt.savefig("iris_pairplot")
plt.clf()


# Describe statistical summary 


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

# Clear all plots to speed up program
plt.close('all')

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
