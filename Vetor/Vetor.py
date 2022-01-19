N = int(input("Quantos números você vai digitar? "))

vet: [float] = [0 for x in range(N)]#lista de float recebe 0 ...
for i in range (0, N): #Para i de 0 até N
    vet[i] = float(input("Digite um número: ")) #vet na posição i recebe o float do input (usuario digita)

print()
print("Números digitados: ")
for i in range(0,N):
    print(f"{vet[i]:.1f}")#imprimir na tela vet na posição i