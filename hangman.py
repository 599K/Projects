'''
hangman game
'''

import random

def main():
    hangman_game()


def hangman_game():
    words = ['apple', 'banana', 'elephant', 'guitar', 'kangaroo', 'butterfly', 'chocolate', 'pizza', 'rainbow',  'telescope']
    mistakes = 7
    word = random.choice(words)
    secret = '_' * len(word)

    print("This is a hangman game. Guess the secret word. You can make 7 guesses of letters, or 1 guess with a word.\n")

    while True:
        try:
            guess = input("Enter your guess: ")
            if not guess.isalpha():
                print("Please enter a letter or a word.")
                continue

            elif guess.isalpha():
                if mistakes == 0:
                    print(f"You lost! The secret word was: {word}")
                    quit()
                if len(guess) == 1:
                    if guess not in word:
                        mistakes -= 1
                        print(f"Letter not in secret word.")
                    elif guess in word:
                        new_secret = []
                        for char in word:
                            if char == guess:
                                new_secret.append(char)
                            elif char in secret:
                                new_secret.append(char)
                            else:
                                new_secret.append('_')
                        secret = ''.join(new_secret)
                        mistakes -= 1
                        
                    if secret == word:
                        print("Congratulations. You won!")
                        quit()
                    print(f"Progress: {secret}")
                    print()
                    print(f"Mistakes left: {mistakes}")

                elif len(guess) != 1:
                    if guess == word:
                        print("Congratulations. You won!")
                        quit()
                    elif guess != word:
                        print(f"You lost the game. The secret word was: {word}")
                        mistakes = 0
                        break

        except Exception as e:
            print(f"Error: {e}")


main()