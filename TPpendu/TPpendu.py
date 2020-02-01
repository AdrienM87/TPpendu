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


    isNewGame = 1     #bouclage sur les parties
    while isNewGame == 1:

        nbLives = 8  #reset

        #choix random d'un mot dans la liste
        nbMax = len(listWords)
        wordChoosed = listWords[random.randint(0, nbMax)]

        print("Fine! Good luck :)")
        print("")


        isContinued = 1
        while isContinued == 1 and nbLives > 0:   #bouclage sur les tentatives

            isValidTry = 0
            while isValidTry != 1:    #bouclage sur la validité de la saisie

                letterTried = input("Your try ('0' to quit) : ")
                inputLength = len(letterTried)

                if inputLength == 0:
                    isValidTry = 0

                elif inputLength > 1:
                    isValidTry = 0
                    print("Invalid try. Only one by one.")

                elif letterTried == "0":
                    isValidTry = 1
                    isContinued = 0
                
                elif not re.search("[a-zA-Z]", letterTried):
                    isValidTry = 0
                    print("Invalid try. Only letters are expected.")


                else:   #cas d'entrée de lettre valide : application de l'essai
                    isValidTry = 1

                    if letterTried in wordChoosed:
                        print("Well done!")
                    else:
                        print("What a shame!")
                        nbLives -= 1
        
        if nbLives == 0:
            print("Looser!")
            print("")
            
        #proposition de nouvelle partie
        isValidAnswer = 0
        while isValidAnswer != 1:    #bouclage sur la validité de la saisie
            print("Wanna try a new game?")
            answer = input("Yes or No ? (y/n) : ")
                        
            if answer == "y" or answer == "Y":
                isValidAnswer = 1
                isNewGame = 1
                print("")
            elif answer == "n" or answer == "N":
                isValidAnswer = 1
                isNewGame = 0
            else:
                isValidAnswer = 0


    #test
    for w in listWords:
        pass

    
    #input("")   #end