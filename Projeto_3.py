"""
Curso: Introdução à programação Python

Projeto Python 3
Escreva um programa em Python que colete dados de notícias políticas na
página do G1 e os salve em um arquivo no formato html. Coloque o código
e o arquivo html no seu GitHub.

Autor: Guilherme Medeiros Lionço
Data: 08/09/2022
Versão:0.0.1
"""

print ("\nEste programa coletará notícias do G1 e salva em html")

#importando o módulo request para trabalhar com pagina da web
import requests

#abrindo a página
pagina = requests.get('https://g1.globo.com/politica/')


#salvando o arquivo
with open('politica.html', 'wb') as arquivo:
    for texto in pagina.iter_content():
        arquivo.write(texto)

print("\nO arquivo foi salvo")
