#Crie um classe que modele o objeto "carro"
#Um carro tem os seguintes atributos: ligado, cor, modelo,
#velocidade.
#Um carro tem os seguintes comportamentos: liga, desliga, acelera,
#desacelera.
#Crie uma instância da classe carro.
#Faça o carro "acelerar" utilizando os métodos da sua classe.
#Faça o carro "desacelerar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, ligado, cor, modelo, velocidade):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar(self):
        if self.ligado:
            print("Seu carro está ligado")
        else:
            print("Seu carro está ligado, Ok")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Seu carro está desligado")
        else:
            print("Seu carro está desligado, Ok")
            self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade} km/h")
        else:
            print("Não é possível acelerar")

    def desacelerar(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade} km/h")
        else:
            print("Não é possível desacelerar")



    
    
    
        
