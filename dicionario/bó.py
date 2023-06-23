pessoa = {}

while True:
    chave = str(input("coloque um elemento que deseja adicionar:"))
    pessoa[chave] = str(input("coloque o nome do item:"))

    res = int(input("digite 1 para sair:"))
    if res == 1:
        break

print(pessoa)