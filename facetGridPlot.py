# Import the required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Generate the Facet Grid Plot
sns.FacetGrid(iris, hue="species", size=6).map(plt.scatter, "sepal_length", "sepal_width").add_legend()

# display the plot
plt.show()





