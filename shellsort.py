import sys
import time

def read_file(name):
    with open(name, 'r') as file:
        line = file.readline()
    numbers = [int(num) for num in line.split()]
    return numbers

def shell_sort(arr):
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

    return arr

if __name__ == "__main__":
    name = "ordem_aleatoria.txt"
    try:
        arr = read_file(name)
        print("Original Array: ")
        print(arr)
        start = time.perf_counter()
        shell_sort(arr)
        end = time.perf_counter()

        execution_time = end - start
        print("Sorted Array:")
        print(arr)
        print("Time Lapse: ")
        print(f"{execution_time:.6f}")
    except FileNotFoundError:
        print("Error: File Not Found")
    except ValueError:
        print("Error: Invalid Value Found")

