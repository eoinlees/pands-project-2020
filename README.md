# **Galway Mayo Institute of Technology**
### **Programming and Scripting**
### **Final Project - 2020**
### **Eoin Lees**


# 
# 

## Introduction

This analysis is the final project for the Program and Scripting module in GMIT's H.Dip in data analytics in april 2020. 
The brief was to research the well known Fisher's Iris data set and to write documentation and code in Python to investigate it. 

The tasks were laid out as follows:

1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called `analysis.py` that:
* outputs a summary of each variable to a single text file,
* saves a histogram of each variable to png files, and
* outputs a scatter plot of each pair of variables.

The following is the results of this analysis and explains how the code written  in Python works. 

## Running the program

In order to run this analysis Python needs to be installed on your system. The program is run using the `analysis.py` program in command prompt. The program needs `ìris.csv` to be in the same repository to run correctly.
It will generate all of the plots shows in this readme along with the `iris_summaries.txt` document.  

## Background

Info reguarding the iris Data set and its history

Who was Ronald Fisher

Who was Edgar Anderson

What did He measure and How

![Iris Types](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Types of Iris in data")

Types of Iris [3] 

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://en.wikipedia.org/wiki/Ronald_Fisher
https://en.wikipedia.org/wiki/Edgar_Anderson

## Data Format 

The csv data was obtained from the following git hub reposityry in csv format [1]. It was complied from the origional data set published by the UCI machine learning repository [2]. This repository is a collection of databases used by teh machine learning community for the empirical analysis of machine learning algorithms. It was created by a number of graduates of the University of California Irvine in 1987.  
 
The following table shows a sample of the data as it is presented in the csv file. 


|number|sepal_length| sepal_width| petal_length | petal_width |    species|
|:----:|:----:|:----:|:----:|:----:|:----:|
|0             |5.1|          3.5|           1.4|          0.2|setosa|
|1             |4.9|          3.0|           1.4|          0.2|     setosa|
|2             |4.7|          3.2|           1.3|          0.2|     setosa|
|3             |4.6|          3.1|           1.5|          0.2|     setosa|
|4             |5.0|          3.6|           1.4|          0.2|     setosa|
|..            |...|          ...|           ...|          ...|        ...|
|145           |6.7|          3.0|           5.2|          2.3|  virginica|
|146           |6.3|          2.5|           5.0|          1.9|  virginica|
|147           |6.5|          3.0|           5.2|          2.0|  virginica|
|148           |6.2|          3.4|           5.4|          2.3|  virginica|
|149           |5.9|          3.0|           5.1|          1.8|  virginica|

This table was then imported into python using the pandas module as described below. 

#### Modules and data imported

The initial set up of teh program required importing modules and the data to python as shows in teh code below: 

````
# Import necessary modules to python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("iris.csv")
````
The modules imported have the following functions:
* numpy - allows fast and efficient operations on arrays of data.  [4]
* pandas - provides high performance data structures and data analysis tools. [5]
* matplotlib - a comprehensive library for creating static, animated and interactive visualisations in Python. [6] 
* seaborn -  a data visualisation libary based on matplotlib. provides highlevel interface for drawing attractive and informative statistical graphics. [7] 


# Main Body

The following is a quick analysis of the iris data set. It's purpose is to demonstrate a a wide array of python techniques for data analysis along with providing a method for classifying the species in the data using vidual means. 



### Length vs width scatter plots

To begin with a simple length vs. width scatter plot for both the petal and sepal measurments was plotted. 
These plots show all of the data with no differentiation of species. Its gives a good idea of how similar the data is across all species of iris studied. 

#### Petal Length Vs. Petal Width

In order to produce the petal elngth vs petal width plot the following code was used:
````
plt.scatter(df['petal_length'], df['petal_width'])
plt.title("Petal length vs. Petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.savefig("all_petal_length_vs_petal_width.png")
plt.clf()
````
It uses the scatter function of matplotlib to plot the petal length vs with imported from the data using teh df function. It is then appropiatly labelled and saved to the curent repositry. The `plt.clf()` command is then used to ensure the plot is clear for the next command. 

![petal length vs width](https://github.com/eoinlees/pands-project-2020/blob/master/all_petal_length_vs_petal_width.png "petal length vs width")

#### Sepal Length Vs. Sepal Width

The same method was used to produce the sepal length vs sepal width scatter plot. 
````
plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title("Sepal length vs. Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("all_sepal_length_vs_sepal_width.png")
plt.clf()
````
![sepal length vs width](https://github.com/eoinlees/pands-project-2020/blob/master/all_sepal_length_vs_sepal_width.png "sepal length vs width")

From an initial analysis of this data it shows how the points are clustered and without further investigation no real conclusions can be drawn. 

The addition of the species to both of these scatterplots reveals a lot more about the data as shown below. 

The code used to acheive this is as follows:
````
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
````
Instead of plotting the graphs with matplotlib, seaborn is used. This allows further customisation and the introduction of the hue to highlight the species. 

It becomes immediatly apparent from this that a classification of at least one of the species can be made. 

### Data summary

The data provided is summarised in the `irissummaries.txt` document. It give a list of the variables, and breaks down each of their details under the headings: 
* count - the total number of data 
* mean - the mean value
* std - the standard deviation
* min - the minimum value
* 25%
* 50%
* 75%
* max - the maximum value

This data can be visualised using the box plot and the violin plot. 

#### Box Plot

The box plot was chosen as it gives a good visual representation of the data. The top and bottom represent the 75th and 25th percentiles. The median value is shown with the horizontal line and the rest is shown with the straight line known as the whiskers. Using this method we can easily see the outliers shown as the points on each graph. 

the following code was used to produce the shown boxplot:
````
sns.set(style="ticks") 
plt.figure(figsize=(12,10))
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
````
It draws heavily on the seaborn module in order to produce the plot. Matplotlib is used to arrange the plots using the `subplot` command. 

![Box plot](https://github.com/eoinlees/pands-project-2020/blob/master/boxplot.png "Box plot")

#### Violin Plot

The violin plot performs a similar role as the box plot. It differs from the boxplot by showing the kernal density estimation of the underlying distribution.

The kernal density estimation..... 

````
sns.set(style="whitegrid")
plt.figure(figsize=(12,10))
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
````
![Violin Plot](https://github.com/eoinlees/pands-project-2020/blob/master/violinplot.png "Violin Plot")

### Pairplot - Overview

The seaborn module allows for the production of a pairplot which compares all the variables against each other on one series of plots.
This feature is preformed with the straightforward code shown below: 
````
sns.set_style("whitegrid")
sns.pairplot(df, hue="species")
plt.savefig("iris_pairplot")
plt.clf()
````
It is an extremely useful tool in data analytics. It provides an immediate overview of the data being worked with and allows us to identify any possible relationships at a high level. 

![Pair Plot](https://github.com/eoinlees/pands-project-2020/blob/master/iris_pairplot.png "Pair Plot")

The pair plot alows us to identiy the relationship in petal length.......



## Detailed Analysis

Using the information from above we can look in more detail at the data provided

#### Petal Length

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/petal_length_hist.png "Logo Title Text 1")

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/petal_length_species.png "Logo Title Text 1")

#### Petal Width

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/petal_width_hist.png "Logo Title Text 1")

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/petal_width_species.png "Logo Title Text 1")

#### Sepal Length

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_length_hist.png "Logo Title Text 1")

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_length_species.png "Logo Title Text 1")

#### Sepal Width

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_width_hist.png "Logo Title Text 1")

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_width_species.png "Logo Title Text 1")




# Conclusions

Petal width can be used to classify one vs other vs otehr etc. 

### Classifications


***


# Sources

[1] https://gist.github.com/curran/a08a1080b88344b0c8a7

[2] https://archive.ics.uci.edu/ml/datasets/Iris

[3] https://www.datacamp.com/community/tutorials/machine-learning-in-r

[4] https://numpy.org/

[5] https://pandas.pydata.org/docs/user_guide/index.html

[6] https://seaborn.pydata.org/tutorial/axis_grids.html

[7] https://matplotlib.org/

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://github.com/RitRa/Project2018-iris

https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e

https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

https://www.youtube.com/watch?v=5dLG3JDk2VU

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet