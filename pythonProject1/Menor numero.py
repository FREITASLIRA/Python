
primeiro = int(input("Qual o primeiro número: "))
segundo = int(input("Qual segundo número: "))
terceiro = int(input("Qual terceiro número: "))

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
elif segundo < terceiro: #elif faz um encadeamento para nao ficar repitido o if(SE)
    menor = segundo
else: # Senão
    menor = terceiro

print(f"O menor valor é: {menor}")