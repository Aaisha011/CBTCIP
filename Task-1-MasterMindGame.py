import random

num = random.randrange(1000, 10000)
chances = 5
guess = int(input(f"Guess a 4-digit number, you have {chances} chances: "))

if num == guess:
    print("Congratulations! You have won the game, You are a Mastermind")
else:
    tries = 0
    while guess != num and chances > 0:
        tries += 1
        chances -= 1
        right_digits = 0
        guess = str(guess)
        num_str = str(num)
        correct = ['X'] * 4

        for i in range(4):
            if guess[i] == num_str[i]:
                right_digits += 1
                correct[i] = num_str[i]

        if right_digits < 4 and right_digits > 0:
            print(f"Not the right guess, but you guessed {right_digits} number(s) right")
            print("Current status is:", " ".join(correct))
            guess = int(input(f"Guess a 4-digit number, you have {chances} chances left: "))

        elif right_digits == 0 and chances > 0:
            print("None of the digits you have guessed are right")
            guess = int(input(f"Guess a 4-digit number, you have {chances} chances left: "))
        
        if guess == num:
            print(f"Congratulations! You have won in {tries} chances and now you are a Mastermind")
            break

    if chances == 0:
        print("Sorry, you lost as you ran out of chances")
        print(f"The correct number was {num}")
