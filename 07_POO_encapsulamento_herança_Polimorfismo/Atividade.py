#1. Veículos
#Crie uma classe mãe Veiculo cujo construtor receba marca e modelo. Todo veículo deve começar desligado.
#A classe Veiculo deve ter:
#ligar(): liga o veículo e mostra "Toyota Corolla ligado." (com a marca e o modelo do veículo).
#mostrar_info(): mostra a marca, o modelo e se o veículo está ligado ou desligado.
#Depois, crie duas classes filhas usando super().__init__():
#Carro: recebe também portas e tem o método abrir_porta_malas(), que mostra uma mensagem.
#Moto: recebe também cilindradas e tem o método empinar(), que só funciona se a moto estiver ligada.
#Crie um carro e uma moto. Mostre que os dois usam ligar() e mostrar_info() sem que esses métodos tenham sido escritos nas classes filhas. Teste também os métodos exclusivos de cada um.



class Veiculo:
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado!")
    def mostrar_info(self):
       if self.ligado == True:
           print(f"O {self.marca} {self.modelo} está ligado!")
       else:
            print(f"O {self.marca} {self.modelo} está desligado!")

# Carro: recebe também portas e tem o método abrir_porta_malas(), que mostra uma mensagem.

class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.portas = False
    def abrir_porta_malas(self):
        if self.portas == True:
        print(f"O carro {self.marca} {self.modelo} está com o porta malas aberto!")
        else:
        print(f"O carro {self.marca} {self.modelo} está com o porta malas fechado!")


#Moto: recebe também cilindradas e tem o método empinar(), que só funciona se a moto estiver ligada.

class: Moto(Veiculo):
   def __init__(self, marca, modelo, ligado, empinar):
      super().__init__(marca,modelo,ligado):
      self.marca = marca
      self.modelo = modelo
      self.ligado = False
      self.empinar = False

    def empinar(self):

