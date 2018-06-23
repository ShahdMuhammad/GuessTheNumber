import random

print("welcome to my humble house, what is your name?")

name = input()

print("hello ", name, " :D, mi casa es su casa :D, do you want to play a game with me?")
print("please notice that u must answer with capital letters or i wont be able to understand you :(\n")


while True:
    answer = input("Y for Yes, N for No\n")

    if answer is "Y" or answer is "N" :
        if answer is "Y":
            play = True
            print("great, so i am going to choose a random number and you have to guess it, you have 5 chances, good luck :D")
            print("let's get started :)")
        if answer is "N":
            play = False
            print("Too bad :(, you don't know what you are missing, however, see you later,", name, ":D.")
        break
    else:
        print("i told you", name, ", i can't understand you if you don't answer me as i say :(")
        print("try answering me correctly please :(")


while True:
    if play:
        print("choose the difficulty level :)")
        print("1- E for Easy")
        print("2- M for Medium")
        print("3- H for Hard")

        difLevel = input()
        if difLevel is "E":
            guess = random.randrange(1, 10)
            break
        elif difLevel is "M":
            guess = random.randrange(1, 100)
            break
        elif difLevel is "H":
            guess = random.randrange(1, 1000)
            break
        else:
            print("i told you", name, ", i can't understand you if you don't answer me as i say :(")
            print("try answering me correctly pleas :(")

numOfChances = 5

while numOfChances > 0 :

    playerGuess = int(input("Enter your guess here :D\n"))

    if playerGuess is guess :
        print("you answered it correctly, Big Congrats :D, see you next time")
        break
    elif playerGuess > guess :
        print("you went too far", name, ", take another guess :D")
        numOfChances -= 1
        print("you have ", numOfChances, " more chances")
    elif playerGuess < guess :
        print("you went too low", name, ", take another guess :D")
        numOfChances -= 1
        print("you have ", numOfChances, ", more chances")
    if numOfChances is 0 and playerGuess is not guess :
        print("you took all your your chances and you :(, the answer is ", guess, ", better luck next time, bye ^_^")


