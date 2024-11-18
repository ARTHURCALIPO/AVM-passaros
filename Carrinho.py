# Carrinho.py

from Produtos import produtos

carrinho = []

def adicionar_ao_carrinho(nome_produto, quantidade):
    """Adiciona um produto ao carrinho"""
    for produto in produtos:
        if produto["nome"] == nome_produto:
            carrinho.append({"produto": produto, "quantidade": quantidade})
            return f"{quantidade}x {produto['nome']} adicionado(s) ao carrinho"
    return "Produto não encontrado"

def remover_do_carrinho(nome_produto):
    """Remove um produto do carrinho"""
    for item in carrinho:
        if item["produto"]["nome"] == nome_produto:
            carrinho.remove(item)
            return f"{nome_produto} removido do carrinho"
    return "Produto não encontrado no carrinho"

def calcular_total():
    """Calcula o total do carrinho"""
    total = 0
    for item in carrinho:
        total += item["produto"]["preco"] * item["quantidade"]
    return total
