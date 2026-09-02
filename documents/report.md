# Modelagem formal do problema

Othello é um jogo onde dois jogadores devem eliminar todas as peças adversárias ou finalizarem o jogo com mais peças que o adversário em um tabuleiro 8x8. O jogo funciona em um modo único de jogador contra computador.

O jogo Othello é caracterizado como um jogo adversarial e é definido por um tabuleiro 8x8 com cada célula podendo ser definida como Branco (W), Preto (B) ou Vazio (EMPTY), iniciando-se com apenas 2 peças de cada jogador na posição central.

Na Inteligência Artificial, o problema pode ser modelado formalmente pela tupla:
$$Jogo = \langle S, A, T, U \rangle$$

* **Espaço de Estados ($S$):** O ambiente do jogo é composto por todas as possíveis configurações do tabuleiro $8 \times 8$. Cada célula do estado $s$ pode assumir um de três valores:
$$S = \{s \mid s \text{ é uma matriz } 8 \times 8 \text{ onde } s_{i,j} \in \{\emptyset, B, W\}\}$$
* **Ações Possíveis ($A$):** Dado um estado $s$ e o jogador atual, define o conjunto de coordenadas $(i, j)$ válidas para jogar. Uma ação só pertence a $A$ se a célula de destino estiver vazia e a colocação da peça resultar no flanqueamento (captura) de uma ou mais peças contínuas do adversário.
* **Transição ($T$):** Define como o ambiente muda de um estado para o outro ao aplicar uma ação $a \in A$. O novo estado $s'$ é gerado ao inserir a peça do jogador atual na coordenada escolhida e inverter a cor de todas as peças adversárias espremidas em qualquer uma das 8 direções (horizontal, vertical e diagonais).
* **Utilidade ($U$):** Avalia os estados de fim de jogo para determinar o vencedor a partir do saldo final de peças. Da perspectiva do jogador Preto (B), a função retorna $1$ caso B tenha mais peças (Vitória), $-1$ caso W tenha mais peças (Derrota) e $0$ se as quantidades forem iguais (Empate).

## Othello

A classe `Othello` implementada no código conta com métodos e variáveis globais responsáveis pelo funcionamento geral do jogo, sendo elas:

**Variáveis:**
- `self.board`: variável global de inicialização do tabuleiro.
- `self.playing`: variável global de armazenamento do jogador atual.

**Métodos:** 
- `player()`: Retorna o atual jogador.
- `change_turn()`: Troca o turno atual juntamente do jogador que deverá jogar.
- `actions()`: Retorna as jogadas possíveis do atual jogador.
- `result()`: Retorna uma cópia do tabuleiro atual com a transição de estado e o resultado da ação recebida como parâmetro.
- `terminal()`: Retorna se o jogo acabou ou não.
- `utility()`: Retorna o resultado final do jogo (1 = B wins; -1 = W wins; 0 = empate).
   
# Busca adversarial

As funções heurísticas têm um papel extremamente importante no aprimoramento da tomada de decisão da IA que será implementada. As heurísticas dão um "instinto" aguçado para a IA, permitindo que ela deduza o jogador que está vencendo no momento da chamada.

**Heurística A:** - Trabalha com a atribuição de valores para determinadas casas do tabuleiro. A posição das peças acrescenta muito mais valor do que a quantidade.
- Casas das extremidades (cantos) possuem valores altos, pois as peças alocadas nelas são definitivas e nunca poderão ser capturadas pelo oponente.
- Casas adjacentes às extremidades possuem valores muito baixos, pois ocupá-las facilita que o oponente tome os cantos.
- As demais casas recebem valores respectivos ao seu valor agregado para o jogador. Casas centrais possuem valores baixos porém positivos. Casas nas pontas das diagonais das casas centrais recebem valores ainda maiores, pois permitem que os jogadores capturem peças com segurança e boa mobilidade estratégica inicial.

**Heurística B:**
- Trabalha com a contagem material de peças dominadas.
- Subtrai a quantidade total de peças do oponente da quantidade de peças da IA. Quanto maior for a diferença (o saldo), maior será a pontuação da jogada.

## Minimax
A classe `Minimax` configura algoritmos de busca e calculo de valores com base em mapeamentos a fim de escolher as melhores jogadas possíveis, criando assim uma IA sólida, estruturada e competitiva. A classe conta com as seguintes variáveis e métodos:

**Variáveis:**
 -  `self.game` = variável global com objeto instânciado da classe Othello
 -  `self.heuristic` = variável global da heuristica a ser utilizada
 -  `self.time_limit` = variável global do tempo limite
 -  `self.use_pruning` = variável global que define o poda
 -  `self.nodes_expanded` = variável global de controle de nós expandidos
 -  `self.start_time` = variável global que marca o tempo do inicio

**Métodos:**
 -  `def get_best_move()` -> retorna a melhor jogada a ser feita com base em "Iterative deepening"
 -  `def search()` -> retorna a melhor jogada a ser feita com base em um Minimax em uma profundidade fixa
 -  `def run()` -> inicia o algoritmo de Minimax com Poda alfa-beta para determinar de maneira ecônomica a melhor jogada a ser feita
   
### Iterative deepening
O `Iterative Deepening` funciona em conjunto com o algoritimo `Minimax` para melhorar a tomada de decisões por meio de restrições de tempo. Em vez de executar a busca diretamente até certa profundidade fixa, o algoritmo realiza várias execuções do Minimax utilizando profundidades crescentes. Essa abordagem permite que, no momento que o tempo limite foi atingido, o sistema já possua a melhor jogada válida. Isso é essencial em cenários onde o tempo de resposta é limitado.
### Alpha-beta punning
O algoritmo `Minimax` com poda `alfa-beta` visa melhorar a performance,cortando caminhos inúteis com base em valores já obtidos. Por exemplo,em casos onde nos é apresentado dois nós que escolherão valores minimos conectados a um nó que deve escolher o valor máximo,e no filho de valor máximo subsequentes de um desses nós temos valores mais baixos que o valor minimo encontrado no outro nó,o mapeamento do restante desse nó minimo será pulado.

# Experimentos computacionais (testes e discussão)
Para avaliar o desempenho da Inteligência Artificial desenvolvida foram realizados diversos testes, variando principalmente a profundidade de busca, o uso de poda alfa-beta e a heurística aplicada.

Também foram realizados testes comparando as heurísticas implementadas:

- **Heurística A (posicional):** apresentou melhor desempenho estratégico, priorizando o controle de posições-chave do tabuleiro, como os cantos. Em partidas mais longas, mostrou-se mais eficiente para garantir vantagem sustentável.
- **Heurística B (material):** teve bom desempenho em estágios finais do jogo, onde a quantidade de peças passa a ser um fator decisivo. No entanto, em fases iniciais e intermediárias, mostrou-se menos eficaz por ignorar aspectos estratégicos do posicionamento.

Além disso, foi avaliado o impacto do uso de *Iterative Deepening*. Os testes demonstraram que essa abordagem permite que a IA sempre retorne uma jogada válida dentro do tempo limite estabelecido, mesmo quando a busca em profundidades maiores não é concluída. Isso aumentou significativamente a robustez do sistema, especialmente em situações onde o tempo de processamento é restrito.

# Conclusão
O código tem uma base forte e bem estruturada para uma partida de Othello onde a IA é baseada em `Minimax`. Isso faz com que nosso código seja limpo, mais claro e objetivo, de maneira que desempenho não seja um problema, e que a performance esteja numa escala padrão apesar dos problemas, além é claro, de ter bons algoritmos de busca.

