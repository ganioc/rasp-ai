# Load libraries
import pandas as pd


col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label' ]

# Load dataset
pima = pd.read_csv("./marks.txt", header=None)

print(pima.head(5))


