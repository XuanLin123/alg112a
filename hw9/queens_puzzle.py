def is_safe(board, row, col, n):
    # 檢查列上是否有皇后
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # 如果已經成功放置了 n 個皇后，將解加入結果中
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)

def solve_n_queens(n):
    board = [-1] * n  # 棋盤初始化，每個元素表示一行中皇后的列索引
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if col == row else "." for col in range(len(board))]))

# 解決八皇后問題
solutions = solve_n_queens(8)

# 輸出所有解
for solution in solutions:
    print_solution(solution)
    print("\n")
