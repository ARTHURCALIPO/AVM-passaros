from Cadastro import buscar_cliente_por_email  # Importando a função para buscar um cliente pelo email

def recuperar_senha():
    """Função para o cliente visualizar se o email está cadastrado no sistema."""
    email = input("Digite seu email para verificar se está cadastrado: ")
    
    # Verifica se o email existe na lista de clientes
    cliente = buscar_cliente_por_email(email)
    
    if cliente:
        print(f"\nCliente encontrado! Email: {cliente['email']}, Senha: {cliente['senha']}")
        return True
    else:
        print("Email não encontrado. Verifique se o email está correto ou se o cadastro existe.")
        return False