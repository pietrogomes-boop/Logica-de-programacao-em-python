# A classe: o modelo (a planta)
class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#Os objetos: criados a partir da classe (as "casas")

#Criação de objeto (Celular1) da classe celular
celular1 = Celular ('Samsung','Galaxy S23', 'preto')

Celular2 = Celular( 'Motorola', 'MotoG', 'azul', 30)

#Acessando e alterando atributos
print(Celular2.marca)


#Tambem podemos alterar diretamente
celular1.cor = 'branco'
print(celular1.cor)

#Chamando metodos
celular1.ligar()