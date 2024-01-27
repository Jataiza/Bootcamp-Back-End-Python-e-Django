# Crie um programa que solicite ao usuário um login e uma senha. O programa deve
# permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.


login = input("login: ")
senha = input("senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido!")
else:
    print("Login e/ou senha inválidos!")
