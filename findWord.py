# findWord.py
# Cassidy Block and Luis Valdivia, March 10th, 2018

# This function gets all the lines from the file, and gets the word to search for (searchWord)
def FindIt(allLines, searchWord):
        print("Here are all the lines that contain the word", searchWord)
        
        # initialize counter for the line number
        c = 0

        # goes through each line in file
        for line in allLines:
                # checks to see if searchWord is in the line
                if searchWord in line:
                        # if word is found, the line number and the line with the word is printed
                        print(c , line, end="")                         
                c += 1

def main():
	# Open the text file to read it 
	filename = 'theRaven.txt'
	MyFile = open(filename, 'r')
	
        # Leave the next few lines below alone...
	lines = MyFile.readlines()

        # prompts the user to input a searchWord
	word = input("Enter word to find (or RETURN to quit): ")
	# checks to quit the program
	if (word != ""): 
		FindIt(lines, word)  

        # Close the text file 
	MyFile.close()
	
if __name__ == "__main__":
    main()


