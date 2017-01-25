import random

def print_hangman(lives):
    print()

def cencored_word(word, guesses):
    cencored = ""
    for letter in word:
        if guesses.count(letter) > 0:
           cencored += letter
        else:
            cencored += "*"
    return cencored

def get_word(filename):
    file = open("words.txt")
    content = file.readlines()
    file.close()

    rand = random.randint(0, len(content) - 1)
    word = content[rand].strip()
    word = word.lower()
    return word

def get_guess(guesses):
    guess = input("Please enter a letter: ").lower()
    while guesses.count(guess) > 0:
        guess = input("You already guessed that letter! Enter a new one:")
    guesses.append(guess)
    return guess

def check_won(word, guesses):
    won = True
    for letter in word:
        if not guesses.count(letter) > 0:
            won = False
    return won

game_played = False
while True:
    if game_played:
        print("1. Play again")
        print("2. Quit")
        choice = int(input(">"))
        if choice == 2:
            quit

    game_done = False
    word = get_word("words")
    lives = 6
    
    guesses = []
    while game_done == False:
        print_hangman(lives)
        print(cencored_word(word, guesses))
        guess = get_guess(guesses)
        found = False
        for letter in word:
            if guess == letter:
                found = True

        if found:
            print("Congrats, you found a letter!")
        else:
            lives -= 1
            print("Wrong! Lives left:", lives)

        if check_won(word, guesses):
            print("Congratulations, you won! The word was", word)
            game_done = True

        if lives == 0:
            print("\n")
            print("You loose! The word was:", word)
            break

    game_played = True
        
