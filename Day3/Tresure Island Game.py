# prompt design of the game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


# prompt instruction for the user
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
game_play = "true"

# while loop to keep the game running
while (game_play):
    direction_input = input('You are on the road where do you want to go? Type "left" or "right"\n')
    direction = direction_input.lower() # change the user input into lowercase
    if direction == "right":
        print("Wrong Direction, you failed")
        start = input('Do you want to start the game. Enter "yes" or "no"\n')
        if start =="no":
            print("Game Over")
            break # end the game break out of the loop
    elif direction == "left":
        cross_input = input('You come to a lake. There is an island in the middle of the lake, '
                            'type "wait" to wait for the boat or "swim" to swim to the island \n')
        cross = cross_input.lower()
        if cross == "swim":
            print("Crocodiles eat you, you failed")
            start = input('Do you want to start the game. Enter "yes" or "no"\n')
            if start == "no":
                print("Game Over")
                break
        elif cross == "wait":
            door_choice_input = input('You arrive to the island unharmed. There is a house with three doors. \n'
                                      'one red, one yellow, one blue. which one do you choose. Enter "red" for red door, '
                                      '"yellow" for yellow door, "blue" for blue door \n')
            door_choice = door_choice_input.lower()
            if door_choice == "red":
                print("There's fire in that room, you failed")
                start = input('Do you want to start the game again. Enter "yes" or "no"\n')
                if start == "no":
                    print("Game Over")
                    break
            elif door_choice == "blue":
                print("Congratulations, you found the treasure")
                print("Game Over")
                break
            elif door_choice == "yellow":
                print("There's wild animals in that room, you failed")
                start = input('Do you want to start the game again. Enter "yes" or "no"\n')
                if start == "no":
                    print("Game Over")
                    break
            else: # else for the third if condition for door_choice, if unwanted or wrong input is entered
                print("Wrong input entered.")
                start = input('Do you want to start the game again. Enter "yes" or "no"\n')
                if start == "no":
                    print("Game Over")
                    break
        else: # else for the second if condition for cross, if unwanted or wrong input is entered
            print("Wrong input entered.")
            start = input('Do you want to start the game again. Enter "yes" or "no"\n')
            if start == "no":
                print("Game Over")
                break
    else: # else for the first if condition for direction, if unwanted or wrong input is entered
        print("Wrong input entered.")
        start = input('Do you want to start the game again. Enter "yes" or "no"\n')
        if start == "no":
            print("Game Over")
            break
