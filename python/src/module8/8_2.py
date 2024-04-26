def read_board():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    return N, board


def find_pos(board, symbol):
    pos = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == symbol:
                pos.append((i, j))
    return pos


def is_valid(board, visited, pos):
    i, j = pos
    N = len(board)
    return ((0 <= i < N) and (0 <= j < N) and (board[i][j] != '#') and (not visited[i][j]))


def BFS(board, start, end):
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    queue = [(start, [start])]
    visited[start[0]][start[1]] = True

    while queue:
        pos, path = queue.pop(0)
        if pos == end:
            return path

        for di, dj in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            ni, nj = pos[0] + di, pos[1] + dj
            if is_valid(board, visited, (ni, nj)):
                visited[ni][nj] = True
                queue.append(((ni, nj), path + [(ni, nj)]))

    return None


def mark_path(board, path):
    for i, j in path:
        board[i][j] = '@'


def print_board(board):
    for row in board:
        print(''.join(row))


def solve_path(board, start_symbol, end_symbol):
    start, end = find_pos(board, start_symbol)

    path = BFS(board, start, end)

    if path is None:
        print("Impossible")
    else:
        mark_path(board, path)
        print_board(board)


N, board = read_board()
solve_path(board, '@', '@')
