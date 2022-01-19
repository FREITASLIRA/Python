
aluno1: str
aluno2: str
aluno3: str
notaaluno1: float
notaaluno2: float
notaaluno3: float
media: float

print(f"Qual o nome do primeiro aluno?")         #o print serve para imprimir na tela do usuário
aluno1 = input()             #primeiro colocamos a variavel (= RECEBE) e depois pedimos a entrada do dado (input = leia)
print(f"Qual a nota do primeiro aluno?")
notaaluno1 = float(input())

print(f"Qual o nome do segundo aluno?")
aluno2 = input()
print(f"Qual a nota do segunda aluno?")
notaaluno2 = float(input()) #quando o input for do tipo real primeiro declaramos o "float ou real" para depois inserir a entrada do dado

print(f"Qual o nome do terceiro aluno?")
aluno3 = input()
print(f"Qual a nota do terceiro aluno?")
notaaluno3 = float(input())

media = float(notaaluno1 + notaaluno2 + notaaluno3)/3 #sempre que o resultado for do tipo real, declaramos primeiro o float para depois entre parenteses calcularmos a soma e depois achar a média.
print(f"A média dos alunos é: {media}")