x: int
soma: int

soma = 0
x = int(input("Digite o um número: "))#Guarda o valor inteiro digitado pelo usuário
while x != 0:#enquanto(while) x for diferente de 0 faça(:)
    soma = soma + x#Soma os valores digitados pelo usuário
    x = int(input("Digite mais um número: "))#Enquato usuario nao digitar zero o comando volta e imputa o valor digitado.
print("A soma dos valores é: ", soma)

