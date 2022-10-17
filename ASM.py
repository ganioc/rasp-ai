# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# import Decision Tree Classifier

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

# Load dataset,
pima = pd.read_csv("diabetes.csv",header=None, names=col_names)
print(pima.head(5))

# split dataset in featuers and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]  # Feature variables,
y = pima.label # Target variable,

# Split dataset into traing set and test set
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

['Pregnancies', 'Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure', 'DiabetesPedigreeFunction']

# Create Decision Tree classifer object,
clf = DecisionTreeClassifier()
# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)
# Predict the response for test dataset,
y_pred = clf.predict(X_test.drop(0))


# Model accuracy
print("Accuracy:", metrics.accuracy_score(y_test.drop(0), y_pred))





