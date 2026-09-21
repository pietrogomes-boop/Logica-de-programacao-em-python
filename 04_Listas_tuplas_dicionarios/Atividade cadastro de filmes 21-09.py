## 1. Cadastro de filmes
#Crie um programa para organizar uma lista de filmes. O programa deverá:

# 1. Criar uma lista contendo inicialmente 5 filmes. X
# 2. Exibir todos os filmes cadastrados. X
# 3. Exibir o primeiro filme da lista. X
# 4. Exibir o último filme da lista. X
# 5. Adicionar um novo filme ao final da lista. X
# 6. Inserir um novo filme em uma posição específica. X
# 7. Remover um filme da lista. X
# 8. Alterar o nome de um dos filmes. X
# 9. Exibir a quantidade de filmes cadastrados. X
# 10. Verificar se um determinado filme está presente na lista.

lista = ["filme1", "filme2", "filme3", "filme4", "filme5"]
print(lista)

print(f"Primeiro item: {lista[0]}")
print(f"Último item: {lista[-1]}")

lista.append("filme6")
print(lista)

lista.insert(4, "filme4.2")
print(lista)

lista.pop(4)
print(lista)

lista[0] = "filme 1.2"
print(lista)

print(f"Quantidade de itens: {len(lista)}")

if "filme3" in lista:
    print("filme3 está na lista.")
else:
    print("filme3 não está na lista.")