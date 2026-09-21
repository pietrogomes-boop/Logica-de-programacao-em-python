## 2. Controle de notas
#Crie um programa para armazenar as notas de um estudante. O programa deverá:

# 1. Criar uma lista contendo 5 notas. X
# 2. Exibir todas as notas. X
# 3. Calcular a soma das notas. X
# 4. Calcular a média das notas. X
# 5. Identificar a maior nota.
# 6. Identificar a menor nota.
# 7. Verificar se existe uma nota igual a 10.
# 8. Informar se o estudante foi aprovado ou reprovado.
# 9. Considerar média igual ou superior a 7 como aprovação.


notas = [6.0,7.5,8.7,5.5,9.7]
print(notas)

soma =  0

for nota in notas:
    soma = soma + nota

print(f"soma: {soma}")

media = soma/len(notas)
print(f"media: %.2f" % media)