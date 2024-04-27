from collections import deque

def bfs(grid, start_row, start_col, door_row, door_col):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col, 0)])
    
    while queue:
        row, col, ladder_size = queue.popleft()
        
        if row == door_row and col == door_col:
            return ladder_size
        
        visited.add((row, col))
        
        # Move horizontally
        for dr, dc in [(0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 'X' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, ladder_size))
        
        # Move vertically using ladder
        for dr in range(-ladder_size, ladder_size + 1):
            new_row = row + dr
            if 0 <= new_row < n and grid[new_row][col] == 'X' and (new_row, col) not in visited:
                queue.append((new_row, col, ladder_size + 1))
    
    return -1

def minimum_ladder_size(N, M, R, V, grid):
    door_row, door_col = R - 1, V - 1
    return bfs(grid, N - 1, door_col, door_row, door_col)


def main():
    # Lectura de la entrada
    N, M = map(int, input().split())
    R, V = map(int, input().split())
    grid = [input() for _ in range(N)]

    # Calcula y muestra el tamaño mínimo de la escalera necesario
    print(minimum_ladder_size(N, M, R, V, grid))


main()