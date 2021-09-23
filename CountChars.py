# CountChars.py
# Luis Valdivia and Cassidy Block, March 10th, 2018

# enables the reading of a URL
import urllib.request 

# This function reads all the lines, reads all the characters, makes a dictionary
def MakeD(xfile):
    
    # creates a dictionary for all ASCII characters and their number of occurrences
    d = {}
    for x in range(128):
        d[chr(x)] = 0

    # this runs when the file is a URL 
    if xfile[0:4] == "http":
        InFile = urllib.request.urlopen(xfile)
        lines = InFile.read().decode('utf-8') 
        for line in lines:
            for ch in line:
                # we use .lower() since we ignore all upper case letters
                d[ch.lower()] += 1
                
    # this runs when the file is not a URL             
    else:
        InFile = open(xfile, 'r')
        lines = InFile.readlines()
        for line in lines:
                for ch in line:
                    # we use .lower() since we ignore all upper case letters
                    d[ch.lower()]  += 1

    # returns the dictionary of all ASCII characters and their number of occurrences
    return d 



def main():
    # strings that must be used for output:
    prompt = "Enter filename: "
    titles = "char       count\n----       -----"
    itemfmt = "{0:5s}{1:10d}"
    totalfmt = "total{0:10d}"
    whiteSpace = {' ':'space', '\t':'tab', '\n':'nline', '\r':'crtn'}

    # Get file from user to read
    filename = input(prompt)

    # Call the function MakeD to create a dictionary myD of all ASCII characters
    # and their number of occurrences in the file

    myD = MakeD(filename)
 
    # Print out the title for the table of ASCII characters
    # and their number of occurrences in the file
    print(titles)

    # go through all keys in myD and put them in a sorted list
    s = sorted(myD.keys())

    #go through all characters in the sorted list
    for ch in s:
        if myD[ch] != 0 and ch  in whiteSpace:
            # prints type of whitespace and number of occurrences
            print(itemfmt.format(whiteSpace[ch], myD[ch]))
            
        elif myD[ch] != 0 and ch not in whiteSpace:
            # prints non-whitespace ASCII characters and their number of occurrences
            print(itemfmt.format(ch, myD[ch]))


    # prints total number of ASCII characters in file
    print(totalfmt.format(sum(myD.values()))) 


if __name__ == "__main__":
    main()


