#!/usr/bin/env python3
import time
import os

filename = input("Digite o nome do arquivo desejado: ")
numgen = input("Digite quantas geracoes voce quer o programa simule: ")

with open(filename, 'rt') as gamefile: 
    dim_y = gamefile.readline().strip() ##leitura das dimensoes da matriz do jogo
    dim_y = int(dim_y)
    dim_x = gamefile.readline().strip()
    dim_x = int(dim_x)
    linereader = []
    gamematrix = []

    for i in range(dim_y):
        linereader = gamefile.readline().strip()
        gamematrix.append(linereader)

    gamematrix = [[int(char) for char in linha] for linha in gamematrix] ##transforma a matriz de strings em matriz de numeros

    for i in range (dim_x):
        for j in range (dim_y):
            if(gamematrix[i][j] == 0):
                ##analisa os vizinhos do para possivelmente criar um novo, cuidados especial para elementos nas bordas
            else
                ##analisa os vizinhos 1 para matar ou deixar a célular viva , mesmo cuidado para elementos nas bordas