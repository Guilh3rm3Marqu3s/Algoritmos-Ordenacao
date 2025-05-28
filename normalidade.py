from scipy.stats import shapiro
import numpy as np


def pegar_dados(url: str) -> list:
    dados = []
    with open(url, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                dados.append(float(linha))
    return dados

CS=pegar_dados('./tempo_execucao/radix/ordenados_inversamente_3.txt')
stat,p_valor=shapiro(CS)
print(f"Shapiro-Wilk (dados normais): estatística={stat:.4f}, p-valor={p_valor:.4f}")

