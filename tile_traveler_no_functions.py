# 1. Player starts in tile 1.1
# 2. We check where the player can move and tell him what directions he can go
# 3. If the player inputs an invalid direction, his position does not change
# 4. If he inputs a valid direction, we change his postition and repeat step 2
# 5. Repeat until player reaches the winning position at 3.1

player_x_pos = 1
player_y_pos = 1

while player_x_pos != 3 or player_y_pos != 1:
    player_pos_str = str(player_x_pos) + " " + str(player_y_pos)

    print("You can travel:", end = " ")
    if player_y_pos != 3 and player_pos_str != "2 2":
        print("(N)orth", end = " ")
    if player_x_pos != 3 and (player_pos_str != "1 1" or player_pos_str != "2 2" or player_pos_str != "2 1"):
        print("(E)ast", end = " ")
    if player_y_pos != 1 and player_pos_str != "2 3":
        print("(S)outh", end = " ")
    if player_x_pos != 1 and (player_pos_str != "2 1" or player_pos_str != "3 2" or player_pos_str != "3 1"):
        print("(W)est", end = " ")

    player_direction_str = input("Where you wanna go? ")
    if player_direction_str == "n":
        player_y_pos += 1
    elif player_direction_str == "e":
        player_x_pos += 1
    elif player_direction_str == "s":
        player_y_pos -= 1
    elif player_direction_str == "w":
        player_x_pos -= 1
    else:
        print("Invalid input")
    print(player_x_pos, player_y_pos)
