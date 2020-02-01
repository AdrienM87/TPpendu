import re   #regex
import random

# main test
if __name__ == "__main__":

    #words list charging
    fileWords = open("C:\_Projets VS19\TPpendu\TPpendu\english-usa-words.txt", "r")
    strWords = fileWords.read()
    listWords = strWords.split()
    fileWords.close()

    #en-tête d'accueil
    print("Welcome to the hanged one game ;)")
    print("")
    print("The computer choose a word.")
    print("You have 8 chances to find it by trying letters one by one.")
    print("")

    continueChoice = 1
    while continueChoice == 1:   #bouclage sur les participations au jeu

        #choix random d'un mot dans la liste
        nbMax = len(listWords)
        wordChoosed = listWords[random.randint(0, nbMax)]

        nbLives = 8
        print("Fine! Good luck :)")
        print("")

        validTry = 0
        while validTry != 1:    #bouclage sur la validité de la saisie

            letterTried = input("Your try ('0' to quit) : ")
            inputLength = len(letterTried)

            if inputLength == 0:
                validTry = 0

            elif inputLength > 1:
                validTry = 0
                print("Invalid try. Only one by one.")

            elif letterTried == "0":
               validTry = 1
               continueChoice = 0
            else:
                validTry = re.search("[a-zA-Z]", letterTried)

                if not validTry:
                    print("Invalid try. Only letters are expected.")
                else:
                    #cas d'entrée de lettre valide : application de l'essai
                    if letterTried in wordChoosed:
                        print("Well done!")
                    else:
                        print("What a shame!")


    #test
    for w in listWords:
        pass

    
    #input("")   #end