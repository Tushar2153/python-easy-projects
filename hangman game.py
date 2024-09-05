import random
word_list=["apple","beautiful","potato"]#list of words

lives=6

chosen_word=random.choice(word_list)
print(chosen_word)

display=[]

for letter in chosen_word:
    display += '_'#display blank space for each letter
print(display)

game_over=False

while not game_over:
    guess=input("guess a letter").lower()

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=guess

    print(display)

    if guess not in chosen_word:
        lives -= 1 
        
        if lives == 0:
            game_over=True
            print ("you lose")

    if '_' not in display:
        game_over = True
        print("you win")
    
          



    