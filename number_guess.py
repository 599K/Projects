import random

def main():
    game_start()
    guesser()
                

def game_start():
    print("This is a number guessing game. My number is in the range 0 and 100. Guess my number (or enter 'quit' anytime to exit)")


def guesser():
    num = random.randrange(100)
    
    while True:
        print(num)
        guess = input("Guess: ")
        if guess == 'quit':
            exit()

        try:
            guess = int(guess)
        except Exception as e:
            print("Please enter numbers between 0 and 100.")
            continue
        else:
            if guess == num:
                print("Congratulations. You guessed my number!")
                quit()
            elif guess < num:
                print("My number is higher!")    
            elif guess > num: 
                print("My number is lower!")


main()