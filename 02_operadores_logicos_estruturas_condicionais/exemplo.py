#AULA: Operadores lógicos  e estruturas condicionais
# 1. Operadores lógicos

# and
# Todas as condições precisam ser verdadeiras.

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)


#or
#Pelo menos uma condição precisa ser verdadeira.

idade = 16
possui_carteira = True

resultado = idade >= 18 or possui_carteira
print(resultado)

#not
#inverte o resultado de uma condição.

aluno_matriculado = True
print(not aluno_matriculado)



# 2. Operadores de comparação

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)



# 3. estrutura if

if idade >= 18:
    print("Maior de idade")

# 4. estrutura if / else

idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
