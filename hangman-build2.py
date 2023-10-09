import random

#declare ASCII art as a constant
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   0   |
       |
       |
      ===''','''
   +---+
   0   |
   |   |
       |
      ===''','''
   +---+
   0   |
  /|   |
       |
      ===''','''
   +---+
   0   |
  /|\  |
       |
      ===''','''
   +---+
   0   |
  /|\  |
  /    |
      ===''','''
   +---+
   0   |
  /|\  |
  / \  |
      ===''', '''
   +---+
  [0   |
  /|\  |
  / \  |
      ===''', '''
   +---+
  [0]  |
  /|\  |
  / \  |
      ===''']

#words list as a string
#words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

#words list as a dictionary
words = {'Colours': 'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana mango strawberry tomato'.split(),
'Animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}

#1 GENERATE A RANDOM WORD FROM LIST
#def getRandomWord(wordList):
    #This function returns a random string from the passed list of strings
    #wordIndex = random.randint(0, len(wordList) - 1)
    #return wordList[wordIndex]

#New function with dictionary
def getRandomWord(wordDict):
    #randomly select key from dictionary
    wordKey = random.choice(list(wordDict.keys()))
    
    #randomly select a word from the key's list
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    #return the randomly selected word
    return [wordDict[wordKey][wordIndex], wordKey]

#2 DISPLAY BOARD TO PLAYER
def displayBoard(missedLetters, correctLetters, secretWord):
    #Get hangman pic according to index set by number of missed letters
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    #print list of missed letters
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    #Display the secret word with blanks    
    blanks = '_' * len(secretWord)

    #Replace blanks with correctly guessed letters
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    #Show the secret word with spaces in between each letter
    for letter in blanks: 
        print(letter, end=' ')
    print()

#This function makes sure the player entered a single letter and not something else
#Returns the letter the player entered. 
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

#This function returns True if the player wants to play again; otherwise it returns False
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#GAME LOOP - Main Program starts here

#generate a random secret word
#secretWord = getRandomWord(words)
secretWord, category = getRandomWord(words)

#display the game board
print('H A N G M A N')

#select game difficulty
difficulty = 'X'
while difficulty not in 'EMH':
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
    difficulty = input().upper()
    
    #reduce number of guesses for M or H
    if difficulty == 'M':
        #delete two hangman pics
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        #delete more pics for Hard
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
        
missedLetters = ''
correctLetters = ''
gameIsDone = False #flag variable to check if player has won

while True: 
    print("The secret word is from the category: " + category)
    displayBoard(missedLetters, correctLetters, secretWord)

    #Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    #Check if guess is in secret word
    if guess in secretWord:
        #add guess to correct letters list
        correctLetters = correctLetters + guess
        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                print(secretWord[i])
                foundAllLetters = False
                break
            
        #if all the letters have been found
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
            
    else:
        #handle incorrect guesses
        missedLetters = missedLetters + guess
        
        #Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run of out guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    
    #end the game if the player has won
    if gameIsDone:
        #reset variables if game is over
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            #secretWord = getRandomWord(words)
            secretWord, category = getRandomWord(words)
        else:
            break    
        
