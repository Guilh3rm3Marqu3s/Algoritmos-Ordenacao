import sys
from arquivo import abrir,gravar
import time
def cocktail_sort(numeros:list):
    inicio=time.time()
    for i in range(len(numeros) // 2):
        troca=False
        for j in range(i,len(numeros)-i-1):
            if numeros[j]>numeros[j+1]:
                #trocar os dois
                numeros[j],numeros[j+1]=numeros[j+1],numeros[j]
                troca=True
                
        if not troca: break
        
        troca=False
        
        for j in range(int(len(numeros)-2-i),i-1,-1):
            if numeros[j]>numeros[j+1]:
                numeros[j],numeros[j+1]=numeros[j+1],numeros[j]
                troca=True
                
        if not troca: break
    
    fim=time.time()
    gravar(sys.argv[2],fim-inicio)
        
    print('Lista Ordenada:\n',numeros)


numeros=abrir(sys.argv[1])
    
cocktail_sort(numeros)