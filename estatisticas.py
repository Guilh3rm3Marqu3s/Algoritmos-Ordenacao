import numpy as np
from scipy.stats import friedmanchisquare
import scikit_posthocs as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import studentized_range

def pegar_dados(url: str) -> list:
    dados = []
    with open(url, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                dados.append(float(linha))
    return dados

# Carregar dados
CS = pegar_dados('./tempo_execucao/cocktail/ordenados_inversamente_3.txt')
HS = pegar_dados('./tempo_execucao/heap/ordenados_inversamente_3.txt')
SS = pegar_dados('./tempo_execucao/shell/ordenados_inversamente_3.txt')
TS = pegar_dados('./tempo_execucao/tim/ordenados_inversamente_3.txt')
RS = pegar_dados('./tempo_execucao/radix/ordenados_inversamente_3.txt')

# Teste de Friedman
res = friedmanchisquare(CS, HS, SS, TS, RS)



# Criar DataFrame e calcular ranks
data = pd.DataFrame({
    'Cocktail': CS,
    'Heap': HS,
    'Shell': SS,
    'Tim': TS,
    'Radix': RS
})

# Calcular ranks médios (por linha)
ranks = data.rank(axis=1, method='min', ascending=True)
mean_ranks = ranks.mean()  # Já é uma Series com nomes
# Teste post-hoc de Nemenyi
nemenyi = sp.posthoc_nemenyi_friedman(data.values)
print(nemenyi)
# Mapear os índices numéricos para os nomes corretos
labels = data.columns.tolist()
nemenyi.index = labels
nemenyi.columns = labels

# Matriz de significância
# Plotar o diagrama de diferença crítica
plt.figure(figsize=(10, 5))
sp.critical_difference_diagram(
    ranks=mean_ranks,
    sig_matrix=nemenyi,
    label_fmt_left='{label} ({rank:.2f})',
    label_fmt_right='({rank:.2f}) {label}',
    text_h_margin=0.02,
    marker_props={'s': 100},  # Correção: usar 's' em vez de 'markersize'
    label_props={'fontsize': 12}
)

plt.title("Diagrama de Diferença Crítica (OD3)")
plt.tight_layout()
plt.show()