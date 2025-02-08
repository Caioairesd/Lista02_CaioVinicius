#10- Escreva um programa que pergunte quantos pedaços o bolo tem, 
# em seguida pergunte ao usuário quantos pedaços ele comeu, 
# calcule quantos pedaços tem e exiba o resultado com uma mensagem de livre escolha.

Pedacos = int(  input("Quantos pedaços o seu bolo tem?"))
Digeridos = int( input("Quantos pedaços você comeu?"))

Resto =Pedacos - Digeridos 
print ("O seu bolo tem ",Pedacos,"pedaços,","Você comeu ",Digeridos,"Restam, ",Resto, "pedaços")

