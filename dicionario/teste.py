#dicionario em python
pessoa = {"nome": "duda", "idade": 16, "altura": 1.50}

#cria
pessoa2 = dict()
pessoa2 = {"nome": "marcão",
           "idade": 17,
           "altura": 1.70}

#adiciona
pessoa["peso"] = 60

#deleta
del pessoa["peso"]

#substitui os elementos de um dicionario por outro
pessoa.update(pessoa2)


pessoa2["idade"] = 15

#para imprimir somento os valores
print(pessoa.values())

#imprime as chaves
print(pessoa.keys())

#coloca os valores em uma lista
print(pessoa.items())

#imprime em linha cada valor, chava ou os dois juntos
for k in pessoa.keys():
    print(k)

for v in pessoa.values():
    print(v)

for v, k in pessoa.items():
    print("o item :", k, "é", v)

#verificação
idade = int(input("digite sua idade"))

if idade == pessoa.values():
    print("voce tem a mesma idade que duda")

print(pessoa)
