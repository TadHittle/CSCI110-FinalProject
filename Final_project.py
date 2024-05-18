"""I initally was trying to do this with a turtle but gave up, this works better and
does not make my brain hurt, angles are hard, my main objective was to successfully
implement a second file for the word list, as I was struggling with this during the
class a fair bit."""


import random #makes random seleciton work
import unittest

def menu():
    while True:
        print("Welcome to Hangman")
        question = input("Would you like to play a game? (Y/N): ").upper()
        if question == 'Y':
            return True
        elif question == 'N':
            print("have a nice day, bye")
            return False
        else:
            print("Invalid input, enter Y or N to continue")

def get_random_word(): #function to grab word for game from textfile
    wordlist = []

    with open("hangman_wordlist.txt", 'r') as file: #opends .txt file
        wordlist = file.read().strip().split("\n")

    word = random.choice(wordlist) #grabs random word
    return word

def get_some_letters(word): #makes list of empty letter and stores letters from word
    letters = [] #make list
    temp = '_' * len(word) #makes underscore string based on ch in word

    for char in list(word):
        if char not in letters:
            letters.append(char)

    character = random.choice(letters)

    templist = list(temp) #replaces _ with new letter
    for num, char in enumerate(word):
        if char == character:
            templist[num] = char
    temp = ''.join(templist)
            
    return temp

def drawhangman(chances): #drawing section, gives player 7 guesses to get correct answer
    if chances == 6:
        print("________ ")
        print("|      | ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif chances == 5:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif chances == 4:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|      | ")
        print("|       ")
        print("|       ")
    elif chances == 3:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|     /| ")
        print("|       ")
        print("|       ")
    elif chances == 2:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\\ ")
        print("|       ")
        print("|       ")
    elif chances == 1:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\\ ")
        print("|     /  ")
        print("|       ")
    elif chances == 0:
        print("________ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\\ ")
        print("|     / \\ ")
        print("|       ")

def get_name():#function to get name of player and store in file
    print("Please enter your name: ")
    name = input().strip()
    with open('name.txt', 'w') as namefile:
        namefile.write(name + '\n')
    return name

def clear_name_file(): #I needed this because letters from name.txt were appearing in the gameplay
    with open('name.txt', 'w') as namefile:
        pass

def start_hangman_game(): #function that starts the game loop
    word = get_random_word() #call ranom word function
    temp = get_some_letters(word) #call new
    chances = 7 #starting number of opprotunites to guess, cant be changed b/c it will break drawing
    found = False

    while True: #a counter that gives a you loose method once you run out of guesses and exits the program
        if chances == 0:
            print(f"You Lost! the word was: {word}")
            print("Better luck next time")
            break
 
        print("=== Guess the word ===")
        print(' '.join(temp), end='') #gets temp list from get_some_letters function
        print(f"\t(btw, the word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have: ")
 
        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only") #keeps player from entering more than one CHR at at time
            continue
        else:
            found = False
            for num, char in enumerate(list(word)): #checks if word is in list
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
 
        if not found: #subtract a guess from the counter when wrong ch entered
            chances -= 1
 
        if '_' not in temp: #prints the win message, gives a count of remaining guesses, based of remaining blank spaces
            print(f"\nYou guessed it! Your word was: {word}")
            print(f"You got it in {7 - chances} guesses")
            break #break on win condition
        else:
            drawhangman(chances) #otherwise show chances and repeat loop
 
        print()

def hangman():
    clear_name_file()#Clear the name file at the beginning of the game
    while True:
        get_name() #gets player name
        start_hangman_game()
        replay = input("Would you like to play again (Y/N): ").upper()
        if replay != 'Y':
            with open('name.txt', 'r') as namefile:
                names = namefile.read().strip().split('\n')
            print("Thanks for playing " + ", ".join(names))
            
            break

class testhangman(unittest.TestCase): #testing suite

    def test_get_random_word(self):#Pulls word and then sees if it is actually in the file
        with open("hangman_wordlist.txt") as file:
            words = file.read().strip().split("\n")
        word = get_random_word()
        self.assertIn(word, words)

    def test_get_some_letters(self): #checks if string is correct lenght and a letter is revealed
        word = "testing"
        revealed_letters = get_some_letters(word)
        self.assertEqual(len(revealed_letters), len(word))
        self.assertTrue(any(char != '_' for char in revealed_letters))
                
unittest.main(exit=False)#runs testing suite
if menu():# only runs game if player said they want to play in menu
    hangman()
