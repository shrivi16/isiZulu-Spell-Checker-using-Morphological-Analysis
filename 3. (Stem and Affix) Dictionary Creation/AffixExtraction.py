# In this file we create a prefix dictionary and a suffix dictionary.
# The spell checker will then compare the morphemes from a segmented word to these dictionary to check the spelling.
morphological_segmentations = []


# The ZuluGoldTrain text file is a dataset of isiZulu word segmentations constructed by a linguist.
with open('ZuluGoldTrain.txt') as f:
    for line in f:
        sentence = line.split("|")

        # Takes out all incomplete words (words that are not described in detail)
        if len(sentence) < 2:
            pass

        else:
            temp = sentence[1]

            # Only looking for words with at least 1 segmentation
            if temp.count("-") != 0:

                # Removing anything that's not made up of alphabets e.g. punctuations, numbers etc...
                if temp[0].isalpha():
                    morphological_segmentations.append(temp)


# Finds the index of an element which has the largest character length
def findLargest(words):
    maxWordLen = 0
    indexOfElement = 0

    for i in range(len(words)):
        if len(words[i]) > maxWordLen:
            maxWordLen = len(words[i])
            indexOfElement = i

    return indexOfElement


prefix_list = []
suffix_list = []


# Extraction process
for i in range(len(morphological_segmentations)):

    segmentation = morphological_segmentations[i]
    seg_arr = segmentation.split("-")
    stem_index = findLargest(seg_arr)

    # Extracting prefix and suffix from the split up array
    prefix = []
    suffix = []

    for j in range(len(seg_arr)):
        if j == stem_index:
            continue
        elif j < stem_index and seg_arr[j].isalpha():
            prefix.append(seg_arr[j])
        else:
            if seg_arr[j].isalpha():
                suffix.append(seg_arr[j])

    prefix_list.extend(prefix)
    suffix_list.extend(suffix)

prefix_dict = {}
suffix_dict = {}


# For getting the counts of the prefixes
for i in range(len(prefix_list)):
    word = prefix_list[i]
    if word in prefix_dict.keys():
        prefix_dict[word] = prefix_dict.get(word) + 1
    else:
        prefix_dict[word] = 1


# For getting the counts of the suffixes
for i in range(len(suffix_list)):
    word = suffix_list[i]
    if word in suffix_dict.keys():
        suffix_dict[word] = suffix_dict.get(word) + 1
    else:
        suffix_dict[word] = 1

final_prefixes = []
final_suffixes = []


# The count variable below means that we only choose affixes that have a frequency of 10 and greater from the corpus.
count = 10

for key, value in prefix_dict.items():
    if value > count:
        final_prefixes.append(key)

for key, value in suffix_dict.items():
    if value > count:
        final_suffixes.append(key)

# By converting the list to a set, and then from a set back to a list we remove duplicates.
final_prefixes = list(sorted(set(final_prefixes)))
final_suffixes = list(sorted(set(final_suffixes)))


# Adding the prefixes found on wikipedia to our prefix dictionary if it is not already in our prefix dictionary.
filename = 'WikiPrefix.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
wiki_prefixes = text.split()

for i in range(len(wiki_prefixes)):
    if final_prefixes.count(wiki_prefixes[i]) == 0:
        final_prefixes.append(wiki_prefixes[i])


# Adding the suffixes found on wikipedia to our suffix dictionary if it is not already in our suffix dictionary.
filename = 'WikiSuffix.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
wiki_suffixes = text.split()

for i in range(len(wiki_suffixes)):
    if final_suffixes.count(wiki_suffixes[i]) == 0:
        final_suffixes.append(wiki_suffixes[i])


# By converting the list to a set, and then from a set back to a list we remove duplicates.
final_prefixes = list(sorted(set(final_prefixes)))
final_suffixes = list(sorted(set(final_suffixes)))


# Saving our prefix dictionary to a text file.
TextFile1 = open("PrefixDictionary.txt", "w")
for p in final_prefixes:
    TextFile1.write(p + '\n')
TextFile1.close()


# Saving our suffix dictionary to a text file.
TextFile2 = open("SuffixDictionary.txt", "w")
for s in final_suffixes:
    TextFile2.write(s + '\n')
TextFile2.close()
