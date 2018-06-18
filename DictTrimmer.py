# Tool to shoten word lists by removing words that contain certain letters
#Intro schpiel
print("This tool will takes a word list and make a new list that includes only words that do not contain certain letters")

#Get user input
wordListFile = input("Provide a word list > ")
dict = open(wordListFile, 'r')
char = input("Nominate a letter; we'll make a new dictionary file excluding all words with this letter > ")

lineCounter = 0
writeCounter = 0
skipCounter = 0

# Scan the input word list and write words to a new list if they do not contain the chosen character

with open('_No' + char + '_' + wordListFile, 'w') as outputWordList:
    for w in dict:
        lineCounter+=1
        if char not in w: #chagnge this to be case-insensitive and diacritic insensitive
            outputWordList.write(w)
            writeCounter+=1
        else:   
            skipCounter+=1
print("Processed %i lines, writing %i lines and skipping %i words" %(lineCounter, writeCounter, skipCounter))
dict.close()
outputWordList.close()
