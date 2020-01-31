# main test
if __name__ == "__main__":

    #words list charging
    fileWords = open("C:\_Projets VS19\TPpendu\TPpendu\english-usa-words.txt", "r")

    strWords = fileWords.read()
    listWords = strWords.split()

    for w in listWords:
        print(w)

    fileWords.close()

    input("")