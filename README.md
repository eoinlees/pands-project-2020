# **Galway Mayo Institute of Technology**
### **Programming and Scripting**
### **Final Project - 2020**
### **Eoin Lees**

## Introduction

This analysis is the final project for the Program and Scripting module in GMIT's H.Dip in Data Analytics in April 2020. 
The brief was to research the well-known Fisher's Iris data set and to write documentation and code in Python to investigate the data set.

The tasks were laid out as follows:

1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called `analysis.py` that:
    * outputs a summary of each variable to a single text file,
    * saves a histogram of each variable to PNG files, and
    * outputs a scatter plot of each pair of variables.

The following information includes the results of this analysis and an explanation of how the Python code works. 

## Running the program

In order to run this analysis, Python needs to be installed on your system. The program is run using the `analysis.py` program in command prompt. The program needs `ìris.csv` to be in the same repository to run correctly.
It will generate all of the plots shows in this README, along with the `iris_summaries.txt` document.  

## Background

The Iris flower data set, also known as Fisher's Iris data set or Anderson's Iris data set is a multivariate data set introduced in 1936 by biologist Ronald Fisher. It is widely used as a beginners data set for data analytics, specifically in machine learning. 

Ronald Fisher was a well-known statistician and geneticist born in London in 1890. His contribution to statistics has him described as "the single most important figure in 20th century statistics" [1]. The data set was first published by the Annals of Eugenics in September 1936 in a report titled "the use of multiple measurments in taxonomic problems." 

In his report, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. 

The data used in his article was collected by Dr. Edgar Anderson, a botanist at the Washington University in St. Louis. The data was collected in its majority from the Gaspé Peninsula in Canada. 

Dr. Anderson measured four secific characteristics of the Iris: petal length, petal width, sepal length and sepal width. He also specified which species of Iris that the measurments came from, either Iris setosa, Iris versicolor or Iris virginica. All of these are shown below. 

