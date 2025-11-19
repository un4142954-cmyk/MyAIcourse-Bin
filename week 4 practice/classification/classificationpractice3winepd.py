import pandas as pd
import numpy as py
import sklearn.preprocessing
import seaborn as sns
df = pd.read_csv('Classfication/winequality-red.csv' , delimiter=',')
print(df.head())
print(df.info())
print(df.describe())
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')
sns.lineplot(x='fixed acidity', y='quality', data=df)
plt.show()
from sklearn.preprocessing import StandardScaler

# Split data into features and label 
X = df[[ 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].copy()
y = df["quality"].copy()

print("X:" , X)
print("y:" , y)
scaler = StandardScaler()
scaler.fit(X)

# Transform features
X_scaled = scaler.transform(X.values)

# View first instance
print(X_scaled[0])


from sklearn.model_selection import train_test_split
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled,
                                                                  y,
                                                             train_size=.65,
                                                           random_state=25)
print("X_train_scaled:", X_train_scaled)
print("X_test_scaled:", X_test_scaled)
print("y_train:", y_train)      
print("y_test:", y_test)
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)      
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print(f"Train size: {round(len(X_train_scaled) / len(X) * 100)}% \n\
Test size: {round(len(X_test_scaled) / len(X) * 100)}%")
 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Instnatiating the models 
logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

# Training the models 
logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

# Making predictions with each model
log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

from sklearn.metrics import classification_report
model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}

for model_name, preds in model_preds.items():
    print(f"Classification report for {model_name}:\n")
    print(classification_report(y_test, preds))