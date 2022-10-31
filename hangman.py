from words import words
import random
import string

def valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print("word is: ",word)
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives ,"Lives left and you have used these letters:", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a leter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                 word_letters.remove(user_letter)

            else:
                lives = lives-1
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("This character has already been used please try another")
        else:
            print("Invalid charater please try again")

    if lives == 0:
        print("Sorry You Died!, the word was",word)

    else:
        print("Congratulations You guessed the Word ",word)
    

hangman()

