def solve_maze(maze, start, end):
    # Função para calcular a distância de Manhattan entre dois pontos.
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    # Função para verificar se um movimento (x, y) é válido.
    def is_valid_move(x, y):
        # Verifica se a posição (x, y) está dentro dos limites do labirinto,
        # não é uma parede (representada por 1) e ainda não foi visitada.
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            return True
        return False

    # Função de busca em profundidade (DFS) para encontrar um caminho no labirinto.
    def dfs(x, y):
        # Verifica se chegamos ao ponto de destino.
        if x == end[0] and y == end[1]:
            return True
        
        if is_valid_move(x, y):
            maze[x][y] = 2  # Marca o caminho como visitado (2).

            # Cálculo da distância de Manhattan para os movimentos possíveis.
            moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            moves.sort(key=lambda move: manhattan_distance(move[0], move[1], end[0], end[1]))

            for move_x, move_y in moves:
                if dfs(move_x, move_y):
                    return True

            maze[x][y] = 0  # Desmarca o caminho se não levar à solução.
            return False

    if dfs(start[0], start[1]):
        return maze  # Retorna o labirinto com o caminho encontrado.
    else:
        return None  # Retorna None se não houver solução para o labirinto.

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

# Exemplo de uso:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0]
]

start = (0, 0)
end = (4, 4)

solution = solve_maze(maze, start, end)

if solution:
    print("Labirinto resolvido:")
    print_maze(solution)
else:
    print("Não há solução para o labirinto.")