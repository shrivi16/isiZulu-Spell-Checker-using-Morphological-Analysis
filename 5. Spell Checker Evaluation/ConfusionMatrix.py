# This file was used to create all confusion matrices

from sklearn.metrics import confusion_matrix as cm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report

# Low Freq data -------------------------------------------------------------------------------------------------------

y_actual = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_predicted = [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
y_actual.reverse()
y_predicted.reverse()
print(classification_report(y_actual,y_predicted))

matrix = cm(y_actual, y_predicted)
print(matrix)
matrix = matrix/np.sum(matrix)
confusion_matrix = pd.DataFrame(data=matrix,
                                columns=['INCORRECT', 'CORRECT'],
                                index=['INCORRECT', 'CORRECT'])

sns.heatmap(confusion_matrix, linewidths=0.5, linecolor="black", annot=True, fmt='.2%', cmap="Blues")
plt.title("Low Frequency Word Evaluation",fontsize=14)
plt.ylabel("Actual Value",fontsize=14)
plt.xlabel("Predicted Value",fontsize=14)
plt.show()


# Medium Freq Data ----------------------------------------------------------------------------------------------------

y_actual = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_predicted = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]
print(classification_report(y_actual,y_predicted))

matrix = cm(y_actual, y_predicted)
matrix = matrix/np.sum(matrix)
confusion_matrix = pd.DataFrame(data=matrix,
                                columns=['INCORRECT', 'CORRECT'],
                                index=['INCORRECT', 'CORRECT'])
sns.heatmap(confusion_matrix, linewidths=0.5, linecolor="black", annot=True, fmt='.2%', cmap='Blues')
plt.title("Medium Frequency Word Evaluation",fontsize=14)
plt.ylabel("Actual Value",fontsize=14)
plt.xlabel("Predicted Value",fontsize=14)
plt.show()

# High Freq Data ------------------------------------------------------------------------------------------------------

y_actual = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_predicted = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0]
print(classification_report(y_actual,y_predicted))

matrix = cm(y_actual, y_predicted)
matrix = matrix/np.sum(matrix)
confusion_matrix = pd.DataFrame(data=matrix,
                                columns=['INCORRECT', 'CORRECT'],
                                index=['INCORRECT', 'CORRECT'])
sns.heatmap(confusion_matrix, linewidths=0.5, linecolor="black", annot=True, fmt='.2%', cmap='Blues')
plt.title("High Frequency Word Evaluation",fontsize=14)
plt.ylabel("Actual Value",fontsize=14)
plt.xlabel("Predicted Value",fontsize=14)
plt.show()

# Combination of all

y_actual = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_predicted = [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0]
print(classification_report(y_actual,y_predicted))

matrix = cm(y_actual, y_predicted)
matrix = matrix/np.sum(matrix)
confusion_matrix = pd.DataFrame(data=matrix,
                                columns=['INCORRECT', 'CORRECT'],
                                index=['INCORRECT', 'CORRECT'])
sns.heatmap(confusion_matrix, linewidths=0.5, linecolor="black", annot=True, fmt='.2%', cmap='Blues')
plt.title("Overall Model Evaluation",fontsize=14)
plt.ylabel("Actual Value",fontsize=14)
plt.xlabel("Predicted Value",fontsize=14)
plt.show()
