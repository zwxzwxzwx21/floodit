import random
import random
import copy
def create_board(size, colors):
    return [[random.choice(colors) for _ in range(size)] for _ in range(size)]

def flood_fill(board, x, y, target_color, new_color):
    # Implement flood-fill logic here
    pass

def is_game_over(board):
    return all(cell == board[0][0] for row in board for cell in row)

# Create random board for AI to play on
size = 6
colors = ["red","yellow","green","orange","purple","cyan","blue","pink"]

color_LUT = {
    "red": 'R',
    "yellow": 'Y',
    "green": 'G',
    "orange": 'O',
    "purple": 'P',
    "cyan": 'C',
    "blue": 'B',
    "pink": 'I',
}
colors_array = ["r","y","g","b","o","p","c","i"]
board = None
#main loop
position_of_group = [(0,0)]
real_pos_array = []
'''board_transformed =[['Y', 'Y', 'Y', 'Y', 'O', 'Y'],
                    ['C', 'Y', 'G', 'Y', 'Y', 'Y'],
                    ['R', 'P', 'C', 'G', 'Y', 'Y'],
                    ['O', 'G', 'Y', 'R', 'Y', 'O'],
                    ['G', 'Y', 'Y', 'Y', 'Y', 'Y'],
                    ['Y', 'Y', 'G', 'Y', 'I', 'Y']]'''
board = create_board(size, colors)
board_transformed = [[color_LUT[(color)] for color in row] for row in board]
def flood_it_logic(board_transformed,pos_array,number_of_moves):
    number_of_moves += 1
    print("loop started")


    #determining positions of current connected colors
    new_color = True # loop arg to check for new color
    board_transformed_copy = copy.deepcopy(board_transformed)
    current_color = board_transformed_copy[0][0]
    while new_color:
        print('position of group:', pos_array)
        new_color = False
        temp_array = [] # for adding positions and printing them
        for position in pos_array:
            print('checking position',position,'lenght of group',len(pos_array))
            print('checking for board')
            for row in board_transformed_copy:
                print(row)
            #make if statement so it wont go negative and over size
            if position[1] + 1 < size:
                print('pos 1 + 1',board_transformed_copy[position[1]+1][position[0]])
                if board_transformed_copy[position[1]+1][position[0]] == current_color:
                    pos = (position[0],position[1]+1) # x,y
                    board_transformed_copy[position[1]+1][position[0]] = 'X'
                    temp_array.append(pos)
                    print('found position: y+1',pos )
                    new_color = True
            if position[0] + 1 < size:
                if board_transformed_copy[position[1]][position[0]+1] == current_color:
                    pos = (position[0]+1,position[1]) # x,y
                    board_transformed_copy[position[1] ][position[0]+1] = 'X'
                    temp_array.append(pos)
                    print('found position: x+1', pos)
                    new_color = True
            if position[1] - 1 > -1:
                if board_transformed_copy[position[1]-1][position[0]] == current_color:
                    pos = (position[0],position[1]-1) # x,y
                    board_transformed_copy[position[1]-1][position[0]] = 'X'
                    temp_array.append(pos)
                    print('found position: y-1', pos)
                    new_color = True
            if position[0] - 1 > -1:
                if board_transformed_copy[position[1]][position[0]-1] == current_color:
                    pos = (position[0]-1,position[1]) # x,y
                    board_transformed_copy[position[1]][position[0] - 1] = 'X'
                    temp_array.append(pos)
                    print('found position: x+1', pos)
                    new_color = True
        for pos in temp_array:
            if pos not in pos_array:
                pos_array.append(pos)
        print(real_pos_array, "real pos array")
        for pos in  pos_array:
            if pos not in real_pos_array:
                print('appending',pos)
                real_pos_array.append(pos)
        #pos_array = copy.deepcopy(temp_array)
        board_transformed_copy[0][0] = 'X'
        print('board transformed copy')
        if is_game_over(board_transformed_copy):
            print('###############################################')
            print(f'victory! you won in {number_of_moves} moves!'); break
            print('###############################################')
        for row in board_transformed_copy:
            print(row)
        print(new_color, 'new color')
    print("leaving loop")
    print(real_pos_array)



    #printing boards
    #region
    ''' for row in board:
        print(row)'''
    '''for row in board_transformed:
        print(row)'''
    #endregion

    user_input = input("Enter your move: ")
    if user_input in color_LUT:
        for position in real_pos_array:
            print("changed position",position)
            for row in board_transformed_copy:
                print(row)
            board_transformed_copy[position[1]][position[0]] = color_LUT[user_input]
        print("changing to", color_LUT[user_input])
        board_transformed = copy.deepcopy(board_transformed_copy)
        flood_it_logic(board_transformed, real_pos_array,number_of_moves)
    else: print("something is wrong")

flood_it_logic(board_transformed, position_of_group,0)


