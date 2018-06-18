# Which words are can be reversed to make another word?
#

#Intro schpiel
print(
    "This app will search the dictionary for words with special properties. " +
    "It will e can look for words that can be reversed to create another word. " +
    "For example, the word 'FIRES' becomes 'SERIF' when reversed")

# Initialize word list from file
dict = open('./WordLists/XwiWordList.txt', 'r')

# Find all the words in the dictionary that start with the user's input
print("Creating a reverse dictionary")

reverseDict = []
intersectionSet = []

def reversed_string(a_string):
    return a_string[::-1]

for w in dict:
    if len(w) > 5:
        w = w.strip()
        reverseDict.append(reversed_string(w))

# move the file pointer back to the beginning of the dictionary, since we're about to use it again
dict.seek(0)

# Calculate the intersection of the dictionary subset and the reverse dictionary, leaving only real words
print("Scanning the reverse dictionary to find real words")
for w in dict:
    if len(w) > 5:
        w=w.strip()
        if w in reverseDict:
            intersectionSet.append(w + "\t" + reversed_string(w))            
            print(w)

print("We found %i words which when reversed are other dictionary words:" %len(intersectionSet))

for w in intersectionSet:
    print(w)

