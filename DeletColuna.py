# -*- coding: utf-8 -*-
#Código destinado a retirar colunas desnecessárias de uma planilha exportada de um sistema empresarial.
import pandas as pd  # Importa a blibioteca panda

nome_arquivo = input("Entre com o nome do arquivo: ")  # Para a entrada do nome do arquivo, utilizando comando input

planilha = pd.read_excel(nome_arquivo, sep='separador', encoding='utf-8')  # Ler a planilha
#encoding declara a codificação da fonte 
#Exclue a coluna, da variavel planilha, com nome inserido entre aspas 
planilha = planilha.drop("Contador", axis=1) 
planilha = planilha.drop("Domínio", axis=1)
planilha = planilha.drop("Regional", axis=1)
planilha = planilha.drop("Ano Rollout", axis=1)
planilha = planilha.drop("Elemento ID", axis=1)
planilha = planilha.drop("Frequência", axis=1)
planilha = planilha.drop("Projeto Ordem ", axis=1)
planilha = planilha.drop("TX", axis=1)
planilha = planilha.drop("Atividade", axis=1)
planilha = planilha.drop("Tipo de Elemento", axis=1)
planilha = planilha.drop("Tecnologia", axis=1)
planilha = planilha.drop("Data Fim Ordem", axis=1) 
planilha = planilha.drop("IBGE", axis=1)
planilha = planilha.drop("Endereço ID", axis=1)
planilha = planilha.drop("Matrícula", axis=1)
planilha = planilha.drop("Proprietário", axis=1)
planilha = planilha.drop("Site", axis=1)
planilha = planilha.drop("Endereço", axis=1)
planilha = planilha.drop("Circuito Identificado", axis=1)
planilha = planilha.drop("Qtd abertura", axis=1)


# Vai transformar em vetor e separar a string.
nome_arquivo = nome_arquivo.split(".")
#Vai pegar só a primneira parte do vetor
nome_arquivo_novo = nome_arquivo[0] + "_sem_colunas.csv"

# Gera o arquivo final contendo as modificações
planilha.to_csv(nome_arquivo_novo, sep=';', encoding='utf-8', index=False)


print(f"\nColunas apagadas!\nArquivo gerado: {nome_arquivo_novo}\nPasta Teste de automação no desktop.")
"""
OBS: O comando index desabilita a coluna que contem o indice gerado pelo python,
quando colocamos o valor logico false.
OBS²: O comando encoding serve para manter a acentuação da planilha, mas qaundo tentamos
abri-lo no excel, por padrão o .csv abre sem essa configuração, então alem desse atributo,
temos que importar os dados também manualmente.
"""









