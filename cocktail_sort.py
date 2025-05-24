import sys
from arquivo import abrir,gravar
import time
def cocktail_sort(numeros:list):
    inicio_tempo=time.time()
    trocado=True
    n=len(numeros)
    inicio=0
    fim=n-1
    
    while(trocado == True):
        trocado=False
        
        for i in range(inicio,fim):
            if(numeros[i]>numeros[i+1]):
                numeros[i],numeros[i+1]=numeros[i+1],numeros[i] #troca
                trocado=True
                
        if trocado==False: break
        
        trocado=False
        
        fim-=1
        
        for i in range(fim-1,inicio-1,-1):
            if (numeros[i]>numeros[i+1]):
                numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
                trocado=True
                
        inicio+=1
        
        
    fim_tempo=time.time()
    gravar(sys.argv[2],(fim_tempo-inicio_tempo)*1000)#em ms
        
    print('Lista Ordenada:\n',numeros)


numeros=abrir(sys.argv[1])
    
cocktail_sort(numeros)