def solve_maze(maze, start, end):
    def is_valid_move(x, y):
        # Verifica se um movimento (x, y) é válido.
        # Um movimento é válido se a posição (x, y) está dentro dos limites do labirinto,
        # não é uma parede (representada por 1) e ainda não foi visitada.
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            return True
        return False

    def heuristic(x, y):
        # Função heurística que calcula a distância de Manhattan (L1) da posição (x, y) até o destino.
        return abs(x - end[0]) + abs(y - end[1])

    open_list = [(start[0], start[1], 0, heuristic(start[0], start[1]))]
    closed_set = set()
    came_from = {}  # Inicializa o dicionário came_from para armazenar os ponteiros dos pais.

    while open_list:
        x, y, cost, est_cost = min(open_list, key=lambda item: item[3])
        open_list.remove((x, y, cost, est_cost))

        if (x, y) == end:
            # Reconstrói o caminho
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = came_from[(x, y)]
            path.append(start)
            path.reverse()
            
            # Marca o caminho no labirinto com 'X'
            for px, py in path:
                maze[px][py] = 2
            
            return maze

        closed_set.add((x, y))

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x, new_y = x + dx, y + dy

            if not is_valid_move(new_x, new_y) or (new_x, new_y) in closed_set:
                continue

            new_cost = cost + 1
            new_est_cost = new_cost + heuristic(new_x, new_y)

            if (new_x, new_y) not in [(item[0], item[1]) for item in open_list] or new_cost < cost:
                open_list.append((new_x, new_y, new_cost, new_est_cost))
                came_from[(new_x, new_y)] = (x, y)

    return None

def print_maze(maze):
    # Função para imprimir o labirinto de forma legível.
    for row in maze:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")  # Caminho livre
            elif cell == 1:
                print("█", end=" ")  # Parede
            elif cell == 2:
                print("X", end=" ")  # Caminho encontrado
        print()

# Labirinto de exemplo 4x5
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0]
]

start = (0, 0)
end = (3, 4)

# Chama a função para resolver o labirinto
solution = solve_maze(maze, start, end)

# Exibe o resultado
if solution:
    print("Labirinto resolvido:")
    print_maze(solution)
else:
    print("Não há solução para o labirinto.")
