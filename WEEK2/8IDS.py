
def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} {board[i+1]} {board[i+2]} ")
    print("-" * 11)

def get_moves(board):
    moves = []
    empty_idx = board.index(0)  
    row = empty_idx // 3
    col = empty_idx % 3

    
    directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    for dr, dc, name in directions:
        new_row = row + dr
        new_col = col + dc
        
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            
            new_board = list(board)
            new_board[empty_idx], new_board[new_idx] = new_board[new_idx], new_board[empty_idx]
            moves.append((new_board, name))
            
    return moves

visited = set()

def solve_dfs(start, goal, max_depth=15):
    stack = [(start, [])]

    while stack:
        current_board, path = stack.pop()

        if current_board == goal:
            return path

        if len(path) >= max_depth:
            continue

        board_tuple = tuple(current_board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        for next_board, move_direction in get_moves(current_board):
            new_path = path + [move_direction]
            stack.append((next_board, new_path))

    return None 

start_board = [1, 2, 3, 
               4, 0, 5, 
               7, 8, 6]

goal_board  = [1, 2, 3, 
               4, 5, 6, 
               7, 8, 0]

print("Starting Board:")
print_board(start_board)

solution = solve_dfs(start_board, goal_board, max_depth=15)

if solution:
    print("8 Puzzle using IDS ---\n")
    print(f"Success! Steps to solve:")
    for move in solution:
        print(f"Move blank to: {move}")
else:
    print("Could not find a solution within the depth limit.")

