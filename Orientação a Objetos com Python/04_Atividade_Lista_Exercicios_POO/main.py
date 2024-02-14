from enum import Enum
from registro import *

class Generos(Enum):
    ROMANCE = 'Romance'
    MISTERIO = 'Mistério'
    FANTASIA = 'Fantasia'
    FICCAO_CIENTIFICA = 'Ficção Ciêntífica'
    TERROR = 'Terror'
    SUSPENSE = 'Suspense'
    JOVEM_ADULTO = 'Jovem Adulto'

class Estados(Enum):
    EMPRESTADO = 'Emprestado'
    DEVOLVIDO = 'Devolvido'
    RENOVADO = 'Renovado'

# Herança
class Pessoa:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade
    
class Autor(Pessoa):
    def __init__(self, nome, nacionalidade):
        super().__init__(nome, nacionalidade)

class Usuario(Pessoa):
    def __init__(self, nome, nacionalidade, telefone):
        super().__init__(nome, nacionalidade)
        self.telefone = telefone
    

class Livro():
    def __init__(self, titulo, editora, generos, autores):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = autores
        self.limitado = False
        self.limite_de_renovacoes = 0
        self.exemplares_disponiveis = []

    def adiciona_exemplar(self, id):
        self.exemplares_disponiveis.append(id)

    def _retira_exemplar(self):
        if self.conta_exemplares_disponiveis() > 0:
            id_exemplar = self.exemplares_disponiveis.pop()
            return id_exemplar
        else:
            return None
    
    def conta_exemplares_disponiveis(self):
        return len(self.exemplares_disponiveis)
    
    def define_limite_renovacao(self, limite):
        self.limitado = True
        self.limite_de_renovacoes = limite

class Biblioteca:
    def __init__(self):
        self.autores = []
        self.livros = []
        self.usuarios = []
        self.registros = []
    
    def adiciona_autor(self, nome, nacionalidade):
        autor = Autor(nome, nacionalidade)
        self.autores.append(autor)
    
    def busca_autor(self, nome):
        for autor in self.autores:
            if autor._nome == nome:
                return autor
            else:
                return None
            
    def adiciona_livro(self, titulo, editora, generos, autores):
        livro = Livro(titulo, editora, generos, autores)
        self.livros.append(livro)

    def busca_livro(self, nome):
        for livro in self.livros:
            if livro.titulo == nome:
                return livro
            else:
                return None

    def adiciona_usuario(self, nome, nacionalidade, telefone):
        usuario = Usuario(nome, nacionalidade, telefone)
        self.usuarios.append(usuario)
    
    def busca_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario._nome == nome:
                return usuario
            else:
                return None
    
    def empresta_livro(self, livro: Livro, usuario: Usuario):
        if len(self.livros) > 0 and len(self.usuarios) > 0:
            exemplar_id = livro._retira_exemplar()
            if exemplar_id is None:
                print('Não há exemplares disponíveis para empréstimo')
            else:
                print('Empréstimo realizado com sucesso!')
                emprestimo = RegistroEmprestimo(livro, usuario, Estados.EMPRESTADO.value, exemplar_id)
                self.registros.append(emprestimo)
                print(emprestimo)
        else:
            print('Requisitos necessários para a operação não atendidos.')
            
    def devolve_livro(self, livro: Livro, usuario: Usuario):
        pass


biblioteca = Biblioteca()
biblioteca.adiciona_autor('Joseph Sheridan Le Fanu', 'Irlandês')
biblioteca.adiciona_livro('Carmilla', 'Pandorga', [Generos.ROMANCE, Generos.TERROR], [biblioteca.autores[0]])
biblioteca.adiciona_usuario('Júlia', 'Brasileira', '98 989898998')
biblioteca.livros[0].adiciona_exemplar(1)
livro = biblioteca.busca_livro('Carmilla')
usuario = biblioteca.busca_usuario('Júlia')
biblioteca.empresta_livro(livro, usuario)

