
# For this code, you input the name of a .txt file you would liked spell checked,
# the program will go through it, make the misspelled words ALL CAPS,
# and print the numbers of times you misspelled a certain word.

# There is a dictionary program (called wordList) as well which is
# imported into the program, and which includes a couple examples of misspelled words.

# Possible problems?:
#
# The program is very basic and will only check for words that are in the
# additional wordList program.
#
# Also, the resulting .txt file has some formatting issues.



#This piece of code imports the list of misspelled words from another piece of code
from wordList import variations

# This portion asks the user for the file they want spell checked
fileLocation = str(input('''Please enter the name of the .txt file
that you would like to spell check:'''))
# This part opens the file and also creates a new one for the output
f = open(fileLocation, "r")
g = open("testresults.txt", "w")

# Dictionary that keeps track of how many words are misspelled
d = {}




spellCheck = list(variations.items())


#main loop
for word in f:

    separated = word.split()

    for i in separated:

        misspelled = 0
        
        if i == ".":
            g.write(" ")

        for a in range(len(spellCheck)):
            if i in spellCheck[a][1]:
                g.write(spellCheck[a][0] + " ")
                if not spellCheck[a][0] in d:
                    d[spellCheck[a][0]] = 1
                else:
                    d[spellCheck[a][0]] += 1
                misspelled += 1
                continue

            
        #writes the correct words to the new file
        if misspelled == 0:
            g.write(i + " ")
        else:
            pass


items = list(d.items())

for k, v in items:
    print("\nYou misspelled the word:",k,",", v, "times")

print('''\nPlease check the corrected file in which all
of your errors are fixed.\n\nYou can find them by looking for
the words in all capital letters''')


g.close()
f.close()
