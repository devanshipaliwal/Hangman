import random
print("Lets Play Hangman!")

man = [ """
                ------;
                |     
                |    
                |     
                |    
        """,
        """
                ------;
                |     O
                |    
                |     
                |     
        """,
        """
                ------;
                |     O
                |     |
                |     |
                |    
        """,
        """
                ------;
                |     O
                |    \|
                |     |
                |    
        """,
        """
                ------;
                |     O
                |    \|/
                |     |
                |    
        """,
        """
                ------;
                |     O
                |    \|/
                |     |
                |    / 
        """,
        """
                ------;
                |     O
                |    \|/
                |     |
                |    / \ 
        """
        ]

# get word length
while True:
    word_length = input('Word Length? Please pick a number less than 10. Answer:  ')
    try:
        if int(word_length) <= 9:
            break
        else:
            print("Please pick a number less than 10")
    except ValueError:
        print("'" + str(word_length) + "' is not a valid input")

word_length = int(word_length)

# get word
print("Selecting a word...")


def get_word(word_length):
    word = []
    file = open("wordlist.txt", 'r')
    for line in file:
        if len(line.strip()) == word_length:
            word.append(line)
        else:
            continue
    h = random.randint(0, len(word))
    return word[h]


word = (get_word(word_length))
non_duplicate_letters_in_word = []
correct_guesses = []
incorrect_guesses = []
attempts = 6
# make a list with letters in word
for i in range(len(word)):
    if word[i] not in non_duplicate_letters_in_word:
        non_duplicate_letters_in_word.append(word[i])


while attempts != 0:
    print("Word: ", end="")
    for k in range(len(word) - 1):
        if word[k] in correct_guesses:
            print(word[k], end="")
        else:
            print("-", end="")
    print(man[attempts])
    letter = input("Guess A Letter: ").lower()
    # check if all input is alphabetical
    if letter.isalpha() is False or len(letter) != 1:
        print("Not a single letter. Please try again.")
    elif letter in correct_guesses or letter in incorrect_guesses:
        print("'" + letter + "' was already guessed. Try again")
    elif letter in word:
        correct_guesses.append(letter)
        print("Correct!")
        if len(correct_guesses) == (len(non_duplicate_letters_in_word) - 1):
            print("You Won! The word was " + word)
            break
    else:
        attempts -= 1
        incorrect_guesses.append(letter)
        print(" '" + letter + "' is not in the word")
    print("You have " + str(attempts) + " attempts left.")

if attempts == 0:
    print("Sorry, you lost! The word was " + word)
