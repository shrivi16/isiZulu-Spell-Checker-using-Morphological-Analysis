import glob

# The data from the dataset folder are contained within 400 separate text files.
# The code below helps write all of this separate data into one file.


# load in the data from the dataset directory.
file_list = glob.glob("Dataset/*.txt")

# Joining all text files from the above directory and writing it to one single text file.
with open('CombinedDataset.txt', 'w') as corpus:
    for f in file_list:
        for line in open(f, 'r', encoding='utf-8'):
            corpus.write(line)
