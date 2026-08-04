from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix ,accuracy_score
# from xy import pyplot as plt


digits = load_digits()
print(digits.keys())


df_data = pd.DataFrame(digits.data,columns=digits.feature_names)
df_target = pd.DataFrame(digits.target,columns=['target'])

print(df_data.head())
print(df_target.head())

merged_df = pd.concat([df_data, df_target], axis=1)
print(merged_df.head())

# for i in range(5):
#     plt.subplot(1, 5, i + 1)
#     plt.imshow(digits.images[i], cmap='gray')
#     plt.title(f"Label: {digits.target[i]}")
#     plt.axis('off')
#     plt.show()

train_data, test_data, train_target, test_target = train_test_split(
    df_data, df_target, test_size=0.2, random_state=42)

logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(train_data, train_target.values.ravel()) 

results = logistic_model.predict(test_data)
print(accuracy_score(test_target, results))
print(classification_report(test_target, results))

cm = confusion_matrix(test_target, results)
print(cm)
#plt.figure(figsize=(10, 7))
#plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
#plt.title('Confusion Matrix')
#plt.colorbar()  
#plt.show()
