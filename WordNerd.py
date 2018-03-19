# This a comment?
#


# Main loop
#Intro schpiel
print(
    "This app will search the dictionary for words with special properties. " +
    "To start, we can look for words that, when you add an extra letter or letters, create another word. " +
    "For example, the word 'ore' becomes 'more' if you add the letter 'm'")

# Get user input
myPrefix = input("Which character or characters would you like to try? >  ")
print("You said %s" % myPrefix)
# frontOrBack = input("Would you like to add that to the font or back of dictionary words? [f/b]>  ")

# Initialize word list from file
dict = open('DefaultDictionary.txt', 'r')

# Find all the words in the dictionary that start with the user's input
prefixLength = len(myPrefix)
print("Your input is %s characters long" % prefixLength)

wordsThatStartWithMyPrefix = []
trimmedWordsThatStartWithMyPrefix = []
trimmedWordsThatAreInTheDictionary = []
for w in dict:
    if w.startswith(myPrefix):
        print(w)
        wordsThatStartWithMyPrefix.append(w.strip())

print("We found %i words that start with %s" %(len(wordsThatStartWithMyPrefix), myPrefix))
#print(wordsThatStartWithMyPrefix,sep='\n')

# Trim off the user input string from the front of the words in the dictionary subset
print("Now let's see what these look like without their heads")
for w in wordsThatStartWithMyPrefix:
    end = len(w)
    trimmedWordsThatStartWithMyPrefix.append(w[prefixLength:])
print(trimmedWordsThatStartWithMyPrefix)

# Calculate the intersection of the trimmed subset and the dictionary, leaving only real words
for w in dict:
    for x in trimmedWordsThatStartWithMyPrefix:
        if x == w:
            trimmedWordsThatAreInTheDictionary.append(x) 
            print(x)

print("We found %i words, whcih if you add %s, make words" %(len(trimmedWordsThatAreInTheDictionary), myPrefix))


