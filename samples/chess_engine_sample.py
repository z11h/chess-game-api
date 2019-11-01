import chess  # see documentation at https://python-chess.readthedocs.io/en/latest/

# instantiates "Board" object
print("~ Chess Board ~")
board = chess.Board()

# Printing off starting board
print(board, "\n")

# Moves performing a "Scholar's mate", showing steps along the way
board.push_san("e4")
print(board, "\n")
board.push_san("e5")
print(board, "\n")
board.push_san("Qh5")
print(board, "\n")
board.push_san("Nc6")
print(board, "\n")
board.push_san("Bc4")
print(board, "\n")
board.push_san("Nf6")
print(board, "\n")
board.push_san("Qxf7")

print("~ Final Board with Checkmate ~")
print(board, "\n")

print("Player in check?", board.is_check())
print("Player in checkmate?", board.is_checkmate())


