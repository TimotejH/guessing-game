import random
import json
import datetime
import operator

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0

player_name = input("Enter your player name: ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! " + str(player_name) + " It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player_name, "secret_number": secret, "wrong_guesses": wrong_guesses})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list, indent=2))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)

score_list.sort(key = operator.itemgetter("attempts"), reverse = False)

for score_dict in score_list[0:3]:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. Wrong guesses were: {4}".format(score_dict.get("player_name"), str(score_dict.get("attempts")), score_dict.get("date"), score_dict.get("secret_number"), score_dict.get("wrong_guesses"))

    print(score_text)
