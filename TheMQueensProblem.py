def queen(board_size, queen_count):
    
    def place_queens(num_placed, current_row):
        if num_placed == queen_count:
            solution_counter[0] += 1
            return
        if current_row >= board_size:
            return
        for current_col in range(board_size):
            if is_position_safe(current_row, current_col):
                chessboard[current_row][current_col] = 1
                rows_under_attack.add(current_row)
                cols_under_attack.add(current_col)
                diagonals_under_attack.add(current_row - current_col)
                anti_diagonals_under_attack.add(current_row + current_col)
                place_queens(num_placed + 1, current_row + 1)
                chessboard[current_row][current_col] = 0
                rows_under_attack.remove(current_row)
                cols_under_attack.remove(current_col)
                diagonals_under_attack.remove(current_row - current_col)
                anti_diagonals_under_attack.remove(current_row + current_col)
        place_queens(num_placed, current_row + 1)
        #we need to maks sure the scope of the position
    
    def is_position_safe(row, col):
        return (row not in rows_under_attack and
                col not in cols_under_attack and
                row - col not in diagonals_under_attack and
                row + col not in anti_diagonals_under_attack)
    solution_counter = [0]
    chessboard = [[0] * board_size for _ in range(board_size)]
    rows_under_attack = set()
    cols_under_attack = set()
    diagonals_under_attack = set()
    anti_diagonals_under_attack = set()
    place_queens(0, 0)
    return solution_counter[0]

if __name__ == "__main__":
    print(queen(4, 4))  # 2
    print(queen(4, 2))  # 44
    print(queen(6, 4))  # 982
    print(queen(7, 2))  # 700
    print(queen(8, 8))  # 92