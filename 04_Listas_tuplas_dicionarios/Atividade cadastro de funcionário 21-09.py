# 4. Cadastro de funcionário
#Crie um programa para armazenar os dados de um funcionário utilizando um dicionário.
#O cadastro deverá possuir:
#1. Nome. X
#2. Idade. X
#3. Cargo. X
#4. Salário. X
#5. Setor. X

#O programa deverá:
#1. Exibir cada informação do funcionário. X
#2. Alterar o salário do funcionário. X
#3. Adicionar uma nova informação ao cadastro. X
#4. Remover uma informação do cadastro. X
#5. Verificar se determinada chave existe. X
#6. Percorrer o dicionário exibindo as chaves e seus respectivos valores. X

funcionario = {
    "nome": "Pietro",
    "idade": 25,
    "cargo": "Programador",
    "salario": 3500,
    "setor": "Tecnologia"
}

print("Nome: ")
print(funcionario["nome"])

print("Idade: ")
print(funcionario["idade"])

print("Cargo: ")
print(funcionario["cargo"])

print("Salário: ")
print(funcionario["salario"])

print("Setor: ")
print(funcionario["setor"])

funcionario["salario"] = 3000

print("Novo salário: ")
print(funcionario["salario"])

funcionario["email"] = "pietro123@email.com"

print("Cadastro com nova informação: ")
print(funcionario)

funcionario.pop("idade")

print("Cadastro após remover a idade: ")
print(funcionario)

if "cargo" in funcionario:
    print("A chave cargo existe no cadastro")
else:
    print("A chave cargo não existe no cadastro")

print("Informações do funcionário: ")

for chave in funcionario:
    print(chave, ":", funcionario[chave])
