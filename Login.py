from Cadastro import clientes  # Importando a função e a lista de clientes de cadastro.py

def realizar_login():
    """Função que realiza o login verificando se o cliente existe na lista de clientes."""
    email = input("Digite seu email para login: ")
    senha = input("Digite sua senha para login: ")

    # Verificar se o cliente existe na lista
    for cliente in clientes:
        if cliente["email"] == email and cliente["senha"] == senha:
            print("Login bem-sucedido!")
            return True  # Login bem-sucedido
    print("Email ou senha incorretos.")
    return False 