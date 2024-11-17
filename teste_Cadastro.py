import pytest
from unittest.mock import patch
from io import StringIO

from Cadastro import adicionar_cliente, obter_dados, buscar_cliente_por_email

# Aqui você define as funções do seu código
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


# Testes

def test_adicionar_cliente():
    """Teste da função adicionar_cliente"""
    clientes.clear()  # Limpa a lista de clientes antes do teste
    adicionar_cliente("teste@exemplo.com", "senha123")
    
    # Verifica se o cliente foi adicionado corretamente
    assert len(clientes) == 1
    assert clientes[0]["email"] == "teste@exemplo.com"
    assert clientes[0]["senha"] == "senha123"

def test_buscar_cliente_por_email():
    """Teste da função buscar_cliente_por_email"""
    clientes.clear()
    adicionar_cliente("teste@exemplo.com", "senha123")
    
    # Verifica se a busca retorna o cliente correto
    cliente = buscar_cliente_por_email("teste@exemplo.com")
    assert cliente is not None
    assert cliente["email"] == "teste@exemplo.com"
    
    # Verifica que o email não existe na lista
    cliente_inexistente = buscar_cliente_por_email("inexistente@exemplo.com")
    assert cliente_inexistente is None

def test_obter_dados_com_input_simulado():
    """Teste da função obter_dados simulando o input"""
    clientes.clear()
    
    # Usamos patch para simular os inputs do usuário
    with patch('builtins.input', side_effect=["teste@exemplo.com", "senha123"]):
        obter_dados()
    
    # Verifica se o cliente foi adicionado após o input simulado
    assert len(clientes) == 1
    assert clientes[0]["email"] == "teste@exemplo.com"
    assert clientes[0]["senha"] == "senha123"
