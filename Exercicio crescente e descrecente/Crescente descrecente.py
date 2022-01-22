print("Digite dois números: ")
x = int(input())
y = int(input())
while x != y:
    if x < y:
        print("Crescrecente!")
    else:
        print("Decrescente!")
    print("Digite mais dois números: ")
    x = int(input())
    y = int(input())