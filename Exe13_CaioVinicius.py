#Escreva um programa que solicite um determinado números de dias,
# em seguida exiba o quanto esses dias equivalem em horas, 
# minutos e segundos.

dias = int ( input("Qual a quantidade de dias você deseja calcular:"))

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(dias, "dias equivalem à ",horas," hrs, ",minutos," minutos e ",segundos," segundos")