![Iris Types](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Types of Iris in data") 
###### Types of Iris [4] 

It is worth noting that while the analytic method used to tell the difference between the species was useful, botanists had a better method to tell the difference based on the morphology of the seeds. 

## Data Format 

The CSV data was obtained from the following GitHub repository in CSV format [2]. It was compiled from the origional data set published by the UCI machine learning repository [3]. This repository is a collection of databases used by the machine learning community for the empirical analysis of machine learning algorithms. It was created by a number of graduates of the University of California Irvine in 1987.  
 
The following table shows a sample of the data as it is presented in the CSV file. 


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

There are five variables in the data:
* sepal_length - measured in centimetres (cm)
* sepal_width  - measured in cm
* petal_length - measured in cm
* petal_width  - measured in cm
* species      - setosa, versicolor or virginica

This table was then imported into Python using the pandas module as described below. 

#### Modules and data imported

The initial setup of the program required importing modules and the data to python as shows in the code below: 

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
* NumPy - allows fast and efficient operations on arrays of data. [5]
* Pandas - provides high performance data structures and data analysis tools. [6]
* Matplotlib - a comprehensive library for creating static, animated and interactive visualisations in Python. [7] 
* Seaborn -  a data visualisation libary based on matplotlib. Seaborn provides a high-level interface for drawing attractive and informative statistical graphics. [8] 

# Analysis of the Iris Data Set

The following includes a quick analysis of the Iris data set. Its purpose is to demonstrate a wide array of Python techniques for data analysis, along with providing a method for classifying the species in the data using visual means. 

### Length vs. width scatter plots

To begin, a simple length vs. width scatter plot for both the petal and sepal measurments was plotted. 
These plots show all of the data with no differentiation of species. Its gives a good idea of how similar the data is across all species of Iris studied. 

#### Petal length vs. petal width

In order to produce the petal length vs. petal width plot, the following code was used:
````
plt.scatter(df['petal_length'], df['petal_width'])
plt.title("Petal length vs. Petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.savefig("all_petal_length_vs_petal_width.png")
plt.clf()
````
It uses the scatter function of Matplotlib to plot the petal length vs. width, which is imported from the data using the df function. It is then appropriately labelled and saved to the curent repository. The `plt.clf()` command is then used to ensure that the plot is clear for the next command. 

![petal length vs width](https://github.com/eoinlees/pands-project-2020/blob/master/all_petal_length_vs_petal_width.png "petal length vs width")

#### Sepal length vs. sepal width

The same method was used to produce the sepal length vs. sepal width scatter plot. 
````
plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title("Sepal length vs. Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("all_sepal_length_vs_sepal_width.png")
plt.clf()
````
![sepal length vs width](https://github.com/eoinlees/pands-project-2020/blob/master/all_sepal_length_vs_sepal_width.png "sepal length vs width")

An initial analysis of this data shows how the points are clustered but without further investigation, no real conclusions can be drawn. 

The addition of the species to both of these scatterplots reveals a lot more about the data as shown below. 

The code used to achieve this is as follows:
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
Instead of plotting the graphs with Matplotlib, seaborn is used. This allows further customisation and the introduction of the hue to highlight the species. 

![length vs width](https://github.com/eoinlees/pands-project-2020/blob/master/scatterplot_species.png "species scatterplot")

It becomes immediately apparent from this that a classification of at least one of the species can be made. 

With both petal length and width, it is easy to pick out the Iris setosa. This can then be classified accordingly. It also shows a correlation in sepal length and width. Generally, if there is a shorter length sepal it will also have a correlating shorter width. 

This correlation can somewhat be seen with the other two species of Iris in the sepal and petal. 

### Data summary

The data provided is summarised in the `irissummaries.txt` document . It give a list of the variables, and breaks down each of their details under the headings: 
* count - the total number of data 
* mean - the mean value
* std - the standard deviation
* min - the minimum value
* 25% - the 25th percentile
* 50% - the 50th percentile
* 75% - the 75th percentilea
* max - the maximum value

This data can be visualised using the box plot and the violin plot. 

#### Box Plot

The box plot was chosen as it gives a good visual representation of the data. The top and bottom represent the 75th and 25th percentiles. The median value is shown with the horizontal line and the rest is shown with the straight line known as the whiskers. Using this method we can easily see the outliers shown as the points on each graph. 

the following code was used to produce the box plot [9]:
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

The violin plot performs a similar role as the box plot. It differs from the box plot by showing the kernal density estimation of the underlying distribution.

The kernal density estimation is a non-parametric way to estimate the probability density function of a random variable. 

The following code was used  to produce the violin plot [10]:

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

From both the box plot and the violin plot, we again can see the easily distinguishable setosa species in the petal width and length. 
The other species are more closely related, however it is possible to draw conclusions using the data in the box and violin plot for petal width and length to identify each based on these measurements.  

### Pair plot - Overview

The seaborn module allows for the production of a pair plot which compares all the variables against each other on one series of plots.
This feature is preformed with the straightforward code shown below: 
````
sns.set_style("whitegrid")
sns.pairplot(df, hue="species")
plt.savefig("iris_pairplot")
plt.clf()
````
It is an extremely useful tool in data analytics. It provides an immediate overview of the data being worked with and allows us to identify any possible relationships at a high level. 

![Pair Plot](https://github.com/eoinlees/pands-project-2020/blob/master/iris_pairplot.png "Pair Plot")

The pair plot alows us to identiy the specific plots we wish to look at in more detail. 


## Detailed Analysis

Using the information from above, we can look in more detail at the data provided.

#### Histograms

Taking an overall view of the data in histogram form allows us to see the variation across the plot. 

These histograms were plotted in matplotlib using subplots to combine them together [11]. 
````
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
````
![Histograms](https://github.com/eoinlees/pands-project-2020/blob/master/subplothistograms.png "histograms subplot")

It is clear that a more detailed vew of each plot is needed. 

If we look at both sepal length and width, it is clear to see that these measurments do not give us much opportunity to differentiate each species. We could draw some conclusions based on the number of samples.

The code below shows how the facetgrid was created for the sepal length and width. It includes the `distplot` command to show the kernal density estimate along with the histogram. 
```` 
plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"sepal_length").add_legend()
plt.savefig("sepal_length_species.png")
plt.clf()
```` 
````
plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"sepal_width").add_legend()
plt.savefig("sepal_width_species.png")
plt.clf()
````
![Sepal Length](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_length_species.png "Sepal Length")

![Sepal Width](https://github.com/eoinlees/pands-project-2020/blob/master/sepal_width_species.png "Sepal Width")


Looking at Petal length we can identify Iris setosa easily. 

````
plt.figure(figsize = (20, 10)) 
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"petal_length").add_legend()
plt.savefig("petal_length_species.png")
plt.clf()
````
````
plt.figure(figsize = (20, 10))
sns.FacetGrid(df,hue="species",height=7, aspect=2).map(sns.distplot,"petal_width").add_legend()
plt.savefig("petal_width_species.png")
plt.clf()
````

![Petal Length](https://github.com/eoinlees/pands-project-2020/blob/master/petal_length_species.png "Petal Length")

![Petal Width](https://github.com/eoinlees/pands-project-2020/blob/master/petal_width_species.png "Petal Width")


# Conclusions

Petal length can be used to classify Iris setosa. The data presented in the Petal Length histogram contains only two clusters, thus it is possible to deduce Iris setosa. 

An approximation of Iris verginica and Iris versicolor can be made with the specied information added to this plot and could be used as a good estimation of a species based on measurment results. The classifications are shown below: 

### Classifications

The simplest method of classification is:
* If Petal width <= 1cm
    then setosa
* If petal width <= 1.5cm 
    then high probability virginic
* otherwise its versicolor



Further analysis is possible to deduce a more accurate classification using machine learning techniques. The scikit learn module is reccomended for further research into the area of machine learning with python. [12]

# Sources

[1] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

[2] https://gist.github.com/curran/a08a1080b88344b0c8a7

[3] https://archive.ics.uci.edu/ml/datasets/Iris

[4] https://www.datacamp.com/community/tutorials/machine-learning-in-r

[5] https://numpy.org/

[6] https://pandas.pydata.org/docs/user_guide/index.html

[7] https://seaborn.pydata.org/tutorial/axis_grids.html

[8] https://matplotlib.org/

[9] https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40

[10] https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e

[11] https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

[12] https://scikit-learn.org/stable/

