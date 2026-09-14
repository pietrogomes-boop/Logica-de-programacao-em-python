# 1. Estrutura condicionais

nota = 6

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')

# 2. Condições com operadores lógicos

# AND -> Todas as condições devem ser verdadeiras
# OR -> Pelo menos uma condição deve ser verdadeira
# NOT -> Inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print('Entrada permitida')
else:
    print('Entrada não permitida')

# 3. Estrutura de repetição

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# 4. Estrutura de repetição for

for numero in range(1, 6):
    print(numero)

# 5. Percorrendo uma lista

nomes = ["Ana","Carlos","João","Maria"]

for nome in nomes:
    print(nome)

# 6. Break
#O break interrompe completamente a repetição
#O Pass não executa nenhuma ação
#O Continue, interrompe apenas a repetição atual

for numero in range(1,11):
    if numero == 7:
        #break
        #pass
        continue
    print(numero)

# 7. Condição dentro de repetição

for numero in range(1,11):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")