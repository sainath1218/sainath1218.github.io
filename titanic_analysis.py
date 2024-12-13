import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Project: Titanic Survival Analysis
Author: Shiping Yu, Tianhao Wang, Bohan Yang, Andrew Xu, Sainath sunkara

Description:
This project analyzes the Titanic dataset to identify key factors influencing passenger survival rates.
The dataset includes demographic information, ticket class, and survival status of the passengers.

Key Questions to Address:
1. What is the overall survival rate?
2. How does gender influence survival rates?
3. What are the survival rates for different passenger classes?
4. Does age impact the likelihood of survival?
5. Is there a relationship between the port of embarkation and survival rate?
6. Does the number of family members aboard influence survival?
"""

# Step 1: Load the dataset
data = pd.read_csv('titanic.csv')
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

# Step 2: Data Cleaning
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data.drop(columns=['Cabin'], inplace=True)
data.drop_duplicates(inplace=True)

print(data.isnull().sum())
data.to_csv('cleaned_titanic.csv', index=False)

# Step 3: Exploratory Data Analysis (EDA)

# Visualize survival count
sns.countplot(x='Survived', data=data)
plt.title('Survival Count')
plt.show()

# Visualize passenger class distribution
sns.countplot(x='Pclass', data=data)
plt.title('Passenger Class Distribution')
plt.show()

# Visualize gender distribution
sns.countplot(x='Sex', data=data)
plt.title('Gender Distribution')
plt.show()

# Visualize embarkation port distribution
sns.countplot(x='Embarked', data=data)
plt.title('Embarkation Port Distribution')
plt.show()

# Visualize age distribution
sns.histplot(data['Age'], kde=True, bins=30)
plt.title('Age Distribution')
plt.show()

# Visualize fare distribution
sns.histplot(data['Fare'], kde=True, bins=30)
plt.title('Fare Distribution')
plt.show()

# Survival rate by gender
sns.barplot(x='Sex', y='Survived', data=data)
plt.title('Survival Rate by Gender')
plt.show()

# Survival rate by passenger class
sns.barplot(x='Pclass', y='Survived', data=data)
plt.title('Survival Rate by Passenger Class')
plt.show()

# Survival rate by embarkation port
sns.barplot(x='Embarked', y='Survived', data=data)
plt.title('Survival Rate by Embarkation Port')
plt.show()

# Step 4: Correlation Matrix
# Compute correlation matrix (only numeric columns)
correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()

# Plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Prepare data for model
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})  # Encode 'Sex' column
data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})  # Encode 'Embarked' column

X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
y = data['Survived']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
