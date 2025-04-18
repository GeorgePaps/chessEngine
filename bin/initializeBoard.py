
def initializeBoard():
    """
    Creates the initial chess board as a list of lists.

    Args:

    Returns:
        board (list): A 2D list representing the chess board, where each element is a string.
        The first row contains the white pieces, the second row contains the white pawns,
        the last two rows contain the black pawns and pieces respectively.
        The white pieces are represented by lowercase letters and the black pieces by uppercase letters.
        The empty squares are represented by 0.
    """

    # Initialize the chess board with empty squares represented by 0
    # The board is an 8x8 grid, so we create a list of lists with 8 rows and 8 columns
    board = [[0 for _ in range(8)] for _ in range(8)]

    # Place the white pieces on the first row
    board[0][0] = 'r'  # Rook
    board[0][1] = 'n'  # Knight
    board[0][2] = 'b'  # Bishop
    board[0][3] = 'q'  # Queen
    board[0][4] = 'k'  # King
    board[0][5] = 'b'  # Bishop
    board[0][6] = 'n'  # Knight
    board[0][7] = 'r'  # Rook

    # Place the white pawns on the second row
    board[1] = ['p' for _ in range(8)]  # Pawns  
    
    # Place the black pawns on the seventh row
    board[6] = ['P' for _ in range(8)]  # Pawns 

    # Place the black pieces on the eighth row
    board[7][0] = 'R'  # Rook
    board[7][1] = 'N'  # Knight
    board[7][2] = 'B'  # Bishop
    board[7][3] = 'Q'  # Queen
    board[7][4] = 'K'  # King
    board[7][5] = 'B'  # Bishop
    board[7][6] = 'N'  # Knight
    board[7][7] = 'R'  # Rook 

    return board

