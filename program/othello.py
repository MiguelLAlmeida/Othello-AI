import math
import copy
import time

class Othello:
    def __init__(self):
        self.W = 'W'
        self.B = 'B'
        self.EMPTY = None
        
        self.board = [
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.W,     self.B,     self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.B,     self.W,     self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY]
        ]
        self.playing = self.B
        
    def player(self, board):
        #Retorna apenas o jogador que está jogando
        return self.playing
    
    def change_turn(self, board):
        #Método criado para decidir qual o proximo jogador
        #Verifica se o possível próximo jogador tem uma lista de possíveis ações diferente de vazia
        #Caso tenha, o próximo jogador é setado como o possível próximo jogador
        #Caso não tenha, retorna como próximo jogador o atual jogador
        oponente = self.W if self.playing == self.B else self.B
        jogador_anterior = self.playing
        
        self.playing = oponente
        
        if len(self.actions(board)) == 0:
            self.playing = jogador_anterior
            
    def actions(self, board):
        #Determina as jogadas possíveis do atual jogador através da analise completa de todas as casas do tabuleiro que correspondem ao jogador atual
        #Quando encontra uma peça do jogador atual, olha nas 8 casas ao seu redor para encontrar peças inimigas
        #Caso encontre, percorre a linha em que a peça inimiga está, até encontrar uma peça vazia para preencher uma linha ou o final do tabuleiro
        #Armazena todas essas possíveis casas em que o jogador atual pode inserir uma peça para preencher uma linha 
        #Retorna a lista de possíveis ações para a chamada do código
        actions_possibles = set()
        lenrow = len(board)
        lencolumn = len(board[0])
        for i in range(lenrow):
            for j in range(lencolumn):
                if board[i][j] == self.playing:
                    list_positions = [(-1, -1), (-1, 0), (-1, 1),( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]
                    for row, column in list_positions:
                        a_row = row + i
                        c_row = column + j
                        oponnent = False
                        while 0 <= a_row < lenrow and 0 <= c_row < lencolumn and board[a_row][c_row] != self.playing and board[a_row][c_row] != self.EMPTY:
                            oponnent = True
                            a_row += row
                            c_row += column
                        if(a_row >= 0 and a_row < lenrow and c_row >= 0 and c_row < lencolumn and oponnent and board[a_row][c_row] == self.EMPTY):
                            actions_possibles.add((a_row, c_row))
        return actions_possibles
    
    def result(self, board, action):
        #Copia o tabuleiro e adicina a peça do atual jogador na posição action passada como parâmetro
        #Usa o mesmo processo da função actions para determinar as linha de peças que deverão ser transformadas em peças do atual jogador
        #Adiciona a posição dessas peças a serem viradas em um vetor de peças
        #Percorre o vetor transformando todas as peças correspondentes as posições armazenadas em peças do jogador atual
        #Retorna essa cópia do tabuleiro com as ações executadas
        boardcopy = copy.deepcopy(board)
        boardcopy[action[0]][action[1]] = self.playing
        lenrow = len(board)
        lencolumn = len(board[0])
        list_positions = [(-1, -1), (-1, 0), (-1, 1),( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]
        for row, column in list_positions:
            a_row = action[0] + row
            c_row = action[1] + column
            to_flip = []
            while 0 <= a_row < lenrow and 0 <= c_row < lencolumn and boardcopy[a_row][c_row] != self.playing and boardcopy[a_row][c_row] != self.EMPTY:
                to_flip.append((a_row, c_row)) 
                a_row += row                            
                c_row += column
            if 0 <= a_row < lenrow and 0 <= c_row < lencolumn and boardcopy[a_row][c_row] == self.playing:
                for r, c in to_flip:
                    boardcopy[r][c] = self.playing
        return boardcopy
          
    def terminal(self, board):
        #Verifica se a quantidade de ações possíveis de ambos os jogadores são iguais a 0
        #Caso seja, retorna True para indicar que o jogo acabou
        #Caso não seja, retorna False para indicar que o jogo continua
        #Armazena o atual jogador em uma variavel local para depois devolver à variável global e não quebrar a lógica do jogo
        player = self.playing
        self.playing = self.B
        if len(self.actions(board)) == 0:
            self.playing = self.W
            if len(self.actions(board)) == 0:
                self.playing = player
                return True
        self.playing = player
        return False
          
    def utility(self, board):
        #Conta a quantidade de peças de todos os jogadores percorrendo todas as linhas e colunas
        #Define o vencedor através da comparação entre a quantidade de peças de B com as de W
        # B > W -> 1 ; B < W -> -1 ; B = W -> 0
        B_pieces = 0
        W_pieces = 0
        for i in range(8):
            for j in range(8):
                if(board[i][j] == self.W):
                    W_pieces += 1
                if(board[i][j] == self.B):
                    B_pieces += 1
        if(B_pieces > W_pieces):
            return 1
        if(W_pieces > B_pieces):
            return -1
        return 0

class Minimax:
    
    def __init__(self, game, heuristic, time_limit = 3.0, use_pruning = True):
        self.game = game
        self.heuristic = heuristic
        self.time_limit = time_limit
        self.use_pruning = use_pruning
        self.nodes_expanded = 0
        self.start_time = 0.0
        
    def get_best_move(self, state):
        #inicia o cronometro da busca
        self.start_time = time.time()
        best_move = None
        
        #iterative deepening - aumenta a profundidade gradualmente
        for depth in range(1, 65):
            original_player = self.game.playing
            try:
                move = self.search(state, depth)
                if move:
                    best_move = move
            except TimeoutError:
                break
            
            #verifica o limite de tempo
            if time.time() - self.start_time > self.time_limit:
                break
            
        #restaura o jogador atual
        self.game.playing = original_player
        return best_move
        
    def search(self, state, depth):
        best_val = -math.inf
        best_move = None
        actions = self.game.actions(state)
        
        if not actions:
            return None
        
        current_node_player = self.game.playing
        #avalia cada ação possível
        for action in actions:
            child_state = self.game.result(state, action)
            val = self.run(child_state, depth - 1, -math.inf, math.inf, False)
            
            self.game.playing = current_node_player
            
            if val > best_val:
                best_val = val
                best_move = action
        return best_move
    
    def run(self, state, depth=4, alpha=-math.inf, beta=math.inf, maxPlayer=True):
        original_player = self.game.playing
        
        #alterna o jogador / simula turno
        if original_player == self.game.B:
            self.game.playing = self.game.W  
        else:
            self.game.playing = self.game.B
            
        current_node_player = self.game.playing
        if time.time() - self.start_time > self.time_limit:
            self.game.playing = original_player
            raise TimeoutError()
        
        if depth == 0 or self.game.terminal(state):
            self.game.playing = original_player
            return self.heuristic(state)
        
        actions = self.game.actions(state)
        if not actions:
            self.game.playing = original_player
            return self.run(state, depth - 1, alpha, beta, not maxPlayer)
        
        #if depth == 0 or self.game(state):
        #caso MAX, IA tentando maximizar os ganhos
        if maxPlayer:
            maxEval = -math.inf
            for action in actions:
                child = self.game.result(state, action)
                
                eval = self.run(child, depth - 1, alpha, beta, False)
                self.game.playing = current_node_player
                
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if self.use_pruning and beta <= alpha:
                    break
            
            self.game.playing = original_player
            return maxEval
        
        #caso MIN, oponente tentando minimizar as perdas
        else:
            minEval = math.inf
            for action in actions:
                child = self.game.result(state, action)
                
                eval = self.run(child, depth - 1, alpha, beta, True)
                self.game.playing = original_player
                
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if self.use_pruning and beta <= alpha:
                    break
            
            return minEval