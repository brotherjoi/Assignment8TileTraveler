# 1. Player starts in tile 1.1
# 2. We check where the player can move and tell him what directions he can go
# 3. If the player inputs an invalid direction, his position does not change
# 4. If he inputs a valid direction, we change his postition and repeat step 2
# 5. Repeat until player reaches the winning position at 3.1

# https://github.com/brotherjoi/Assignment8TileTraveler

def possible_movements(player_x_pos, player_y_pos):
    player_pos_str = str(player_x_pos) + " " + str(player_y_pos)
    north_bool = False
    east_bool = False
    south_bool = False
    west_bool = False
    direction_count = 0

    print("You can travel:", end = "")
    if player_y_pos != 3 and player_pos_str != "2 2":
        print(" (N)orth", end = "")
        north_bool = True
        direction_count += 1
    if player_x_pos != 3 and (player_pos_str != "1 1" and player_pos_str != "2 2" and player_pos_str != "2 1"):
        if direction_count > 0:
            print(" or (E)ast", end = "")
        else:
            print(" (E)ast", end = "")
        east_bool = True
        direction_count += 1
    if player_y_pos != 1 and player_pos_str != "2 3":
        if direction_count > 0:
            print(" or (S)outh", end = "")
        else:
            print(" (S)outh", end = "")
        south_bool = True
        direction_count += 1
    if player_x_pos != 1 and (player_pos_str != "2 1" and player_pos_str != "3 2" and player_pos_str != "3 1"):
        if direction_count > 0:
            print(" or (W)est", end = "")
        else:
            print(" (W)est", end = "")
        west_bool = True
    print(".")
    
    return north_bool, east_bool, south_bool, west_bool


def player_move(player_x_pos, player_y_pos, north_bool, east_bool, south_bool, west_bool):
    x_check, y_check = player_x_pos, player_y_pos
    while player_x_pos == x_check and player_y_pos == y_check:
            player_direction_str = input("Direction: ")
            player_direction_str = player_direction_str.lower()
            if player_direction_str == "n":
                if north_bool == True:
                    player_y_pos += 1
                else:
                    print("Not a valid direction!")
            elif player_direction_str == "e":
                if east_bool == True:
                    player_x_pos += 1
                else:
                    print("Not a valid direction!")
            elif player_direction_str == "s":
                if south_bool == True:
                    player_y_pos -= 1
                else:
                    print("Not a valid direction!")
            elif player_direction_str == "w":
                if west_bool == True:
                    player_x_pos -= 1
                else:
                    print("Not a valid direction!")
            else:
                print("Not a valid direction!")
    return player_x_pos, player_y_pos
    

player_x_pos = 1
player_y_pos = 1


while player_x_pos != 3 or player_y_pos != 1:
    north_bool, east_bool, south_bool, west_bool = possible_movements(player_x_pos, player_y_pos)

    player_x_pos, player_y_pos = player_move(player_x_pos, player_y_pos, north_bool, east_bool, south_bool, west_bool)
    

    
print("Victory!")