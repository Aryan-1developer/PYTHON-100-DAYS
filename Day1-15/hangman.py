import random
stage = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["cat", "dog", "fish", "book", "tree", "apple"]
random_word = random.choice(words)
print(random_word)
word_length = len(random_word)
display = ["_"] * word_length
lives = 6

print("Welcome to Hangman!")
print(" ".join(display))

while "_" in display and lives > 0:
    guess = input("enter an alphabet of your choice:").lower()
    if guess in random_word:
        for position in range(word_length):
            if random_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    elif guess in display:
        print(f"You have already guessed the letter '{guess}'. Try a different letter.")
    else:
        lives -= 1
        print("Wrong guess!")
        print(f"The no of life left is {lives}")
        print(stage[lives])
        
    print(" ".join(display))

if "_" not in display:
    print("Congratulations! You guessed the word correctly.")
else:
    print(stage[0])
    print(f"You have run out of the life.Game over! The word was '{random_word}'.")

