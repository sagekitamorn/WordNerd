# Which words are the same as other words plus a letter?
#

#Intro schpiel
print(
    "This app will search the dictionary for words with special properties. " +
    "To start, we can look for words that, when you add an extra letter or letters, create another word. " +
    "For example, the word 'ore' becomes 'more' if you add the letter 'm'")

# Get user input
#myPrefix = "champ"
myPrefix = input("Which character or characters would you like to try? >  ")
print("You said %s" % myPrefix)
# frontOrBack = input("Would you like to add that to the font or back of dictionary words? [f/b]>  ")

# Initialize word list from file
dict = open('./WordLists/DefaultDictionary.txt', 'r')

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
#print("Now let's see what these look like without their heads")
print("Next we'll cut off their heads, then see which of those shorter versions are also in the dictionary")
for w in wordsThatStartWithMyPrefix:
    if len(w) > prefixLength:
        trimmedWordsThatStartWithMyPrefix.append(w[prefixLength:])
#print(trimmedWordsThatStartWithMyPrefix)

# move the file pointer back to the beginning of the dictionary, since we're about to use it again
dict.seek(0)

# Calculate the intersection of the trimmed subset and the dictionary, leaving only real words
for w in dict:
    w=w.strip()
    for x in trimmedWordsThatStartWithMyPrefix:
        if x == w:
            trimmedWordsThatAreInTheDictionary.append(x) 
            
            

print("We found %i words, whcih if you add '%s', are other dictionary words:" %(len(trimmedWordsThatAreInTheDictionary), myPrefix))

for w in trimmedWordsThatAreInTheDictionary:
    print('{0:12s} {1}'.format(myPrefix+w, w))

