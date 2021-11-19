# This was used to create the line graph used to find the best number of segmentations that optimizes accuracy

import matplotlib.pyplot as plt
import matplotlib as mlp

numOfSegmentations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
low_freq_words = [20, 25, 25, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
medium_freq_words = [30, 35, 50, 50, 55, 60, 65, 65, 65, 65, 65, 65, 65, 65, 65]
high_freq_words = [70, 80, 80, 80, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85]

mlp.style.use('seaborn-talk')

plt.plot(numOfSegmentations, low_freq_words, label="Low Frequency Accuracy", color="dodgerblue")
plt.plot(numOfSegmentations, medium_freq_words, label="Medium Frequency Accuracy", color="blueviolet")
plt.plot(numOfSegmentations, high_freq_words, label="High Frequency Accuracy", color="fuchsia")
plt.axvline(35, 0, 85, label="Optimal", linestyle='dotted', color='black')

plt.xlabel("Number of Segmentations", fontsize=14)
plt.ylabel("Spell Checker Accuracy", fontsize=14)
plt.title("Number of Segmentations Vs Spell Checker Accuracy\n", fontsize=18)
plt.legend()
plt.show()
