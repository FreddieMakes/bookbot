def main():
    directory = "books/"
    file = "frankenstein.txt"

    bookString = readBook(directory + file)
    totalWords = countWords(bookString)
    letterDic = countLetters(bookString)

    print(f"--- Begin report of {directory}{file} ---")
    print(f"{totalWords} words in the document.")
    print("")
    formatPrint(letterDic)
    print("--- End Report ---")
    


def readBook(filePath):
    with open(filePath) as file:
        return file.read()

def countWords(string):
    wordList = string.split()
    return len(wordList)

def countLetters(string):
    localString = string.lower()
    localDic = {}

    #Make a list of all the characters in the text.
    listLetters = list(localString)
    listDic = []
    for letter in listLetters:
        if letter.isalpha():
            if letter not in localDic.keys():
                localDic[letter] = 1
            else:
                localDic[letter] += 1

    for entry in localDic:
        listDic.append({"name": entry, "num": localDic[entry]})
    
    return listDic

def sort_on(dict):
    return dict["num"]

def formatPrint(dictionary):
    localList = dictionary
    localList.sort(reverse=True, key=sort_on)

    for i in localList:
        print(f"The '{i["name"]}' character was found {i["num"]} times")



main()
