import sys
import time
from arquivo import abrir, gravar

def shell_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    end=time.perf_counter()
    gravar(sys.argv[2],(end-start)*1000)
    print('Lista Ordenada:\n',arr)
    return arr

numeros=abrir(sys.argv[1])
shell_sort(numeros)

