import threading
import multiprocessing
import numpy as np   #ESSE NUMPY ESTÁ SENDO USADO PARA IMPORTAR A MATRIZ
from threading import Thread

matriz = np.loadtxt('res/4_int.txt')  # AQUI É ONDE IMPORTAMOS A MATRIZ
tamanhodamatriz = len(matriz)
qntdthreads = multiprocessing.cpu_count() #NO P3 multiprocessing.cpu_count()*2 #NO P4 multiprocessing.cpu_count()/4
divisaoDaThread = tamanhodamatriz/qntdthreads
matRes = []


def multiplicarMatriz(i, divisaoDaThread,mult):
    for j in range(int(i*divisaoDaThread), int(divisaoDaThread*mult)):
        # print(f" for de {(i*divisaoDaThread)}, até {(divisaoDaThread*mult)}")
        # print(j)
        #Função De Multiplicar A Matriz
        for k in range(int(len(matriz[0]))): #coluna da matriz 2
            v= 0
            for l in range(int(len(matriz[0]))): # coluna matriz 1
                v+=matriz[j][l]*matriz[l][k]
            matRes[j].append(v)
    return matRes


mult = 1
for i in range(len(matriz)):
    matRes.append([])
for i in range(qntdthreads):
    # print(f"for {i}, thread {i} ")
    th1 = threading.Thread(target=multiplicarMatriz, args=[i, divisaoDaThread, mult]) #INICIAR A THREAD
    th1.start()
    th1.join() #JOIN É USADO PARA ORGANIZAR A ORDEM DAS THREADS
    mult+=1

print(matriz)
print("\n---------------------------------------------------------------\n")
print(matRes)
