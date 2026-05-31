from game_data import data
import functions
import random
import art




def game(random_num1):


    random_num2 = random.randint(0, len(data) - 1)
    while random_num2 == random_num1:
        random_num2 = random.randint(0, len(data) - 1)

    functions.comparision(data, random_num1, random_num2)

    guess = input("Who has more followers? Type 'A' or 'B': ")
    guess = guess.upper()

    print("\n" * 50)

    #Displays the results and if wrong will make sure you don't continue
    cont = functions.check_answer(guess, data, random_num1, random_num2)

    return random_num2, cont





print(art.logo)

cont = True

random_num1 = random.randint(0, len(data) - 1)
while cont:
    random_num1 , cont = game(random_num1)


