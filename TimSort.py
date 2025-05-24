import sys
import time

MIN_MERGE = 32


def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
    numeros = list(map(int, conteudo.replace(',', ' ').split()))
    return numeros


if __name__ == "__main__":

    nome_entrada = sys.argv[1]
    nome_saida_tempo = sys.argv[2]

    try:
        arr = ler_arquivo(nome_entrada)
        print("\nArray fornecido:\n")
        print(arr)

        inicio = time.perf_counter()
        timSort(arr)
        fim = time.perf_counter()

        print("\nArray ordenado:\n")
        print(arr)

        tempo_execucao = fim - inicio

        with open(nome_saida_tempo, 'a') as f:
            f.write(f"Tempo: {tempo_execucao:.6f} segundos\n")

    except FileNotFoundError:
        print(f"Arquivo '{nome_entrada}' não encontrado. Verifique o caminho e tente novamente.")
    except ValueError:
        print("Erro ao ler os dados. Verifique se o arquivo contém apenas números válidos.")

