import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

# Assign colum names to the dataset
names = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

with open("Gorthi Jaswanth - iris.csv", 'r') as f:
    with open("updated_iris.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)

# Read dataset to pandas dataframe
dataset = pd.read_csv("updated_iris.csv", names=names)

print(dataset)
# Histogram
plt.figure(figsize=(10, 7))
x = dataset["Petal.Length"]

plt.hist(x, bins=100, color="blue")
plt.title("Petal Length in cm")
plt.xlabel("Petal.Length")
plt.ylabel("Count")
plt.show()
# --------------------------------------
# Boxplot
plt.figure(figsize=(10, 7))
dataset.boxplot()
plt.show()

# --------------------------------------
# ScatterPlot
plt.scatter(dataset["Petal.Length"], dataset["Petal.Width"])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
# Using Seaborn
# Histogram
sb.distplot(dataset["Sepal.Length"], bins=100, kde=False, rug=True, color="green")
plt.show()
# --------------------------------------
# Boxplot
sb.boxplot(x=dataset["Petal.Length"], y=dataset["Species"], data=dataset)
plt.show()
# --------------------------------------
# ScatterPlot
sb.scatterplot(x=dataset["Petal.Length"], y=dataset["Sepal.Length"], hue="Species", data=dataset)
plt.show()