# 5. Sistema de estoque
#Uma loja de informática deseja organizar seu estoque.
#Crie uma estrutura utilizando uma lista de dicionários para armazenar pelo menos 5 produtos. Cada produto deverá possuir:
#1. Nome.
#2. Categoria.
#3. Preço.
#4. Quantidade em estoque.

#O programa deverá:
#1. Exibir todos os produtos cadastrados.
#2. Exibir o nome, preço e quantidade em estoque de cada produto.
#3. Calcular a quantidade total de itens armazenados no estoque.
#4. Calcular o valor total do estoque.
#5. Identificar os produtos que possuem menos de 10 unidades disponíveis.
#6. Verificar se determinado produto está cadastrado.
#7. Alterar a quantidade em estoque de um produto.
#8. Adicionar um novo produto.
#9. Exibir um relatório final com todos os produtos e suas respectivas informações.

estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 5500,
        "quantidade": 10
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 100,
        "quantidade": 35
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 190,
        "quantidade": 79
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1600,
        "quantidade": 18
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 240,
        "quantidade": 90
    }
]

print("\nProdutos cadastrados: ")
print(estoque)

print("\nInformações dos produtos: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()

quantidade_total = 0

for produto in estoque:
    quantidade_total = quantidade_total + produto["quantidade"]

print(f"A quantidade total de itens no estoque é: {quantidade_total}")

valor_total = 0

for produto in estoque:
    valor = produto["preco"] * produto["quantidade"]
    valor_total = valor_total + valor

print(f"\nO valor total do estoque é: R$ {valor_total}")

print("\nProdutos com menos de 10 unidades: ")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])

nome_produto = "Mouse"

encontrado = False

for produto in estoque:
    if produto["nome"] == nome_produto:
        encontrado = True

if encontrado:
    print(f"\n{nome_produto} está cadastrado")
else:
    print(f"\n{nome_produto} não está cadastrado")

for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 20

print("\nQuantidade do Mouse alterada.")

novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 300,
    "quantidade": 6
}

estoque.append(novo_produto)

print("\nRelatório final do estoque: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("-------------------------")