clientes = []

def adicionar_cliente(email, senha):
    # Adiciona o cliente como um dicionário na lista
    clientes.append({"email": email, "senha": senha})

def obter_dados():
    # Solicita os dados do cliente
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    # Chama a função para adicionar os dados na lista
    adicionar_cliente(email, senha)
    print("Dados adicionados com sucesso!")
    return True
    
def buscar_cliente_por_email(email):
    """Função para buscar um cliente na lista pelo email."""
    for cliente in clientes:
        if cliente["email"] == email:
            return cliente  # Retorna o cliente se o email for encontrado
    return None  # Retorna None se o email não for encontrado