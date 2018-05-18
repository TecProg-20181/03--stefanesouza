import random
import string

WORDLIST_FILENAME = "palavras.txt"
GUESSES_NUMBER = 8

def load_words_list():
    try:
        in_file = open(WORDLIST_FILENAME, 'r')
        line = in_file.readline()
        word_list = str.split(line)
    except:
        print("File not found!")
        quit()
    return word_list

def load_message():
    print ("Loading word list from your file...")
    words = load_words_list()
    print (" Total of", len(words), "words loaded.")

def random_words(word_list):
    secret_word = random.choice(word_list).lower()
    return secret_word

def word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed = ''

    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_'
    return guessed

def get_available_letters():
    available = string.ascii_lowercase
    return available

def update_letters(letters_guessed):
    letters = get_available_letters()
    for letter in letters:
        if letter in letters_guessed:
            letters = letters.replace(letter, '')
    return letters

def different_letters(secret_word):
    different_list = set(list(secret_word))
    return len(different_list)

def welcome_game(secret_word):
    load_message()
    different_list = different_letters(secret_word)

    print ('\n-------------------------------------')
    print ('    WELCOME TO THE GAME, HANGAM!')
    print ('I am thinking of a word that is', len(secret_word), 'letters long.')
    print ('And it has ', different_list, ' different letters.')
    print ('-------------------------------------\n')

def end_game(secret_word, letters_guessed):
    if word_guessed(secret_word, letters_guessed) == True:
        print ('Congratulations, you won!\n')
    else:
        print ('Sorry, you ran out of guesses. The word was ', secret_word, '.\n')

def hangman():
    guesses = GUESSES_NUMBER
    letters_guessed = []
    word_list = load_words_list()
    secret_word = random_words(word_list)
    welcome = welcome_game(secret_word)
    different_list = different_letters(secret_word)

    while  word_guessed(secret_word, letters_guessed) == False and guesses > 0:
        letters = update_letters(letters_guessed)

        print ('   ATTENTION: You have ', guesses, 'guesses left.')
        print (' Available letters: ', letters)

        if different_list > guesses:
            print ('You are almost without guesses! You can choose another word, insert 1.')

        letter = input('\n Please guess a letter: ')

        if letter == '1':
            hangman()

        if letter in letters_guessed:
            guessed = get_guessed_word(secret_word, letters_guessed)
            print ('Oops! You have already guessed that letter: ', guessed)

        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed = get_guessed_word(secret_word, letters_guessed)
            print ('Good Guess:  ', guessed)

        else:
            guesses -= 1
            letters_guessed.append(letter)
            guessed = get_guessed_word(secret_word, letters_guessed)
            print ('Oops! That letter is not in my word: ',  guessed)
        print ('\n------------------------------------\n')

    else:
        end_game(secret_word, letters_guessed)


def play_game():
    hangman()

play_game()
