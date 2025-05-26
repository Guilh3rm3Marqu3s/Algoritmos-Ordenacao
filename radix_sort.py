import sys
from arquivo import abrir,gravar
import time

def countingSort(numbers:list,expo)->None:
    n=len(numbers)
    output=[0]*n
    count=[0]*10
    
    for i in range(0,n):
        idx=numbers[i] // expo
        count[idx % 10]+=1
        
    for i in range(1,10):
        count[i]+=count[i-1]
        
    i=n-1
    while i>=0:
        idx=numbers[i] // expo
        output[count[idx%10]-1]=numbers[i]
        count[idx%10]-=1
        i-=1
        
    i=0
    for i in range(0,len(numbers)):
        numbers[i]=output[i]


def radix_sort(numbers:list)->None:
    maxi=max(numbers)
    
    exp=1
    while maxi/exp >=1:
        countingSort(numbers,exp)
        exp*=10
        
        
numeros=abrir(sys.argv[1])
ini=time.time()
radix_sort(numeros)
fim=time.time()
gravar(sys.argv[2],(fim-ini)*1000)
print(numeros)
    