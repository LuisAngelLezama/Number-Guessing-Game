import random
number = 0
tries = 0
attempts = 0
check0 = True
check1 = True
check2 = True
check3 = True
check4 = True

while True:
    attempts = 0
    check2 = True
# Introducción.
    if check0 == True:
        print("Welcome to the Number Guessing Game.\nYou need to guess the random number between 1 and 100 in a limited number of chances")
    elif check0 == False:
        while check3 == True:
            bye = input("Do you want to continue playing? (Yes/No): ")
            if bye.upper() == "NO":
                check4 = False
                break
            elif bye.upper() == "YES":
                break
            else:
                print("Write Yes or No")
    if check4 == False:
        print("Thanks for playing!")
        break
    print("Choose a Difficulty by writing the number") 
# El usuario elije la dificultad en la que quiere jugar.
    print("1.Easy (10 Chances)\n2.Medium (5 Chances)\n3.Hard (3 Chances)\n4.Lunatic (1 Chance)")
    while check1 == True:
        choose_difficulty = int(input())
        if choose_difficulty < 1 or choose_difficulty > 4:
            print("Write a correct value")
        else:
            check1 = False
# Determinar el numero de intentos que tendra el usuario.
    if choose_difficulty == 1:
        tries = 10
    elif choose_difficulty == 2:
        tries = 5
    elif choose_difficulty == 3:
        tries = 3
    elif choose_difficulty == 4:
        tries = 1
    print("You have", tries, "tries to win!")
# El juego inicia
    print("The game stars NOW!!!")
    number = random.randrange(1,101)

    while tries >= 0:
        while check2 == True:
            guess = int(input(f"Try Number {tries}: "))
            attempts = attempts + 1
            if guess < 1 or guess > 100:
                print("Write a correct value (Remember 1 to 100)")
            else:
                check2 = False
        if guess == number:
            print("YOU WON, the number was", number)
            print("It took you", attempts, "attempts")
            break
        else:
            if guess < number:
                print("Incorrect!, the number you are searching is higher than the one you wrote")
            elif guess > number:
                print("Incorrect!, the number you are searching is lower than the one you wrote")
        tries = tries - 1
        check0 = False
        check1 = True
        check2 = True
        check3 = True

        if tries == 0:
            print("YOU LOST, the number was", number)
            break