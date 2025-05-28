import sys
from arquivo import abrir, gravar
import time

def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq

    if dir < n and arr[dir] > arr[maior]:
        maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(numeros: list):
    inicio_tempo = time.time()
    n = len(numeros)

    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(numeros, n, i)

    # Extrair elementos um por um
    for i in range(n - 1, 0, -1):
        numeros[0], numeros[i] = numeros[i], numeros[0]  # Move a raiz para o final
        heapify(numeros, i, 0)

    fim_tempo = time.time()
    gravar(sys.argv[2], (fim_tempo - inicio_tempo) * 1000)  # Tempo em ms

    print('Lista Ordenada:\n', numeros)

numeros = abrir(sys.argv[1])
heap_sort(numeros)