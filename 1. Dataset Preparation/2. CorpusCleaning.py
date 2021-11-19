from nltk.corpus import brown
from nltk import FreqDist
import pandas as pd
import re

# This file helps clean the data so its ready for training a Morfessor Model

# Loading the single text file which contains all data. (This file was created using TextFileJoin.py)
filename = 'CombinedDataset.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


# Splitting sentences into individual words and storing them in an array
words = text.split()


# Removing punctuation, symbols and numbers
words = [word for word in words if word.isalpha()]


# Removing Roman Numerals
removed_roman = []
for word in words:
    if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", word)):
        pass
    else:
        removed_roman.append(word)
words = removed_roman


# Converting all words to lowercase
words = [word.lower() for word in words]


# Removing any english words
english_words = set(brown.words())
words = [w for w in words if not w in english_words]


# Getting the counts of each word in the dataset
word_data = []
freq_data = []
frequencies = FreqDist(words)
for word, freq in frequencies.items():
    word_data.append(word)
    freq_data.append(freq)


# Creating a text file that contains each word with its corresponding frequency in the corpus
# This text file will be used to train the Morfessor Model.
TextFile3 = open("Dataset.txt", "w")
for i in range(len(word_data)):
    TextFile3.write(str(freq_data[i]) + " " + word_data[i] + '\n')
TextFile3.close()


# This contains the same data as the text file created above, except its a csv file (excel).
# This file is used for finding specific words tha can be used to evaluate the model later on.
CleanedIsizuluCorpus = {
                            'Word': word_data,
                            'Frequency': freq_data
                        }

df = pd.DataFrame(CleanedIsizuluCorpus)
df.to_csv('Frequency of words.csv', index=False)
