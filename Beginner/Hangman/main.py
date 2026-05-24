import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
lives = 6

chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)

guessList = []
guessedList = []
for item in chosen_word:
    guessList.append('_')
    
game_over = False
while (game_over == False):
    print("Word to guess:" , "".join(guessList))
    guess = input("Guess a letter: ").lower()

    if guess in guessedList:
        print("You already guessed this letter")
    else:
        guessedList.append(guess)

        before_guess = guessList.copy()
        iteration = 0
        for item in chosen_word:
            if item == guess:
                guessList[iteration] = guess
            iteration += 1

        if before_guess == guessList:
            lives -= 1
            print("You guessed" , guess , ",that's not in the word. You lose a life.")


        print(stages[lives])
        print("****************************",lives,"/6 LIVES LEFT****************************")

        if lives == 0:
            game_over = True
            print("***********************IT WAS ","".join(chosen_word),"! YOU LOSE**********************")

        if "_" not in guessList:
            game_over = True
            print("****************************YOU WIN****************************")
