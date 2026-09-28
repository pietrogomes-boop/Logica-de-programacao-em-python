## 2. Controle de notas
#Crie um programa para armazenar as notas de um estudante. O programa deverá:

# 1. Criar uma lista contendo 5 notas. X
# 2. Exibir todas as notas. X
# 3. Calcular a soma das notas. X
# 4. Calcular a média das notas. X
# 5. Identificar a maior nota. X
# 6. Identificar a menor nota. X
# 7. Verificar se existe uma nota igual a 10. X
# 8. Informar se o estudante foi aprovado ou reprovado. X
# 9. Considerar média igual ou superior a 7 como aprovação. X


notas = [6.0,7.5,8.7,5.5,9.7]
print(notas)

mediafinal = 7.0
menornota = 10
maiornota = 0
soma =  0

for nota in notas:
    soma = soma + nota

print(f"soma: {soma}")

media = soma/len(notas)
print(f"media: %.2f" % media)

if notas >= maiornota:
    maiornota = notas

print(f"Maior nota: {maiornota}")

if notas <= menornota:
    menornota = notas

print(f"Menor nota: {maiornota}")

if notas == 10:
    print("Existe uma nota 10!")


if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")