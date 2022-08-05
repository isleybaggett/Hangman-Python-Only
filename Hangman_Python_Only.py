import random
import os
from time import sleep
 
#empty list to hold user choices so far and display secret word
userChoiceList = []
displayList = []

#following three list are the game categories
domesticAnimals = ['Cows', 'bull', 'Rabbit', 'Duck', 'Pig', 'Bee', 'Goat', 'Crab', 
                   'Fish', 'Chicken', 'Horse', 'Dog', 'Llamas', 'Ostrich', 'Camel', 
                   'Shrimp', 'Deer', 'Turkey', 'Dove', 'Sheep', 'Cat', 'Geese', 'Oxen', 'Reindeer']

wildAnimals = ['Antelope', 'Arctic wolf', 'Bald eagle', 'Porcupine', 'Bat', 'Bear', 'Camel', 'Chimpanzee', 
               'Coyote', 'Deer', 'Gorilla', 'Hare', 'Hedgehog', 'Hippopotamus', 'Kangaroo', 'Badger', 
               'Elephant', 'Elk', 'Fox', 'Giraffe', 'Koala', 'Leopard', 'Lion', 'Lizard', 'Monkey', 'Otter',
              'Owl', 'Mole', 'Panda', 'Rabbit', 'Rhinoceros', 'Raccoon', 'Rat', 'Squirrel', 'Tiger', 'Walrus', 
              'Bison', 'Reindeer', 'Possum', 'Chipmunk', 'Porcupine', 'Wolf', 'Woodpecker', 'Zebra', 'Wombat', 'Red panda']


stateNames = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ",
             "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas",
            "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana",
           "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
          "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands",
         "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

#variations of hangman
gameboard = ['       ______   \n      |      |  \n      |         \n      |         \n      |         \n      |         \n    __|_________ \n',
             '       ______   \n      |      |  \n      |      O  \n      |         \n      |         \n      |         \n    __|_________ \n',
             '       ______   \n      |      |  \n      |      O  \n      |     /   \n      |         \n      |         \n    __|_________ \n',
             '       ______   \n      |      |  \n      |      O  \n      |     /|  \n      |         \n      |         \n    __|_________ \n', 
             '       ______   \n      |      |  \n      |      O  \n      |     /|\ \n      |         \n      |         \n    __|_________ \n',
             '       ______   \n      |      |  \n      |      O  \n      |     /|\ \n      |     /   \n      |         \n    __|_________ \n',
             '       ______   \n      |      |  \n      |      O  \n      |     /|\ \n      |     / \ \n      |         \n    __|_________ \n']

#list to check and pick players category
userOptionList = ['domestic animals', 'wild animals', 'state names']
#intiating global variables
userCatChoice = ''
secretWord = ''
userGuess = ''
#global int and bool variables
i = False
h = 0
l = 6

#gameboard that your seeing as player
def game_Screen(letter, word):
    global gameboard
    global userCatChoice
    global h
    global l 
    global displayList

    #appending list with letter guessed
    userChoiceList.append(letter)
    word = word.upper()

    #changes displayed hangman and lowers misses left
    if letter not in word:
        h = h + 1
        l = l - 1

    #print results for the player
    print(gameboard[h])
    print('You typed: ' + letter)
    print('Your category is ' + userCatChoice + '.\nBeware you can only miss ' + str(l)+ ' more letters.\n')
    print('Your word is ', end = '')

    #interates through the word and creates the display for the secret word
    for j in range(0, len(word)):
        if word[j] == ' ':
            displayList.append(' ')
        elif word[j] in userChoiceList:
            displayList.append(word[j])
        else:
            displayList.append('_')
    #formating and displaying the secret word list
    print('\n')
    print(*displayList, sep = ' ')
    print('\n')
    
#uses random.choices to pick a word form our categories
def computer_Choice(category): 
    global stateNames
    global wildAnimals
    global domesticAnimals
    global secretWord
    if category == 'state names':
        secretWord = random.choice(stateNames)
    elif category == 'domestic animals':
        secretWord = random.choice(domesticAnimals)
    elif category == 'wild animals':
        secretWord = random.choice(wildAnimals)
    
#welcome screen and passing the category choice
def game_Menu():
    global userCatChoice
    print('Welcome to Hangman!')
    print('A classic game with dire consequences.\n')
    print('What category would you like to play?\n')
    print('Domestic Animals\nWild Animals\nState Names\n')
    userCatChoice = input('Please type one of the above options: ')
    userCatChoice = userCatChoice.lower()
    
