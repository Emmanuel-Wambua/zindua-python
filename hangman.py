import random


def get_word():
    word_list = ["python","demon","bottlejobs","arsenal","boys"]
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [1 for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations you win!!!")
    else:
        print(f"Sorry,your tries are over,the word was{word}")


def display_hangman(tries):
    stages = [
        """
            -------
            |      |
            |      0
            |     \|/
            |      |
            |     / \

        """,
        """
            -------
            |      |
            |      0
            |     \|/
            |      |
            |     / 
        """,
        """
            -------
            |      |
            |      0
            |     \|/
            |      |
            |     
        """,
        """
            -------
            |      |
            |      0
            |     \|/
            |      
            |   
        """,
        """
            -------
            |      |
            |      0
            |     \|
            |      
            |     
        """,
        """
            -------
            |      |
            |      0
            |      |
            |      
            |     
        """,
        """
            -------
            |      |
            |      0
            |     
            |      
            |     
        """,
        """
            -------
            |      |
            |      
            |     
            |      
            |     
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again ? (Y/N)").uppeer() == "Y":
        word = get_word()
        play(word)