def abrir(url)->list[int]:
    caminho_arquivo=url
    with open(caminho_arquivo,'r', encoding='utf-8') as f:
        dados=f.read().strip()
        if not dados: raise ValueError('O arquivo passado está vazio.')
    
    numeros=[int(x) for x in dados.split() if x]
    return numeros


def gravar(url, info)->None:
    with open(url,'a',encoding='utf-8') as arquivo:
        arquivo.write(str(info)+'\n')
    