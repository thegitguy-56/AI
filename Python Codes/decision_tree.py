from sklearn import tree
import pandas as pd

# Take user input for dataset
n = int(input("Enter number of samples: "))
m = int(input("Enter number of features: "))

# Input feature names
feature_names = [input(f"Enter name of feature {i+1}: ") for i in range(m)]

# Input data
data = []
for i in range(n):
    row = input(f"Enter feature values for sample {i+1} (space-separated): ").split()
    data.append(row)

# Input target labels
target = []
for i in range(n):
    label = input(f"Enter target label for sample {i+1}: ")
    target.append(label)

# Convert data to DataFrame
df = pd.DataFrame(data, columns=feature_names)

# Encode features and labels (convert to integers)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
target = LabelEncoder().fit_transform(target)

# Create Decision Tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(df, target)

# Display decision tree
print("\nDecision Tree trained successfully!")

# Predict new sample
new_sample = input(f"Enter new sample feature values ({', '.join(feature_names)}) separated by spaces: ").split()
new_sample = [int(val) if val.isdigit() else le.fit_transform([val])[0] for val in new_sample]
prediction = clf.predict([new_sample])
print("Predicted class:", prediction[0])
