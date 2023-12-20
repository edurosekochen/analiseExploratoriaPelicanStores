import pandas as pd
import numpy as np
# Carregando os dados do arquivo
dados = pd.read_excel('PelicanStores.xlsx')
# Visualizando as primeiras linhas do dataframe
print(dados.head())
# Calculando medidas de posição e variabilidade para as variáveis quantitativas
resumo_quantitativo = {
'Vendas Líquidas': {
'Média': np.mean(dados['Vendas líquidas']),
'Mediana': np.median(dados['Vendas líquidas']),
'Variância': np.var(dados['Vendas líquidas'], ddof=1),
'Desvio Padrão': np.std(dados['Vendas líquidas'], ddof=1),
'Amplitude': np.ptp(dados['Vendas líquidas'])
},
'Itens': {
'Média': np.mean(dados['Itens']),
'Mediana': np.median(dados['Itens']),
'Variância': np.var(dados['Itens'], ddof=1),
'Desvio Padrão': np.std(dados['Itens'], ddof=1),
'Amplitude': np.ptp(dados['Itens'])
},
'Idade': {
'Média': np.mean(dados['Idade']),
'Mediana': np.median(dados['Idade']),
'Variância': np.var(dados['Idade'], ddof=1),
'Desvio Padrão': np.std(dados['Idade'], ddof=1),
'Amplitude': np.ptp(dados['Idade'])
}
}
# Calculando a moda para as variáveis qualitativas
moda_qualitativa = dados[['Tipo de Cliente', 'Método de Pagamento', 
'Gênero', 'Estado Civil']].mode().iloc[0].to_dict()
# Calculando a quantidade de ocorrências para cada variável qualitativa
ocorrencias_qualitativas = dados[['Tipo de Cliente', 'Método de Pagamento', 'Gênero', 'Estado Civil']].apply(pd.Series.value_counts)
# Exibindo os resultados
print("Resumo Quantitativo:\n", resumo_quantitativo)
print("\nModa Qualitativa:\n", moda_qualitativa)
print("\nOcorrências Qualitativas:\n", ocorrencias_qualitativas)
