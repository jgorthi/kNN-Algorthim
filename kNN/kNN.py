import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import math

# Assign colum names to the dataset
names = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

with open("Gorthi Jaswanth - iris.csv", 'r') as f:
    with open("updated_iris.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)

# Read dataset to pandas dataframe
dataset = pd.read_csv("updated_iris.csv", names=names)

feature_columns = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
x = dataset[feature_columns].values
y = dataset['Species'].values


def distance_cal(i, j):
    return pow((x[i][1] - j[1]), 2) + pow((x[i][2] - j[2]), 2) + pow((x[i][3] - j[3]), 2) + pow((x[i][0] - j[0]), 2)


p = [5.1, 3.8, 1.4, 0.2]
dist_list = list()

for l in range(100):
    distance = distance_cal(l, p)
    dist_list.append(distance)

print(dist_list)
dist_list = np.array(dist_list)
sort_index = np.argsort(dist_list)
print(sort_index)


k = int(math.sqrt(len(dist_list)) - 1)
setosa_count = 0
versicolor_count = 0
for m in range(k):
    if y[sort_index[m]] == 'Setosa':
        setosa_count += 1
    else:
        versicolor_count += 1

print(setosa_count, versicolor_count)

if setosa_count > versicolor_count:
    print("Setosa")
else:
    print("Versicolor")
