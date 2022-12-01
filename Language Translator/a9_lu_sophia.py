# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 9
# Description:
# This program asks the user what language they would like to translate words into and then translates user's words

# getLanguages(fileName)
# Parameter: fileName is a string containing the name of a CSV file to read from (default value of "languages.csv")
# Return value: a list of strings representing the languages in the header row
def getLanguages(fileName="languages.csv"):
    fileOpen = open(fileName, "r")
    languagesLine = fileOpen.readline()
    languagesLine = languagesLine.strip()
    languagesList = languagesLine.split(",")
    # return list of languages
    return languagesList

# getSecondLanguage(langList)
# Parameter: langList is a list of the languages
# Return value: a string for the second language
def getSecondLanguage(langlist):
    # display to user
    print("Language Translator")
    print("Translate English words into one of the following languages:")
    for language in langlist[1:len(langlist)]:
        print(language, end=" ")
    print()
    secondLang = input("Enter a language: ")
    while secondLang.capitalize() not in langlist:
        print("This program does not support", secondLang.capitalize())
        secondLang = input("Enter a language: ")
    # return value
    return secondLang.capitalize()

# readFile(langList, langStr, fileName)
# Parameter 1: langList is a list of the languages
# Parameter 2: langStr is a string of containing the name of a language and it has a default value of "English"
# Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# Return value: a list of words in the language identified by the langStr parameter
def readFile(langList, langStr="English", fileName="languages.csv"):
    fileOpen = open(fileName, "r")
    headerLine = fileOpen.readline()
    # get index of the chosen language in each line
    langIndex = langList.index(langStr)
    # create empty list
    wordsList = []
    for line in fileOpen:
        line = line.strip()
        line_list = line.split(",")
        word = line_list[langIndex]
        wordsList.append(word)
    return wordsList

# createResultsFile(language)
# Parameter: language is a string containing the name of the second language
# Return value: a string containing the name of the results text file
def createResultsFile(language):
    resultsFile = language + ".txt"
    fileOpen = open(resultsFile, "w")
    print("Words translated from English to", language, file=fileOpen)
    fileOpen.close()
    return resultsFile

# translateWords(englishList, secondList, resultsFile)
# Parameter 1: englishList is a list of words in English
# Parameter 2: secondList is a list of words in the second language
# Parameter 3: resultsFile is a string containing the name of the text file
def translateWords(englishList, secondList, resultsFile):
    fileOpen = open(resultsFile, "a")
    repeat = "y"
    while repeat.lower() == "y":
        englishWord = input("\nEnter a word to translate: ")
        if englishWord.lower() not in englishList:
            print(englishWord, "is not in the English list.")
        else:
            wordIndex = englishList.index(englishWord)
            translated = secondList[wordIndex]
            if translated == "-":
                print(englishWord, "did not have a translation.")
            else:
                print(englishWord, "is translated to", translated)
                print(englishWord, "=", translated, file=fileOpen)
        # update while loop
        repeat = input("Another word (y/n)? ")
        while repeat.lower() not in "yn":
            repeat = input("Another word (y/n)? ")

    print("\nTranslated words have been saved to", resultsFile)

# defining main
def main():
    languages = getLanguages()
    englishWordsList = readFile(languages)
    chosenLanguage = getSecondLanguage(languages)
    chosenWordsList = readFile(languages, chosenLanguage)
    newFile = createResultsFile(chosenLanguage)
    translateWords(englishWordsList, chosenWordsList, newFile)

# calling main
main()
