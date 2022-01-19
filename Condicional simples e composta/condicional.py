
#Condicional simples SE
X = 10

print ("Bom dia")

if X < 0: #if = se / se x < 10 faça
    print("Boa tarde")

print ("Boa noite")

#Condicional composta SE ENTAO

hora : int

hora = int(input("Digite a hora: "))
if hora < 12: #SE
    print("Bom dia")
else: #ENTAO
    print("Boa tarde")

#Encadeameto

hora : int

hora = int(input("Digite a hora: "))
if hora < 12: #SE
    print("Bom dia")
elif hora < 18: #SENAO
    print("Boa tarde")
else:
    print("Boa noite")
