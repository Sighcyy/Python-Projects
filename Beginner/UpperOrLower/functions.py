import art
SCORE = 0

def comparision(data, random_num1, random_num2):
    print("Compare A:", data[random_num1]['name'], ",", data[random_num1]['description'], ", from",
          data[random_num1]['country'])

    print(art.vs)

    print("Against B:", data[random_num2]['name'], ",", data[random_num2]['description'], ", from",
          data[random_num2]['country'])






def check_answer(guess, data, random_num1, random_num2):
    global SCORE
    if guess == 'A' and data[random_num1]['follower_count'] > data[random_num2]['follower_count']:
        SCORE += 1
        print(art.logo)
        print("You're right! Your Score:", SCORE)
        return True
    elif guess == 'B' and data[random_num1]['follower_count'] < data[random_num2]['follower_count']:
        SCORE += 1
        print(art.logo)
        print("You're right! Your Score:", SCORE)
        return True
    else:
        print(art.logo)
        print("Sorry, that's wrong! Your Final Score:", SCORE)
        return False


