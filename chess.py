def isValidChessBoard(board):
    valid_positions = {str(row) + col for row in range(1, 9) for col in 'abcdefgh'}
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    piece_count = {'w': {'king': 0, 'pieces': 0, 'pawns': 0}, 'b': {'king': 0, 'pieces': 0, 'pawns': 0}}

    for pos, piece in board.items():
        if pos not in valid_positions:
            return False  # Invalid position
        
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            return False  # Invalid piece name
        
        color, piece_type = piece[0], piece[1:]
        piece_count[color]['pieces'] += 1
        if piece_type == 'king':
            piece_count[color]['king'] += 1
        if piece_type == 'pawn':
            piece_count[color]['pawns'] += 1
    
    # Check constraints
    if piece_count['w']['king'] != 1 or piece_count['b']['king'] != 1:
        return False
    if piece_count['w']['pieces'] > 16 or piece_count['b']['pieces'] > 16:
        return False
    if piece_count['w']['pawns'] > 8 or piece_count['b']['pawns'] > 8:
        return False
    
    return True

# Example usage
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_board))  # Output: True
