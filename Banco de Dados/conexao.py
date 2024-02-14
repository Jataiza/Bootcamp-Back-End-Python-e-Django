import sqlite3

conexao = sqlite3.connect('escola')
cursor=conexao.cursor()

#------------------------COMANDO PARA CRIAÇÃO DE TABELA--------------------------------------------------#

cursor.execute('CREATE TABLE alunos(id INT,Nome VARCHAR(100),idade INT,curso VARCHAR(100))')

#------------------------COMANDO PARA INSERIR DADOS NA TABELA--------------------------------------------#
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(1,"Isadora",18,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(2,"Marcos",28,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(3,"Fernanda",25,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(4,"Daniel",23,"Engenharia Civil")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(5,"Matheus",32,"Fisica")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(6,"Maria",19,"Sistemas de Informação")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(7,"Eduarda",37,"Astronomia")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(8,"Gabriel",30,"Banco de dados")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(9,"Joao",27,"Arquitetura e Urbanismo")')
cursor.execute('INSERT INTO alunos(id,Nome,idade,curso)VALUES(10,"Lara",19,"Engenharia Biomédica")')

#------------------------COMANDO DE CONSULTAS BÁSICAS-----------------------------------------------------#

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#        print(alunos)

#------------------------MOSTRANDO ALUNOS COM MAIS DE 20 ANOS ---------------------------------------------#

#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20 ')
#for alunos in dados:
#        print(alunos)

#------------------------MOSTRANDO ALUNOS DE ENGENHARIA EM ORDEM ALFABÉTICA --------------------------------#

#dados = cursor.execute("SELECT nome,curso FROM alunos WHERE curso = 'Engenharia' ORDER BY nome ASC")
#for alunos in dados:
#        print(alunos)

#------------------------ CONTAR O NUMERO DE ALUNOS NA TABELA ----------------------------------------------#       

#dados = cursor.execute("SELECT COUNT (*) FROM alunos ")
#for alunos in dados:
#       print(alunos)

#------------------------ ATUALIZANDO IDADE ---------------------------------------------------------------#       

#cursor.execute("UPDATE alunos SET idade = 26 WHERE nome = 'Marcos'")

#------------------------ REMOVER ALUNO ---------------------------------------------------------------# 

#cursor.execute('DELETE FROM alunos WHERE id=1')

 
conexao.commit()
conexao.close

