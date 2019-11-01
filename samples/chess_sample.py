# for alphabet
from string import ascii_uppercase

# Filling chessboard with labels
labels_chessboard = [ [],[],[],[],[],[],[],[] ]
index = 0
label_index = 8
# loop thru each c of r with strings made of ascii/num value
for row in labels_chessboard:
    index = 0
    for col in range(8):
        label = ""
        label += ascii_uppercase[index]
        label += str(label_index)
        row.append(label)
        index += 1
    label_index -= 1

# making a 2D array for chessboard with pieces
chessboard = [ [],[],[],[],[],[],[],[] ]
# first row - royalty (black)
chessboard[0] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
# second row - pawns (black)
for c in range(8):
    chessboard[1].append("P")
# third - sixth row - empty
for r in range(2,6):
    for c in range (8):
        chessboard[r].append(".")
# seventh row - pawns (white)
for c in range(8):
    chessboard[6].append("p")
# eighth row - royalty (white)
chessboard[7] = ["r", "n", "b", "q", "k", "b", "n", "r"]

# Loop continues until exit conditional is met, similar to do/while in other languages
while True:
    print("\n============= Chess board: =============\n")
    # printing chessboard 2D array
    for r in chessboard:
        print(r)
    # starting user prompts
    answer = input("\nWould you like to make a move? [Y] = yes [N] = no: ")
    if answer == "Y":
        starting = input("Please enter starting position chess notation format"
                         "\n OR enter '?' to see notation key:  ")
        # prints chess notation 2D array
        if(starting == "?"):
            for row in labels_chessboard:
                print(row)
            starting = input("Now that you know, which piece do you want to move? (chess notation): ")
        ending = input("Please enter space for landing destination of piece:  ")
        # Exit conditional
    elif answer == "N":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, answer cannot be understood. Please rerun the program and type 'Y' or 'N' next time")
        break

    # Searches for notation table for index of notation input, switches same indices of actual chess board
    # Starting position
    for r in labels_chessboard:
        for c in r:
            if (c == starting):
                x1 = labels_chessboard.index(r)
                y1 = r.index(c)
    # Ending position
    for r in labels_chessboard:
        for c in r:
            if (c == ending):
                x2 = labels_chessboard.index(r)
                y2 = r.index(c)

    # Selects piece with correct indices, replaces piece
    piece_selected = chessboard[x1][y1]
    if (piece_selected == "."):
        print("You chose an empty space, run the program again.")
        break
    # Replaces old position with period (empty space)
    chessboard[x1][y1] = "."
    # Moves old piece to new position, replaces whatever was there
    chessboard[x2][y2] = piece_selected