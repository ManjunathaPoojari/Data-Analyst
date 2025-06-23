def block_win(pos1, pos2):
    board = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for line in board:
        if pos1 in line and pos2 in line:
            for pos in line:
                if pos != pos1 and pos != pos2:
                    return pos
    return None
