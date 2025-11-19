import pandas as pd
import numpy as py
import sklearn.preprocessing

df = pd.read_csv('health_lifestyle_dataset.csv')
print(df.head())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['gender-in-num'] = le.fit_transform(df['gender'])

print("class lables mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['gender', 'gender-in-num']].head())
col_names = []
from sklearn.preprocessing import StandardScaler

#split data into features and lables
x =df[['age','gender-in-num','bmi','daily_steps','sleep_hours','water_intake_l','calories_consumed','smoker','alcohol','resting_hr','systolic_bp','diastolic_bp','family_history','cholesterol']].copy()
y =df['disease_risk'].copy()

print("x:",x)
print("y:",y)

#instantite scaler and fit on features 
scaler = StandardScaler()
scaler.fit(x)

#Transform features
x_scaled = scaler.transform(x.values)

# view first instance
print(x_scaled[0])

from sklearn.model_selection import train_test_split

#split data into train and test
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(x_scaled,
                                                                  y,
                                                             train_size=.4,
                                                           random_state=25)

#check the splits are correct
print(f"Train size: {round(len(X_train_scaled) / len(x) * 100)}% \n\
Test size: {round(len(X_test_scaled) / len(x) * 100)}%")
"""
train size: 40%
test size: 60%"""


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
# Store modle predictions in dictionary
# This makes it easier to itrate through each model
# and print the each results
model_preds = {
    "Logistic Regression": log_reg_preds,
    "support vector machine": svm_preds,
    "decession tree": tree_preds
}

for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test,preds)}", sep="\n\n")
    