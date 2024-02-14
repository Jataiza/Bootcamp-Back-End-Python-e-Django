import sqlite3

conexao = sqlite3.connect('comercio')
cursor=conexao.cursor()

#------------------------COMANDO PARA CRIAÇÃO DE TABELA--------------------------------------------------#
cursor.execute('CREATE TABLE clientes (id INT,Nome VARCHAR(100),idade INT,saldo FLOAT(30))')


#------------------------COMANDO PARA INSERIR DADOS NA TABELA--------------------------------------------#  

cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(1,"Maria",18,1.500)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(2,"joao",19,2.500)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(3,"Gustavo",20,3.500)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(4,"Gabriela",25,5.000)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(5,"Jessica",27,10.500)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(6,"kelly",30,8.130)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(7,"Isabella",38,6.250)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(8,"Jaqueline",50,11.500)')
cursor.execute('INSERT INTO clientes (id,Nome,idade,saldo)VALUES(9,"Maria Clara",18,1.500)')


#------------------------COMANDO DE CONSULTAS BÁSICAS-----------------------------------------------------#
#visualizar = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for cliente in visualizar:
#    print(cliente)


#------------------------MOSTRANDO O SALDO MÉDIO DOS CLIENTES-----------------------------------------------------#

#visualizar = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for cliente in visualizar:
#    print(cliente)

#------------------------MOSTRANDO O SALDO MÁXIMO DOS CLIENTES-----------------------------------------------------#
#visualizar = cursor.execute('SELECT id,nome,saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#for cliente in visualizar:
#   print(cliente)

#------------------------ CONTAR O NUMERO DE CLINTES COM SALDO DE 1.500---------------------------------------------#       

#visualizar = cursor.execute ('SELECT COUNT(*) FROM clientes WHERE saldo = 1.500')
#for cliente in visualizar:
#    print(cliente)

#------------------------ ATUALIZAR O SALDO---------------------------------------------#       

#visualizar = cursor.execute ('UPDATE clientes SET saldo=3.500 WHERE id=1')
#for cliente in visualizar:
#    print(cliente)

#------------------------ DELETAR PELO ID---------------------------------------------#      

#cursor.execute('DELETE FROM clientes WHERE id=9')

#------------------------ CRIAR A TABELA DE COMPRAS---------------------------------------------# 
#cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

#------------------------ INSERIR DADOS NA TABELA--------------------------------------------# 

#cursor.execute("INSERT INTO compras(cliente_id, produto, valor) VALUES (1, 'Produto A', 100.50), (2, 'Produto B', 75.25), (3, 'Produto C', 150.00)")

#------------------------ EXIBIR  DADOS DO CLIENTE--------------------------------------------# 


#cursor.execute('SELECT c.nome AS nome_cliente, co.produto, co.valor FROM compras co JOIN clientes c ON co.cliente_id = c.id')

# Obtém todos os resultados da consulta
#resultados = cursor.fetchall()

# Itera sobre os resultados e imprime cada linha
#for cliente in resultados:
#    print(cliente)


conexao.commit()
conexao.close
