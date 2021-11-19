# In this file we create a stem dictionary.
# The spell checker will then compare the morphemes from a segmented word to the stem to check the spelling.

# Finds the largest morpheme in a segmented word.
def biggestLength(word_arr):
    maxLen = 0

    for i in range(len(word_arr)):
        if len(word_arr[i]) > maxLen:
            maxLen = len(word_arr[i])

    return maxLen


stem_list = []

# The ZuluGoldTrain text file is a dataset of isiZulu word segmentations constructed by a linguist.
with open('ZuluGoldTrain.txt') as f:
    for line in f:
        sentence = line.split("|")

        if len(sentence) < 2:
            pass

        else:
            segmentation = sentence[1]

            if segmentation.count("-") == 0 and segmentation.isalpha() and len(segmentation) > 1:
                stem_list.append(segmentation)

            else:
                temp_arr = segmentation.split("-")
                longest_length_word = biggestLength(temp_arr)

                for i in range(len(temp_arr)):
                    current_word = temp_arr[i]

                    if len(current_word) == longest_length_word and current_word.isalpha() and len(current_word) > 1:
                        stem_list.append(current_word)

stem_list = list(sorted(set(stem_list)))


# Loading the prefix dictionary created using AffixExtraction.py
filename = 'PrefixDictionary.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
prefix = text.split()


# Loading the suffix dictionary created using AffixExtraction.py
filename = 'SuffixDictionary.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
suffix = text.split()


# Removing all stems that are contained within the prefix dictionary and stem dictionary.
final_stem_list = []
for i in range(len(stem_list)):
    word = stem_list[i]

    if prefix.count(word) > 0:
        continue
    elif suffix.count(word) > 0:
        continue
    else:
        final_stem_list.append(word)


# Saving our stem dictionary to a text file
TextFile1 = open("StemDictionary.txt", "w")
for s in final_stem_list:
    TextFile1.write(s + '\n')
TextFile1.close()
