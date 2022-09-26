# Import the required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Generate the box plot
sns.pairplot(iris, hue="species", size= 2.5)

# Display the plot
plt.show()


