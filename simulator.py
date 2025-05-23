#!/usr/bin/env python3
import time
import os

def neighbours(gamematrix: list[list[int]], i: int, j: int, dim_x: int, dim_y: int): ##funcao que busca os vizinhos
    nb = 0
    if i < dim_x - 1 and gamematrix[i + 1][j]: ##verifica se pode ter vizinho a diretia and se gamematrix[][] = true 
        nb = nb + 1
    if i - 1 >= 0 and gamematrix[i - 1][j]: ##verifica se pode ter vizinho a esquerda and se gamematrix[][] = true 
        nb = nb + 1
    if j < dim_y - 1 and gamematrix[i][j + 1]: ##verifica se pode ter vizinho em cima and se gamematrix[][] = true
        nb = nb + 1
    if j - 1 >= 0 and gamematrix[i][j - 1]: ##verifica se pode ter vizinho em baixo and se gamematrix[][] = true
        nb = nb + 1
    if i < dim_x - 1 and j < dim_y - 1 and gamematrix[i + 1][j + 1]: ##verifica se pode ter vizinho na direita-cima and se gamematrix[][] = true 
        nb = nb + 1
    if i - 1 >= 0 and j - 1 >= 0 and gamematrix[i - 1][j - 1]: ##verifica se pode ter vizinho na esquerda-baixo and se gamematrix[][] = true
        nb = nb + 1
    if i < dim_x - 1 and j - 1 >= 0 and gamematrix[i + 1][j - 1]: ##verifica se pode ter vizinho na direta-baixo and se gamematrix[][] = true
        nb = nb + 1
    if i - 1 >= 0 and j < dim_y - 1 and gamematrix[i - 1][j + 1]: ##verificase pode ter vizinho na esquerda-cima and se gamematris[][] = true
        nb = nb + 1

    return nb
filename = input("Digite o nome do arquivo desejado: ")
numgen = int(input("Digite quantas geracoes voce quer o programa simule: "))
                
with open(filename, 'rt') as gamefile: 
    dim_x = gamefile.readline().strip() ##leitura da dimensão y(primeiro valor do arquivo)
    dim_x = int(dim_x)
    dim_y = gamefile.readline().strip()##leitura da dimensão x(segundo valor do arquivo)
    dim_y = int(dim_y)
    linereader = [] ##lista que vai armazezando a leitura do mapa incial do jogo
    gamematrix = [] ##matriz que vai receber o mapa inicial do

    for i in range(dim_y):
        linereader = gamefile.readline().strip()
        gamematrix.append(linereader)

gamematrix = [[int(char) for char in linha] for linha in gamematrix] ##transforma a matriz de strings em matriz de numeros

for t in range (numgen):
    celulas = 0
    switchermatrix = [[0 for _ in range(dim_y)] for _ in range(dim_x)]
    for i in range (dim_x):
        for j in range (dim_y):
            nb = neighbours(gamematrix, i, j, dim_x, dim_y)
            if gamematrix[i][j] == 0: ##estado da celula morto
                if nb == 3:
                    switchermatrix[i][j] = 1 ##nasce a célula
                    
            if gamematrix[i][j] == 1: ##estado da celula vivo
                if nb > 3: ##superpopulacao
                    switchermatrix[i][j] = 0
                if nb < 2: ##solidao
                    switchermatrix[i][j] = 0
                if nb == 2 or nb == 3: ##sobrevivencia
                    switchermatrix[i][j] = 1

    gamematrix = switchermatrix
    time.sleep(0.1)
    os.system('clear')
    print(f"Gen: {t + 1}")
    print(f"Células vivas: {celulas}")
    for linha in gamematrix:
          print(''.join('.' if x == 0 else '■' for x in linha))

