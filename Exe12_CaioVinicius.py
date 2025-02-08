#Escreva um programa que pergunte o valor total da conta e em seguida quantos clientes existem,
# divida a conta pelos clientes e exiba cada cliente deve pagar, 
# seguida da mensagem "cada cliente deve pagar:" X valor.

total = float( input ("Qual o valor total da sua conta? "))
clientes = int( input ("Quantas pessoas iram dividir a conta? "))

resultado = total / clientes

print("Cada cliente irá pagar R$ ",resultado,)