#fuction handles the error if user misspells the options available
def wrong_Entry():
    global userCatChoice
    print('\nOops you typed ' + userCatChoice)
    print('Note: While capitalization does not matter, spelling and spaces do.\n')
    print('What category would you like to play?\n')
    print('Domestic Animals\nWild Animals\nState Names\n')
    userCatChoice = input('Please type one of the above options: ')
    userCatChoice = userCatChoice.lower()
    
#runs the game
def main_Logic ():
    global i
    #brings in the first game screen for the player to see
    game_Menu()
    #handles wrong category input
    while i == False:   
        if  userCatChoice not in userOptionList:
            wrong_Entry()
        else:
            break 
    #computer chooses the secret word
    computer_Choice(userCatChoice)
    #prompt player for input
    userGuess = input('Please type your first letter and hit enter:')

    x = False
    #makes sure the player enters one letter and no blank space
    while x == False:
        if int(len(userGuess)) != 1 or userGuess == ' ':
            print('Only enter one letter to start. (no blanks or spaces)')
            userGuess = input('Please type your first letter and hit enter: ')
        elif int(len(userGuess)) == 1:
            x = True
    userGuess = userGuess.upper()
    #clear screen
    os.system('cls')
    #run gamescreen function
    game_Screen(userGuess, secretWord)
    #loop decides if you won lost or need to continue
    while i == False:
        if '_' not in displayList:
            print('You won the answer was ' + secretWord)
            break
        elif h == 6:
            print('You lost the answer was ' + secretWord)
            break
        elif userGuess == secretWord.upper():
            print('You won the answer was ' + secretWord)
            break
        else:
            #clear the list to start a new .append with new user guess
            displayList.clear()
            #print out players letters so far
            print('Your guesses so far: ', end = '')
            print(userChoiceList)
            #prompt for another letter or guess
            userGuess = input('\nPlease type your next letter or take a guess and hit enter: ')

            z = False
            #handles first input player can now guess the word 
            while z == False:
                #guess is bigger than secret ask for another guess
                if int(len(userGuess)) > int(len(secretWord)):
                    print('Entered letter count is more than the secret word.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if the but empty space
                elif int(len(userGuess)) < 1 or userGuess == ' ':
                    print('Blank or space invalid.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if player choose a letter count more than one but less than the secret word
                elif int(len(userGuess)) < int(len(secretWord)) and int(len(userGuess)) > 1:
                    print('Entry letter count less than the secret word, if your not sure enter one letter.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if the userguess equaled the word or equaled 1 letter 
                elif int(len(userGuess)) == int(len(secretWord)) or int(len(userGuess)) == 1:
                    z = True
            userGuess = userGuess.upper()


            while userGuess in userChoiceList:
                userGuess = input('You have already selected that letter, please enter another letter: ')
                #guess is bigger than secret ask for another guess
                if int(len(userGuess)) > int(len(secretWord)):
                    print('Entered letter count is more than the secret word.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if the but empty space
                elif int(len(userGuess)) < 1 or userGuess == ' ':
                    print('Blank or space invalid.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if player choose a letter count more than one but less than the secret word
                elif int(len(userGuess)) < int(len(secretWord)) and int(len(userGuess)) > 1:
                    print('Entry letter count less than the secret word, if your not sure enter one letter.')
                    userGuess = input('Please type your next letter or take a guess, then hit enter: ')
                #if the userguess equaled the word or equaled 1 letter and not already choosen 
                elif (int(len(userGuess)) == int(len(secretWord)) or int(len(userGuess)) == 1) and userGuess not in userChoiceList:
                    break
            userGuess = userGuess.upper()
            os.system('cls')
            game_Screen(userGuess, secretWord)


#run interation of game        
main_Logic()
#asking if you want to play again and if yes run the game logic again otherwise exit
while i == False:
    #needs error handling
    quitOrNot = input('Would you like to play again? yes/no: ')
    if quitOrNot.lower() == 'yes':
        h = 0
        l = 6
        userChoiceList.clear()
        displayList.clear()
        os.system('cls')
        main_Logic()
    else:
        os.system('cls')
        print('Thanks for playing!')
        sleep(3)
        exit()







