class Puzzle15:
    def __init__(self, initial_state):
        self.initial_state = initial_state  # Define o estado inicial do quebra-cabeça.
        self.goal_state = list(range(1, 16)) + [0]  # Define o estado objetivo (resolvido).
        self.open_set = []  # Inicializa a lista de estados abertos.
        self.closed_set = set()  # Inicializa o conjunto de estados fechados.

    def solve(self):
        self.open_set.append((self.initial_state, []))  # Adiciona o estado inicial à lista de estados abertos.

        while self.open_set:
            current_state, path = self.open_set.pop(0)  # Pega o estado atual e o caminho até ele.
            self.closed_set.add(tuple(current_state))  # Adiciona o estado atual ao conjunto de estados fechados.

            zero_index = current_state.index(0)  # Encontra a posição do espaço vazio.
            moves = self.valid_moves(zero_index)  # Encontra os movimentos válidos a partir dessa posição.

            for move in moves:
                new_state = current_state[:]
                new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
                if tuple(new_state) not in self.closed_set:
                    new_path = path + [new_state]  # Atualiza o caminho com o novo estado.
                    self.open_set.append((new_state, new_path))  # Adiciona o novo estado à lista de estados abertos.
                    self.open_set.sort(key=lambda x: self.heuristic(x[0]) + len(x[1]))  # Ordena a lista de estados abertos por uma função heurística.

            if current_state == self.goal_state:
                self.print_solution(current_state)  # Se encontramos o estado objetivo, imprime a solução.

    def valid_moves(self, zero_index):
        moves = []
        if zero_index % 4 > 0:
            moves.append(zero_index - 1)
        if zero_index % 4 < 3:
            moves.append(zero_index + 1)
        if zero_index >= 4:
            moves.append(zero_index - 4)
        if zero_index < 12:
            moves.append(zero_index + 4)
        return moves

    def heuristic(self, state):
        distance = 0
        for i in range(16):
            if state[i] != 0:
                goal_row, goal_col = divmod(state[i] - 1, 4)
                current_row, current_col = divmod(i, 4)
                distance += abs(goal_row - current_row) + abs(goal_col - current_col)
        return distance

    def print_solution(self, state):
        print("Solução Final:")
        self.print_board(state)  # Imprime a solução final.

    def print_board(self, state):
        for i in range(0, 16, 4):
            print(state[i:i + 4])  # Imprime o estado do tabuleiro em linhas de 4 peças.

if __name__ == "__main__":
    initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12]  # Define o estado inicial do quebra-cabeça.
    puzzle = Puzzle15(initial_state)
    puzzle.solve()  # Chama o método para resolver o quebra-cabeça.