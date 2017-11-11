import random
from words import get_words

def main():

    print("-- HANGMAN GAME --")
    list_of_words = get_words()

    secret_word = list_of_words[random.randint(0, len(list_of_words))]
    blank_lines = list("_" * len(secret_word))

    tries = 0
    max_tries = ( len(secret_word) * 2 )
    word_guesses = ''.join(blank_lines)
    won_game = False


    def clear_screen():
        return print("\033[H\033[J")

    def wonGame(word, secret_word):
        if word == secret_word:
            return True
        else:
            return False

    def checkIfCharIsInWord(character, secret_word):
        got_a_match = False
        for index, value in enumerate(secret_word):
            if value == character:
                blank_lines[index] = character
                got_a_match = True

        clear_screen()

        if got_a_match == False:
            print("Bummer! {} wasn't in the secret word.".format(character))


    def charCheck(char):
        if len(char) != 1:
            return False
        else:
            return True

    while tries < max_tries:
        print("Tries: {}. Max tries: {}".format(tries, max_tries))
        choice = input("Enter a letter: ")

        while not charCheck(choice):
            clear_screen()
            choice = input("Please enter one character for your choice: ")

        checkIfCharIsInWord(choice, secret_word)
        word_guesses = ''.join(blank_lines)
        print(word_guesses)

        if wonGame(word_guesses, secret_word):
            won_game = True
            break

        tries += 1

    if won_game:
        print("YOU WIN!!! The secret word was '{}'.".format(secret_word))
    else:
        print("Sorry. You lose! The secret word was '{}'.".format(secret_word))

    play_again = input("Play again? (Y/n): ")
    if play_again.lower() == "n" or play_again.lower() == "no":
        return
    else:
        clear_screen()
        main()

main()
