from abc import ABC, abstractmethod
from datetime import date, timedelta
# Classe base
class Registro(ABC):
    def __init__(self, livro, usuario, estado, id_exemplar):
        self.livro = livro
        self.usuario = usuario
        self.estado = estado
        self.id_exemplar = id_exemplar

    @abstractmethod
    def definir_data_de_emprestimo(self):
        pass
    
    @abstractmethod
    def definir_data_de_devolucao(self):
        pass

    def __str__(self):
        return f'----- REGISTRO -----\nLivro: {self.livro.titulo}\tID: {self.id_exemplar}\nEstado: {self.estado}\nUsuario: {self.usuario._nome}'

class RegistroEmprestimo(Registro):
    def __init__(self, livro, usuario, estado, id_exemplar):
        super().__init__(livro, usuario, estado, id_exemplar)
        self.data_de_emprestimo = self.definir_data_de_emprestimo()
        self.data_de_devolucao = self.definir_data_de_devolucao()

    def definir_data_de_emprestimo(self):
        return date.today()
    
    def definir_data_de_devolucao(self):
        prazo = timedelta(7)
        return self.data_de_emprestimo + prazo
        

class RegistroDevolucao(Registro):
    def __init__(self, livro, usuario, estado, id_exemplar, registro_emprestimo):
        super().__init__(livro, usuario, estado, id_exemplar)
        self.registro_emprestimo = registro_emprestimo
        self.data_de_emprestimo = self.definir_data_de_emprestimo()
        self.data_de_devolucao = self.definir_data_de_devolucao()

    def definir_data_de_emprestimo(self):
        return self.registro.data_de_emprestimo
    
    def definir_data_de_devolucao(self):
        return date.today()
