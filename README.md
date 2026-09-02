# Othello com Inteligência Artificial

Implementação completa do jogo **Othello (Reversi)** em Python, incluindo uma Inteligência Artificial baseada em **Minimax**, **poda alfa-beta**, **aprofundamento iterativo (Iterative Deepening)** e funções heurísticas.

O projeto foi desenvolvido como trabalho acadêmico da disciplina de **Inteligência Artificial**.

## Sobre o projeto

O Othello é um jogo adversarial disputado por dois jogadores em um tabuleiro 8x8.

O objetivo é terminar a partida com uma quantidade de peças maior que a do adversário. Durante o jogo, novas peças são posicionadas no tabuleiro e peças inimigas são capturadas por meio de flanqueamento nas direções horizontal, vertical e diagonal.

Além da implementação completa das regras do jogo, o projeto possui uma Inteligência Artificial capaz de escolher jogadas por meio de algoritmos de busca adversarial.

## Funcionalidades

- Implementação completa das regras do Othello
- Tabuleiro 8x8
- Identificação automática das jogadas válidas
- Captura e inversão das peças adversárias
- Controle de turnos
- Detecção de fim de jogo
- Cálculo do vencedor
- Modo Jogador x Jogador
- Modo Jogador x Máquina
- Modo Máquina x Máquina
- Algoritmo Minimax
- Poda alfa-beta
- Aprofundamento iterativo
- Limite de tempo para tomada de decisão da IA
- Funções heurísticas para avaliação do tabuleiro

## Inteligência Artificial

A Inteligência Artificial utiliza o algoritmo **Minimax** para analisar possíveis estados futuros do jogo e escolher a jogada considerada mais vantajosa.

Como o número de possibilidades cresce rapidamente conforme a profundidade da busca aumenta, foram utilizadas técnicas para melhorar o desempenho do algoritmo.

### Minimax

O Minimax é um algoritmo utilizado em jogos adversariais.

A IA considera que:

- um jogador tenta maximizar o valor da posição;
- o adversário tenta minimizar esse valor.

A partir dessa lógica, diferentes sequências de jogadas são analisadas para encontrar a melhor decisão possível.

### Poda alfa-beta

A **poda alfa-beta** reduz a quantidade de estados que precisam ser analisados pelo Minimax.

Quando o algoritmo identifica que determinado caminho não poderá produzir uma decisão melhor do que uma alternativa já analisada, esse caminho deixa de ser explorado.

Isso permite alcançar profundidades maiores com menor custo computacional.

### Aprofundamento iterativo

O **Iterative Deepening** executa o Minimax várias vezes utilizando profundidades progressivamente maiores.

Por exemplo:

```text
Profundidade 1
      ↓
Profundidade 2
      ↓
Profundidade 3
      ↓
...
```

Dessa forma, quando o limite de tempo é atingido, a IA ainda possui uma jogada válida obtida na última profundidade completamente analisada.

## Heurísticas

O projeto implementa duas formas de avaliação dos estados do tabuleiro.

### Heurística A — Avaliação posicional

Cada posição do tabuleiro possui um peso estratégico.

Os cantos possuem valores muito altos porque uma peça posicionada em um canto não pode mais ser capturada pelo adversário.

Posições próximas aos cantos possuem valores negativos, pois ocupá-las pode facilitar a captura do canto pelo oponente.

As demais posições recebem valores de acordo com sua importância estratégica.

Exemplo da matriz utilizada:

```text
120  -20   20    5    5   20  -20  120
-20  -40   -5   -5   -5   -5  -40  -20
 20   -5   15    3    3   15   -5   20
  5   -5    3    3    3    3   -5    5
  5   -5    3    3    3    3   -5    5
 20   -5   15    3    3   15   -5   20
-20  -40   -5   -5   -5   -5  -40  -20
120  -20   20    5    5   20  -20  120
```

### Heurística B — Avaliação por quantidade de peças

A segunda heurística considera a quantidade de peças dominadas por cada jogador.

O valor é calculado a partir da diferença entre as peças pretas e brancas.

## Modelagem do problema

O Othello pode ser representado formalmente como:

```text
Jogo = <S, A, T, U>
```

Onde:

- `S` representa o conjunto de estados possíveis do tabuleiro;
- `A` representa as ações válidas disponíveis;
- `T` representa a função de transição entre estados;
- `U` representa a função de utilidade utilizada para determinar o resultado final.

A função de utilidade utilizada no projeto retorna:

```text
 1  → Vitória do jogador Preto
-1  → Vitória do jogador Branco
 0  → Empate
```

## Estrutura do projeto

```text
.
├── main.py
├── othello.py
├── report.md
├── README.md
└── LICENSE
```

### `main.py`

Responsável pela execução do programa.

Contém:

- seleção do modo de jogo;
- interação com o jogador;
- impressão do tabuleiro;
- funções heurísticas;
- controle da partida.

### `othello.py`

Contém a implementação principal do jogo e da Inteligência Artificial.

Principais classes:

```text
Othello
Minimax
```

### `report.md`

Documentação acadêmica contendo:

- modelagem formal do problema;
- explicação da busca adversarial;
- heurísticas;
- Minimax;
- poda alfa-beta;
- aprofundamento iterativo;
- experimentos computacionais.

## Como executar

É necessário possuir o Python instalado.

Como o projeto utiliza `match/case`, recomenda-se utilizar **Python 3.10 ou superior**.

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/othello-ia.git
```

Entre na pasta:

```bash
cd othello-ia
```

Execute:

```bash
python main.py
```

## Modos de jogo

Ao iniciar o programa, são apresentadas três opções:

```text
1 - Jogador x Jogador
2 - Jogador x Máquina
3 - Máquina x Máquina
```

A partida é executada diretamente pelo terminal.

As coordenadas das jogadas válidas são exibidas a cada turno.

## Tecnologias e conceitos utilizados

- Python
- Inteligência Artificial
- Busca adversarial
- Minimax
- Poda alfa-beta
- Aprofundamento iterativo
- Funções heurísticas
- Busca em espaço de estados

## Autores

- Miguel Henrique Amorim Pereira
- Miguel Lopes de Almeida
- Murilo Matos Lopes

## Licença

Consulte o arquivo `LICENSE` para informações sobre a licença do projeto.
