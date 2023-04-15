import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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
logo = logo = '''
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                   
                                                                 
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

live = 6

display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:  ").lower()
    if guess in display:
        print(f"You have guess {guess} again")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] =letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, you lose a life!")
        live -= 1
        if live == 0:
            end_of_game = True
            print("Game Over")
   
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!!")
       
    print(stages[live])    
print(chosen_word)
