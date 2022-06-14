from cmath import inf
import random
import re

word = random.choice("""chin abstract cry agile pump crouch fault latest try improve occupation carry hook land 
biography note seize stick random delicate bitter storm check manufacter domestic makeup compact temperature 
disgrace example leash scene card bed plagiazrize return mood jaw margin lonely allowance pierce tiger fibre costume 
quote begin flock government afford
""".split()).upper()

print("""\nHangman! Guess the Word, Letter by Letter!
---------------------------------------------------------------------------------------------------
A random word will be generated and your job is to guess a letter!
If you wish to guess the word at any time during the game, just type the word you think it is!
But be warned, you have one chance to guess the word correctly, if it is incorrect, it's Game Over!

Select your difficulty below: 

    1: Easy Mode
    2: Intermediate Mode
    3: Expert Mode

    4. Exit Program

""")

def char_frequency(word): 
    count = 0
    for char in word: 
        count += 1
    for char in word: 
        print(' _ ', end='')
    print(f'\nThere are {count} letters in the word.')

#print(word)

def hangman(word, mode, alloted_attempts):
    char_frequency(word)
    print(f'\n{mode} Mode: You have {alloted_attempts} attempts to guess the word! If you think you know the word at anytime, just type it in! Good luck!\n')
    used_attempts = 0
    letters_guessed = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    dashes = [' _ '] * len(word)
    while used_attempts <= alloted_attempts:
        letter_guess = input('\nLetter Guess: \n').upper()
        letter_count = word.count(letter_guess)
        if letter_guess in word and letter_count == 1 and len(letter_guess) == 1: 
            dashes_into_letters(word, dashes, letter_guess)
            print(f'There is one {letter_guess}.')
            if len(letter_guess) == 1 and letter_guess in alphabet and letter_guess not in letters_guessed:
                letters_guessed.append(letter_guess)
                print(letters_guessed)
            continue
        elif letter_guess in word and letter_count >= 2 and len(letter_guess) == 1 and letter_guess not in letters_guessed: 
            dashes_into_letters(word, dashes, letter_guess)
            print(f'There are {letter_count} {letter_guess}s.')
            if len(letter_guess) == 1 and letter_guess in alphabet and letter_guess not in letters_guessed:
                letters_guessed.append(letter_guess)
                print(letters_guessed)
            continue
        elif letter_count == 0 and letter_guess in alphabet:
            used_attempts +=1
            if used_attempts == alloted_attempts:
                dashes_into_letters(word, dashes, letter_guess)
                print(f'Game Over! The secret word was {word}. Better luck next time!')
                print('Returning to Game Menu...\n')
                difficulty_selection()
            dashes_into_letters(word, dashes, letter_guess)
            print(f'There are no {letter_guess}s. \nYou have {alloted_attempts-used_attempts} attempts left.')
            if len(letter_guess) == 1 and letter_guess in alphabet and letter_guess not in letters_guessed:
                letters_guessed.append(letter_guess)
                print(letters_guessed)
            continue
        elif len(letter_guess) == 1 and letter_guess not in alphabet:
            dashes_into_letters(word, dashes, letter_guess)
            print('Invalid - Please choose a letter from the alphabet.')
            continue
        elif len(letter_guess) > 1 and letter_guess.isdigit():
            dashes_into_letters(word, dashes, letter_guess)
            print('Invalid - Please choose a letter from the alphabet.')
            continue
        elif len(letter_guess) > 1 and letter_guess != word and any(char.isalpha for char in letter_guess):
            dashes_into_letters(word, dashes, letter_guess)
            print(f'Nice try! But unfortunately the word was: {word}. Game Over!')
            print('Returning to Game Menu...\n')
            difficulty_selection()
        elif letter_guess == word: 
            dashes_into_letters(word, dashes, letter_guess)
            print(f'Congrats! You got the word: {word}!')
            print('Returning to Game Menu.\n')
            difficulty_selection()
        elif letter_guess in letters_guessed:
            dashes_into_letters(word, dashes, letter_guess)
            print('You have already guessed this letter. Please try again.')
            if len(letter_guess) == 1 and letter_guess in alphabet and letter_guess not in letters_guessed:
                letters_guessed.append(letter_guess)
                print(letters_guessed)
            continue
        else: 
            print('Error...ending game. \nPlease restart the program.')
            break

#hangman_easy(word)

def dashes_into_letters(word, dashes, letter_guess):
    for index, letter in enumerate(word):
        if letter == letter_guess:
            dashes[index] = letter_guess
    print(dashes)

def difficulty_selection():
    x = True
    while x == True:
        difficulty = (input('Choose Your Difficulty: \n'))
        if difficulty == '1':
            hangman(word, 'Easy', 8)
        elif difficulty == '2':
            hangman(word, 'Intermediate', 6)
        elif difficulty == '3': 
            hangman(word, 'Expert', 4)
        elif difficulty == '4': 
            exit()
        elif difficulty.isalpha():
            print('Error - Please select a number 1-4.')
            continue
        else:
            print('Error - Please select a number 1-4.')
            continue
difficulty_selection()