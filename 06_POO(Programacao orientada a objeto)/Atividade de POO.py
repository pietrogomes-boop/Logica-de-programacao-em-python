class Cachorro:
    def __init__(self , nome , raca , idade , latir= True):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.latir = latir


    def latir1(self):
        if self.latir == True:
            print("Enzo diz: Au Au!")
        else:
            self.ligado = False
            print(f"{self.nome} não late!")

    def mostrar(self):
        print(self.nome, self.raca, self.idade)

enzo = Cachorro('Enzo','Poodle', '10')

rex = Cachorro ( 'Rex', 'Dalmata', '8')


print(enzo.nome)


enzo.idade = 4
print(enzo.idade)

enzo.latir1()
enzo.mostrar()