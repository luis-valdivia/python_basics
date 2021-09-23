# lab05.py

def ReadFile():
    filename = input("Enter filename: ")
    InFile = open(filename, 'r')

    count = 0
    for line in InFile:
        count += 1
    print("There are", count, "lines in the file", filename)
    return(filename)
    InFile.close()


def WriteFile(allLines):
    OutFile = open(allLines, 'w')

    for line in allLines:
        if OutFile != "I":
            OutFile.write(line)
    print("myout.txt written")

    OutFile.close()



# solution must be above this comment

# do not change any part of the code below
def main():
    linesRead = ReadFile()
    WriteFile(linesRead)

if __name__ == "__main__":
    main()
