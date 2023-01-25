"""
Desafio, cadastro de Usúario 

Crie um programa que receba os dados do usúario sendo eles
Nome , Idade, e data de cadastro esta sendo a data que o mesmo informou os dados 
Crie uma lista contendo valores que serão atribuidos randomicamente  como desconto ao realizar o cadastro 
E imprima a seguinte mensagem na tela após receber os dados 
Olá (nome) seu registro foi confirmado com sucesso na data de (data de cadastro). Parabens houve um sorteio e você
ganhou um desconto de (lista com desconto aleatorio) na sua primeira compra, confirme abaixo seus dados. E imprima
os dados do cliente abaixo.

"""


import random
from datetime import datetime

nome_usuario = str(input("Digite seu nome completo "))
idade = int(input("Digite sua idade "))
data_de_cadastro = datetime.now()
desconto_automatico = ["R$50,00", "R$35,00", "R$40,00", "R$100,00" ]

data_aniversario = datetime.strptime(input("Digite a sua data de aniversario"),"%d%m%Y")

print(f" Olá {nome_usuario} seu registro foi confirmado com sucesso na data de {data_de_cadastro}. Parabéns houve um sorteio e você ganhou um desconto no valor de {random.choice(desconto_automatico)} na sua primeira compra, confirme seus dados abaixo   ")
print (nome_usuario )
print(idade)
print(data_de_cadastro)
print(data_aniversario)
