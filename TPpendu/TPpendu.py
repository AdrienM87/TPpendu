import re   #regex

# main test
if __name__ == "__main__":

    #words list charging
    fileWords = open("C:\_Projets VS19\TPpendu\TPpendu\english-usa-words.txt", "r")

    strWords = fileWords.read()
    listWords = strWords.split()

    #en-tête d'accueil
    print("Welcome to the hanged one game ;)")
    print("")
    print("The computer choose a word.")
    print("You have 8 chances to find it by trying letters one by one.")
    print("")

    continueChoice = True
    while continueChoice == True:   #bouclage sur les participations au jeu

        print("Fine! Good luck :)")
        print("")

        validTry = False
        while validTry != True:    #bouclage sur la validité de la saisie

            letterTried = input("Your try : ")
            inputLength = len(letterTried)

            if inputLength == 0:
                validTry = False
            elif inputLength > 1:
                validTry = False
                print("Invalid try. Only one by one.")
            else:
                validTry = re.search("[a-zA-Z]", letterTried)

                if not validTry:
                    print("Invalid try. Only letters are expected.")
                else:
                    print("Good!")  #test       


    #test
    for w in listWords:
        pass

    fileWords.close()
    input("")   #end