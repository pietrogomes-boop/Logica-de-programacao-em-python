# 3. Informações de um produto
#Crie um programa para armazenar informações de um produto utilizando uma tupla. A tupla deverá armazenar:
#1. Nome do produto. X
#2. Categoria. X
#3. Preço. X
#4. Código do produto. X

#O programa deverá:
#1. Exibir cada informação individualmente. X
#2. Exibir todas as informações utilizando uma estrutura de repetição. X
#3. Informar a quantidade de informações armazenadas. X
#4. Tentar alterar uma das informações da tupla. X
#5. Observar e explicar o que acontece ao tentar modificar um elemento. X

Produto = ("sorvete", "cremoso", 15.90, 12345)
itens= 0

print(f"Nome do produto:  {Produto[0]}")
print(f"Categoria: {Produto[1]}")
print(f"Preço: {Produto[2]}")
print(f"Codigo: {Produto[3]}")

for informacao in Produto:
    print(informacao)

print(f"Quantidade de informações armazenadas: {len(Produto)}")

#Produto[0] = "Picolé"
#print(Produto[0])
#Não pode alterar informações de tuplas.
#Se tentar alterar aparece o seguinte erro:
#TypeError: 'tuple' object does not support item assignment