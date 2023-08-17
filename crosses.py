play_field = [[" " for row in range(3)] for column in range(3)]# initial of play field matrix

game_term = True # the term of infinite "while" loop in "game_core" func

count = 0 # counter of all turn iteration, the term of infinite "while" loop in "game_core" func

# coordinates of all possible winning_variants for comparing with the current play_field state
winning_variants = [[(1, 1), (2, 2), (3, 3)],
                    [(1, 3), (2, 2), (3, 1)],
                    [(1, 1), (1, 2), (1, 3)],
                    [(2, 1), (2, 2), (2, 3)],
                    [(3, 1), (3, 2), (3, 3)],
                    [(1, 1), (2, 1), (3, 1)],
                    [(1, 2), (2, 2), (3, 2)],
                    [(1, 3), (2, 3), (3, 3)]]


# function that searching "win" vector combination in play_field matrix
def get_win_row(*args):
    win_row = []
    for i in args:
        for a, b in i:
            win_row.append(play_field[a-1][b-1])
    if win_row == ['0', '0', '0']:
        rendering_play_field(play_field)
        print(f"Player 1 WINS by coordinates: {i}")
    elif win_row == ['x', 'x', 'x']:
        rendering_play_field(play_field)
        print(f"Player 2 WINS by coordinates: {i} ")
        return False
    else:
        return True

#  function that run "get_win_row" function with the parameters from "winning_variants" list
#  and change the global "game_term" variable on False if the winning combination has found
def check_on_win():
    for item in winning_variants:
         if not get_win_row(item):
            global game_term
            game_term = False
            break

# function re-rendering the current state of "play_field" matrix
def rendering_play_field(some_field):
    some = 0
    print('   1    2    3')
    for i in some_field:
        some += 1
        print(f'{some} {i}', end='\n')


# functions that checking "current_coordinates" in 3 terms:
# 1,2) a and b coordinates belongs to range of matrix; 3) place is not taken by "0" or "X"
def chk_current_coordinates(*some_coordinates):
    for a, b in some_coordinates:
        if 0 <= a <= 2 and 0 <= b <= 2 and play_field[a][b] == ' ':
            return True
        else:
            return False



# function that shifting coordinates taken from player by "-1" value
# to return the correct coordinates for matrix
def correcting_coordinates(*args):
    for a, b in args:
        a, b = a-1, b-1
    return [a, b]


# function for putting Player 1 coordinates in matrix
def put_in_current_coordinates_0(*args):
    for x, y in args:
        play_field[x][y] = '0'

# function for putting Player 2 coordinates in matrix
def put_in_current_coordinates_x(*args):
    for x, y in args:
        play_field[x][y] = 'x'

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
# function is checking is possible type elements of "raw_input" list equal to integer
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# The Main function
def game_core(field):
                                                       # players turn counter
    current_coordinates = ()
    print('WELLCOME TO THE GAME')
    global count
    while game_term and count < 9:                                            # initiating the infinite loop on "game_term" variable

        rendering_play_field(field)

        if not count % 2:
            print(f'player 1 input coordinates:')
        else:
            print(f'player 2 input coordinates:')

        raw_input = input().split(' ')
        if len(raw_input) == 2 and isInt(raw_input[0]) and isInt(raw_input[-1]):# special term for raw_data must be list consist of two integer elements
            current_coordinates = tuple(map(int, raw_input)) # data type casting of current coordinates to the tuple of integers
            current_coordinates = correcting_coordinates(current_coordinates) # correcting by "-1"

            if chk_current_coordinates(current_coordinates): # validation check of current coordinates
                if not count % 2:
                    put_in_current_coordinates_0(current_coordinates)
                    check_on_win()
                    count += 1
                else:
                    put_in_current_coordinates_x(current_coordinates)
                    check_on_win()
                    count += 1
        else:
            print('NoN correct coordinates PLEASE input AGAIN!!!')
            pass
    print('GAME OVER!!!')
    if count == 9:
        print("ITS DRAW: NOBODY WINS TRY AGAIN")
    print('HAVE A GOOD DAY!!!')

game_core(play_field)
