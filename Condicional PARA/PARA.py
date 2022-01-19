

N = int(input("Quantos números serão digitados? "))

soma = 0
for i in range(0, N): #para(for) i dentro da faixa(in ranger) de 0 até N
    x = int(input("Digite um número: ")) #x recebe o valor que o usuário digita
    soma = soma + x

print("A soma é: ", soma)
