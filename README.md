# **pands-project-2020**


# Introduction

Into to porject. Aims and brief

# Background

Info reguarding the iris Data set and its history

# Data Format

info regarding how the data is presented. the file type. its source. 

Show graph with details

|sepal_length| sepal_width| petal_length | petal_width |    species|
|0             |5.1|          3.5|           |1.4|          0.2|     setosa|
|1             |4.9|          3.0|           |1.4|          0.2|     setosa|
|2             |4.7|          3.2|           |1.3|          0.2|     setosa|
|3             |4.6|          3.1|           |1.5|          0.2|     setosa|
|4             |5.0|          3.6|           |1.4|          0.2|     setosa|
|..            |...|          ...|           |...|          ...|        ...|
|145           |6.7|          3.0|           |5.2|          2.3|  virginica|
|146           |6.3|          2.5|           |5.0|          1.9|  virginica|
|147           |6.5|          3.0|           |5.2|          2.0|  virginica|
|148           |6.2|          3.4|           |5.4|          2.3|  virginica|
|149           |5.9|          3.0|           |5.1|          1.8|  virginica|


#### Modules and data imported
````
# Import necessary modules to python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("iris.csv")
````

# Main Body

### Length vs width scatter plots

#### Petal Length Vs. Petal Width
![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/all_petal_length_vs_petal_width.png "Logo Title Text 1")


#### Sepal Length Vs. Sepal Width

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/all_sepal_length_vs_sepal_width.png "Logo Title Text 1")



### Box plot and violin plot

#### Box Plot

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/boxplot.png "Logo Title Text 1")


#### Violin Plot

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/violinplot.png "Logo Title Text 1")

### Pairplot - Overview

````
sns.set_style("whitegrid")
sns.pairplot(df, hue="species")
plt.savefig("iris_pairplot")
plt.clf()
````

![alt text](https://github.com/eoinlees/pands-project-2020/blob/master/iris_pairplot.png "Logo Title Text 1")



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

https://seaborn.pydata.org/tutorial/axis_grids.html

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://github.com/RitRa/Project2018-iris

https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e

https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

https://www.youtube.com/watch?v=5dLG3JDk2VU

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet