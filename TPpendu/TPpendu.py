import re   #regex
import random

# main test
if __name__ == "__main__":

    #words list charging
    fileWords = open("C:\_Projets VS19\TPpendu\TPpendu\english-usa-words.txt", "r")
    strWords = fileWords.read()
    listWords = strWords.split()
    fileWords.close()

    #const
    nbMaxTries = 12

    #en-tête d'accueil
    print("Welcome to the hanged one game ;)\n")
    print("The computer choose a word.")
    print("You have 8 chances to find it by trying letters one by one.\n")


    isNewGame = 1     #bouclage sur les parties
    while isNewGame == 1:

        nbTries = nbMaxTries  #reset
        isWordFound = 0

        #choix random d'un mot dans la liste et initialisation
        nbMax = len(listWords)
        wordChoosed = listWords[random.randint(0, nbMax)]
        listLettersTried = list()
        wordState = list()

        for j, let in enumerate(wordChoosed):
            wordState.append((j, let, 0))

        print("Fine! Good luck :)\n")


        while nbTries > 0:   #bouclage sur les tentatives

            isValidTry = 0
            while isValidTry != 1:    #bouclage sur la validité de la saisie

                triesLine = "Tries left : " + str(nbTries) + " /"
                for l in listLettersTried:
                    triesLine += " " + l
                print(triesLine + "\n")

                wordLine = "The word :"
                i = 0
                while i < len(wordState):

                    if wordState[i][2] == 1:
                        wordLine += " " + wordState[i][1]
                    else:
                        wordLine += " _"

                    i += 1
                print(wordLine + "\n")

                letterTried = input("Your try ('0' to quit) : ")
                inputLength = len(letterTried)

                if inputLength == 0:
                    isValidTry = 0

                elif letterTried == "0":
                    isValidTry = 1
                    nbTries = 0
                
                elif not re.search("[a-zA-Z]", letterTried):
                    isValidTry = 0
                    print("Invalid try. Only letters are expected.\n")

                else:   #cas d'entrée de lettre valide : application de l'essai
                    
                    isValidTry = 1
                    nbTries -= 1

                    #cas d'une tentative de mot
                    if len(letterTried) > 1:
                        if letterTried == wordChoosed:
                            
                            isWordFound = 1                            
                        else:                            
                            print("What a shame! This is not exact...\n")

                        nbTries -= 1

                    #cas d'une tentative de lettre seule
                    else:
                        if letterTried in wordChoosed:

                            for k, let in enumerate(wordState):
                            
                                if let[1] == letterTried:

                                    tempLet = let
                                    wordState.pop(k)
                                    wordState.insert(k, (k, let[1], 1))

                            print("Good move!\n")
                        else:
                            if not letterTried in listLettersTried:
                                listLettersTried.append(letterTried)
                            print("Bad move ! It isn't in the word...\n")


                #vérification de l'état trouvé ou non du mot
                if isWordFound == 0:

                    isWordFound = 1
                    for let in wordState:
                        if let[2] == 0:
                            isWordFound = 0
                            break

                #Résultat
                if isWordFound == 1:
                    
                    print("Good Game! You found the word with " + str(nbMaxTries-nbTries) + " tries !")
                    endLine = "The word was :"
                    
                    for l in wordChoosed:
                        endLine += " " + l                    
                        
                    print(endLine + "\n")
                    nbTries = 0
                        
        
        if nbTries == 0 and isWordFound == 0:
            print("Looser!\n")
            
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