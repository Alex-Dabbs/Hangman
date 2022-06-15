import random

#This file plays the game Hangman in three difficulties determined by the player once the program starts. The player can opt for
#easy, intermediate or expert, the only difference being the amount of attempts they have to guess the word. Players can end the 
#program either by typing 4 in the Game Menu or by typing a word into the hangman input option which will return the player
#to the main menu where they can end the program from there. Progress will be shown throughout each guess and will end once
#the player makes one full word guess or if they run out of attempts.

#This is a list of words 50 words that the program will randomly choose between. 
word = random.choice("""chin abstract cry agile pump crouch fault latest try improve occupation carry hook land 
biography note seize stick random delicate bitter storm check manufacter domestic makeup compact temperature 
disgrace example leash scene card bed plagiazrize return mood jaw margin lonely allowance pierce tiger fibre costume 
quote begin flock government afford
""".split()).upper()

#Game Menu text.
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

#This will convert dashes into letters if they are correct guesses. Dashes will remain if the guess is not correct or if
#the word is guessed entirely and the game is won. If the player guesses all the letters and coverts every dash, they must still
#guess the word in its entireity.
def dashes_into_letters(word, dashes, attempt):
    for index, char in enumerate(word):
        if char == attempt:
            dashes[index] = attempt
    print(dashes)

#This will display a number of underscores depending on how long the word is and tell the player how many letters are in the word.
def char_frequency(word): 
    count = 0
    for char in word: 
        count += 1
    for char in word: 
        print(' _ ', end='')
    print(f'\nThere are {count} letters in the word.')

#The main program that defines a list of variables and uses if, elif and else statements under an infinite while loop.
def hangman(word, mode, alloted_attempts):
    char_frequency(word)
    print(f'\n{mode} Mode: You have {alloted_attempts} attempts to guess the word! If you think you know the word at anytime, just type it in! Good luck!\n')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    special_characters = """!@#$%^&*()_+~`-={ }|[]\:";'<>?,./"""
    used_attempts = 0
    letters_guessed = []
    dashes = [' _ '] * len(word)
    #Every time a continuation occurs, the player will be asked to input a letter.
    while used_attempts <= alloted_attempts:
        attempt = input('\nLetter Guess: \n').upper()
        count = word.count(attempt)
        #if the guess is only 1 letter and it is in the alphabet and not already in the list of letters guessed, the 
        #letter will be added to the list. Otherwise, the list will not add anything and only display itself.
        if len(attempt) == 1 and attempt in alphabet and attempt not in letters_guessed:
            letters_guessed.append(attempt)
            print(f'Your guessed letters: {letters_guessed}')
        else: 
            print(f'Your guessed letters: {letters_guessed}')
        #if the player guesses the word correclty they will be praised and sent back to the Game Menu.
        if attempt == word:
            print(f'Congrats! You got the word: {word}.')
            print('Ending Hangman. Run it again if you would like to keep playing. \n')
            exit()
        #if the guess is more than 1 letter and it is an incorrect guess, this function will search through each character
        #in the guess and determine if there are any special characters, digits or a mix thereof. If so, it will give the 
        #player another chance to guess. However, if the guess only has letters, then the program will determine it was an 
        #official guess and determine the guess as an incorrect one and end the game and exit the program.
        elif len(attempt) >= 2 and attempt != word:
            for char in attempt: 
                if any((char in special_characters) for char in attempt) or any((char.isdigit() for char in attempt)):
                    dashes_into_letters(word, dashes, attempt)
                    print('Invalid - Guesses must contain only letters.')
                    break
                elif any((char in alphabet) for char in attempt):
                    dashes_into_letters(word, dashes, attempt)
                    print(f'Nice try! But unfortunately the word was {word}. Game Over!')
                    print('Ending Hangman. Run it again if you would like to keep playing.\n')
                    exit()
        #if the player presses enter, this will explain what happened and provide another chance with no penalty.
        elif len(attempt) == 0:
            dashes_into_letters(word, dashes, attempt)
            print('You did not type anything!')
            continue
        #if the guess is 1 character long and not in the alphabet, then this will tell the player what the guess must
        #contain and let the player try again without penalty.
        elif len(attempt) == 1 and attempt not in alphabet:
            dashes_into_letters(word, dashes, attempt)
            print('Invalid - Guess must contain a letter.')
            continue
        #if the guess is a letter and there is one of those letters in the word: 
        elif attempt in word and count == 1:
            dashes_into_letters(word, dashes, attempt)
            print(f'There is one {attempt}.')
        #if the guess is in the word but there are 2 or more instances of those letters: 
        elif attempt in word and count >= 2:
            dashes_into_letters(word, dashes, attempt)
            print(f'There are {count} {attempt}s.')
        #if the guess was a letter but not in the word, this statement will split it up into two scenarios: 
        #The first will determine if the player has used all of their attempts and if so, reveal the word and tell them 
        #Game Over and exit the program. The second will run if the player still has guess remaining and alert
        #them as to how many they have. 
        elif attempt in alphabet and attempt not in word:
            used_attempts += 1
            if used_attempts == alloted_attempts:
                dashes_into_letters(word, dashes, attempt)
                print(f'Game Over! The secret word was {word}. Better luck next time!')
                print('Ending Hangman. Run it again if you would like to keep playing.\n')
                exit()
            dashes_into_letters(word, dashes, attempt)
            print(f'There are no {attempt}s. \nYou have {alloted_attempts-used_attempts} attempts left.')
            if len(attempt) == 1 and attempt in alphabet and attempt not in letters_guessed:
                letters_guessed.append(attempt)
                print(letters_guessed)
            continue
        #in cases of unexpected inputs or a problem with the program. The game will exit and require the user to restart it.
        else: 
            print('Error...exiting program.')
            exit()
            
#This takes the input the player gives and matches it to the difficulty level according to the Game Menu.
#if the player does not enter a number 1-4, then the program tells them what went wrong and loops back to 
#asking for their input.
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

if __name__ == '__main__':
    difficulty_selection()