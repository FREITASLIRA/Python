import math #(É uma biblioteca de funções matematicas) serve para usar a raiz quadrada no código


base = float(input("Qual a base do retangulo? "))
altura = float(input("Qual a altura do retangulo? "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2) #O ** significa a exponenciação ou o elevado a alguma coisa

print(f"Area =", area)
print(f"Perimetro = ", perimetro)
print(f"Diagonal = ", diagonal)