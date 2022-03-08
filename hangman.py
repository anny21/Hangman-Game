import random

word_list = ["happy", "friend", "mediawiki", "hangman"]
chosen_word = random.choice(word_list)

print(f'The right word is {chosen_word}.')

display = list()

for _ in range(len(chosen_word)):
    display += "_"

word = len(chosen_word)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower().replace(" ", "")

    found = guess in display
    if found:
        print(f"already entered {guess} before")
    else:
        word = word - 1
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            # if display[position] == letter:
            #   abs(n)word = word - 1
            if letter == guess:
                display[position] = letter

        print(display)
        print(word)
    check = '_' not in display
    if check:
        end_of_game = True
        print("game over")
        print("you won")
    if word == 0:
        end_of_game = True
        print("game over")
        print("you lost")

    # else:
    # print("Wrong")
