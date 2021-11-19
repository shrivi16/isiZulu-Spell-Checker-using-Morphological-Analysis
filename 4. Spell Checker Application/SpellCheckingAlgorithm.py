import morfessor

# Loading in the Suffix, Prefix and Stem Dictionaries created under the '(Stem and Affix) Dictionary Creation' folder.

# Loading Prefix Dictionary
filename = 'PrefixDictionary.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
prefixes = text.split()

# Loading Suffix Dictionary
filename = 'SuffixDictionary.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
suffixes = text.split()

# Loading Stem Dictionary
filename = 'StemDictionary.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
stems = text.split()


# This uses the morfessor model to generate a list of possible segmentations
def generateSegmentationList(word, n):
    io = morfessor.MorfessorIO()
    model = io.read_any_model('MorfessorModel.bin')

    segmentation = model.viterbi_nbest(word, n, 1.0)
    segmentationList = []

    for i in range(len(segmentation)):
        word = segmentation[i]
        segmentationList.append(word[0])

    return segmentationList


# We use this function to find the index of the segmentation that has the biggest length
def findLargest(words):
    maxWordLen = 0
    indexOfElement = 0
    for i in range(len(words)):
        if len(words[i]) > maxWordLen:
            maxWordLen = len(words[i])
            indexOfElement = i
    return indexOfElement


# If a word has no segmentation then we just compare it straight to the stem dictionary
def noSegmentation(word):
    if stems.count(word[0]) == 1:
        return True
    else:
        return False


# This returns true only if the word is segmented 100% correctly as well as spelt correctly
def perfectCase(segmentation):
    stemIndex = findLargest(segmentation)

    # In some cases the prefix can be larger then the stem. This prevents this issue e.g. uku-la-le-la
    if len(segmentation) > 1 and stemIndex == 0:
        stemIndex = findLargest(segmentation[1:-1])

    possibleStems = []

    # The case where multiple words are the same length as the stem word
    for i in range(len(segmentation)):
        if len(segmentation[i]) == len(segmentation[stemIndex]):
            possibleStems.append(segmentation[i])

    if len(possibleStems) == 1:
        pass

    else:
        for i in range(len(possibleStems)):
            if stems.count(possibleStems[i]) == 1:
                stemIndex = segmentation.index(possibleStems[i])
                break
        return False

    for i in range(len(segmentation)):
        if i == stemIndex:
            if stems.count(segmentation[i]) == 0:
                return False
        elif i < stemIndex:
            if prefixes.count(segmentation[i]) == 0:
                return False
        elif i > stemIndex:
            if suffixes.count(segmentation[i]) == 0:
                return False
    return True


# This converts the array of segmentations into a string separated by hyphens
def segmentationToString(seg):
    output = ""

    if len(seg) == 1:
        output = seg
    else:
        for i in range(len(seg)):
            if i == len(seg)-1:
                output = output + seg[i]
            else:
                output = output + seg[i] + " + "

    return output


# This runs the entire program
def result(word, n=35):
    output = ""
    ans = False

    # looping through all segmentations produced by morfessor
    segmentationList = generateSegmentationList(word, n)

    for i in range(len(segmentationList)):

        # This represents one segmentation from a list of possible segmentations
        segmentation = segmentationList[i]

        # Checking if the word has no segmentations
        if len(segmentation) == 1:
            isCorrect = noSegmentation(segmentation)
            if isCorrect:
                ans = True
                output = str(segmentation[0])
                return ans, output
            else:
                continue

        # This is if the word is segmented
        else:
            isCorrect = perfectCase(segmentation)
            if isCorrect:
                ans = True
                output = str(segmentationToString(segmentation))
                return ans, output
            else:
                continue

    return ans, output


# The code below was used for testing the model
# test = []
#
# # Testing
# filename = 'test.txt'
# file = open(filename, 'rt')
# text = file.read()
# file.close()
# test = text.split()
#
# # This gets the output of the model from the text.txt file
# prediction = []
# for i in range(len(test)):
#     ans, seg = result(test[i], 35)
#     if ans:
#         prediction.append(1)
#     else:
#         prediction.append(0)
#
# print(prediction)

# This piece of code was used calculating the accuracy of the model
# accuracy = []
# num_of_segmentations = 5
# for i in range(10):
#     print("\nNum of Segmentations: ", num_of_segmentations)
#     correct = 0
#     for j in range(len(test)):
#         ans, seg = result(test[j], num_of_segmentations)
#         print(ans,seg)
#         if ans:
#             correct = correct + 1
#     num_of_segmentations = num_of_segmentations + 5
#     acc = (correct/20) * 100
#     acc = int(acc)
#     accuracy.append(acc)
#
# print(accuracy)
