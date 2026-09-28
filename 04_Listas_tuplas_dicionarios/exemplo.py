#Listas, tuplas e dicionarios

# 01. Listas
#Listas são utilizadas para armazenar varios valores dentro de uma unica variavel

nomes = ["ana","carlos","joão","Maria"]
print(nomes)

# 02. Acessando elementos

print(nomes[3])

#Podemos acessar o ultimo elemento usando o -1
print(nomes[-1])

# 03. Alterando elementos

nomes[0] = "Pedro"
print(nomes)

# 04. Adicionar elementos

#append adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição especifica

nomes.insert(1,"Mariana")
print(nomes)

# 05. Removendo elementos
#Remove um elemento pelo valor

nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice

nomes.pop(0)
print(nomes)

# 06. Tamanho da lista
#Len() informa a quantidade de elementos
print(len(nomes))

# 07. Percorrendo uma lista

for nome in nomes:
    print(nome)

# 08. Verificando se um elemento existe

if "joão" in nomes:
    print("joão está na lista")
else:
    print("joão não está na lista")

# 09. Lista com diferentes tipos de dados

dados = ["joão", 18, 1.75, True]
print(dados)

# 10. Lista de numeros

notas = [7.5,8.0,6.5,9.0]

soma =  0

for nota in notas:
    soma = soma + nota

media = soma/len(notas)
print(f"media: {media}")

# 11. Tuplas
#Tuplas são semelhantes as linhas
#As tuplas não podem ser alteradas

coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0])

# 12. Dicionários
# Dicioanrios armazenam informações no formato: chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5

}
print(aluno)


# 13. Acessando os valores do dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# 14. Alterando os valores

aluno["nota"] = 9.0
print(aluno)


# 15. Adicionando novos dados

aluno["curso"] = "Informática"
print(aluno)

# 16. Removendo dados

del aluno["curso"]
print(aluno)


# 17. Percorrendo um dicionário

for chave in aluno:
    print(chave)

#Podemos acessar chave e valor ao mesmo tempo.

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# 18. Verificando uma chave

if "nome" in aluno:
    print("A chave nome existe.")

# 19. Dicionário com lista

aluno = {
    "nome": "Maria",
    "notas": [8.0,7.5,9.0]
}