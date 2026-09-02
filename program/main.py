from othello import Othello
from othello import Minimax
from os import system

def main():
    jogo = Othello()
    tabuleiro_atual = jogo.board
    
    print("ESCOLHA UM MODO DE JOGO")
    print("1 - Jogador x Jogador")
    print("2 - Jogador x Máquina")
    print("3 - Máquina x Máquina")
    escolha = input("Modo de jogo escolhido: ")
    
    #dicionario para facilitar a identificação dos jogadores
    handle = {}
    
    match(escolha):
        case "1":
            handle[jogo.B] = "humano"
            handle[jogo.W] = "humano"
        case "2": 
            handle[jogo.B] = "humano"
            handle[jogo.W] = Minimax(jogo, heuristica_A, time_limit=3.0)
        case "3":
            handle[jogo.B] = Minimax(jogo, heuristica_A, time_limit=2.0)
            handle[jogo.W] = Minimax(jogo, heuristica_A, time_limit=2.0)

    system('clear')
    print("Bem-vindo ao Othello!")

    while not jogo.terminal(tabuleiro_atual):
        imprimir_tabuleiro(tabuleiro_atual)
        
        current_turn = jogo.playing
        current_player = handle[current_turn]
        acoes = jogo.actions(tabuleiro_atual)
        
        if current_player == "humano":
            print(f"Vez do jogador: {current_player}")
            print(f"Jogadas válidas: {acoes}")
            
            linha = int(input("Escolha a linha: "))
            coluna = int(input("Escolha a coluna: "))
            
            try:
                acao = (linha, coluna)
            except ValueError:
                print("Por favor, digite apenas números!")
                continue

        else:
            print(f"Jogadas válidas: {acoes}")
            print(f"{current_turn} pensando...")
            acao = current_player.get_best_move(tabuleiro_atual)
            print(f"{current_turn} jogou: {acao}")
            
        if acao in acoes:
            tabuleiro_atual = jogo.result(tabuleiro_atual, acao)
            jogo.change_turn(tabuleiro_atual)
        else:
            print("Jogada inválida! Escolha uma coordenada da lista.")

    print("\n--- FIM DE JOGO ---")
    imprimir_tabuleiro(tabuleiro_atual)
    
    resultado = jogo.utility(tabuleiro_atual)
    if resultado == 1:
        print("O Jogador PRETO (B) Venceu!")
    elif resultado == -1:
        print("O Jogador BRANCO (W) Venceu!")
    else:
        print("EMPATE!")


def imprimir_tabuleiro(board):
    #Método de impressão do tabuleiro
    print("\n   0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        linha_str = f"{i}  "
        for cell in row:
            if cell == 'B':
                linha_str += "B "
            elif cell == 'W':
                linha_str += "W "
            else:
                linha_str += ". "
        print(linha_str)
    print()
    

def heuristica_A(board):
    weight = [
        [ 120, -20,  20,   5,   5,  20, -20,  120],
        [ -20, -40,  -5,  -5,  -5,  -5, -40,  -20],
        [  20,  -5,  15,   3,   3,  15,  -5,   20],
        [   5,  -5,   3,   3,   3,   3,  -5,    5],
        [   5,  -5,   3,   3,   3,   3,  -5,    5],
        [  20,  -5,  15,   3,   3,  15,  -5,   20],
        [ -20, -40,  -5,  -5,  -5,  -5, -40,  -20],
        [ 120, -20,  20,   5,   5,  20, -20,  120]
    ]
    score = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'B': score += weight[r][c]
            elif board[r][c] == 'W': score -= weight[r][c]
    return score

def heuristica_B(board):
    score = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'B': score += 1
            elif board[r][c] == 'W': score -= 1
    return score

if __name__ == "__main__":
    main()