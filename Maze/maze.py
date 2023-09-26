def solve_maze(maze, start, end):
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

            # Movimento para cima
            if dfs(x - 1, y):
                return True
            # Movimento para baixo
            if dfs(x + 1, y):
                return True
            # Movimento para a esquerda
            if dfs(x, y - 1):
                return True
            # Movimento para a direita
            if dfs(x, y + 1):
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
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

solution = solve_maze(maze, start, end)

if solution:
    print("Labirinto resolvido:")
    print_maze(solution)
else:
    print("Não há solução para o labirinto.")
