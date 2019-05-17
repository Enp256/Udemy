#!/usr/bin/env python
# coding: utf-8

# # Primeiro projeto - Notebook de passo a passo
# 
# Abaixo está um conjunto de passos para você seguir para tentar criar o jogo da velha!

# ** Passo 1: Escreva uma função que pode imprimir o tabuleiro. Configure-o como uma lista, onde cada índice 1-9 corresponde a um número em um bloco de números, para que você obtenha uma representação do tabuleiro 3 por 3. **

# In[32]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# ** Passo 2: Escreva uma função que pode receber uma entrada de jogador e atribua seu marcador como 'X' ou 'O'. Pense em usar * while * para pedir jogadas continuamente até obter uma resposta correta. **

# In[25]:


def player_input():
    resp=' '
    
    while not(resp == 'X' or resp == 'O'):
        
        resp=input('X ou O ?  ').upper()
    if resp == 'X':
        return ('X','O')
    else:
        return ('X','O')


# ** Passo 3: Escreva uma função que recebe, no objeto da lista do tabuleiro, um marcador ('X' ou 'O') e uma posição desejada (número 1-9) e atribuia-o ao tabuleiro. **

# In[4]:


def place_marker(board, marker, position):
    board[position]=marker


# ** Etapa 4: escreva uma função que recebe um tabuleiro e uma jogada (X ou O) e, em seguida, verifica se essa jogada ganhou. **

# In[36]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # vitória pelo topo
    (board[4] == mark and board[5] == mark and board[6] == mark) or # pelo meio
    (board[1] == mark and board[2] == mark and board[3] == mark) or # por baixo
    (board[7] == mark and board[4] == mark and board[1] == mark) or # pela esquda
    (board[8] == mark and board[5] == mark and board[2] == mark) or # pelo meio
    (board[9] == mark and board[6] == mark and board[3] == mark) or # pela direita
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# 
# ** Etapa 5: Escreva uma função que usa o módulo random para decidir aleatoriamente qual jogador é o primeiro. Você pode querer pesquisar random.randint () Retornar uma string de qual jogador foi primeiro. **

# In[ ]:


import random
def choose_first():
    first=random.randint(0,1)
    if first == 0:
        return 'Player 2'
    elif first ==1: 
        return 'Player 1'


# ** Passo 6: Escreva uma função que retorna um booleano indicando se um espaço na placa está livremente disponível. **

# In[7]:


def space_check(board, position):
    
    return board[position] == ' '


# ** Passo 7: escreva uma função que verifica se a placa está cheia e retorna um valor booleano. Verdadeiro se cheio, Falso de outra forma. **

# In[48]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# 
# ** Etapa 8: Escreva uma função que solicita a próxima posição de um jogador (como número 1-9) e, em seguida, usa a função do passo 6 para verificar se é uma posição livre. Se for, então retorne a posição para uso posterior. **

# In[44]:


def player_choice(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Escolha sua jogada: (1-9) ')
    return int(position)


# ** Passo 9: escreva uma função que pede ao jogador se eles querem jogar novamente e retorna um verdadeiro booleano se eles quiserem jogar novamente. **

# In[50]:


def replay():
    
    return input('querem jogar novamente? ').lower().startswith('s')


# ** Passo 10: Aqui vem a parte difícil! Use os loops e as funções que você fez para executar o jogo! **

# In[51]:


print('Bem vindo ao jogo da velha!')

while True:
    
    # Defina o jogo
    board=[' '] *10
    j1,j2=player_input()
    turn= choose_first()
    print(turn + 'começa')
    game_on =True
    
    while game_on:
        # Vez do jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, j1, position)
        
            if win_check(board,j1):
                display_board(board)
                print('parabens, voce ganhou')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, j2, position)
        
            if win_check(board,j2):
                display_board(board)
                print('Player 2 ganhou')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate')
                    break
                else:
                    turn = 'Player 1'
        

    if not replay():
        break


# ## Muito bem!

# In[ ]:




