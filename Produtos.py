# Produtos.py

produtos = [
    {"nome": "Açúcar de Uva 500G", "preco": 34.00},
    {"nome": "Arara 5 KG", "preco": 120.00},
    {"nome": "Bambito Extrusado 5 KG", "preco": 106.00},
    {"nome": "Bambito Mix 5 KG", "preco": 80.00},
    {"nome": "Bio Classic Amarela 1 KG", "preco": 32.00},
    {"nome": "Bio Classic Branca 1 KG", "preco": 24.00},
    {"nome": "Frutas e Cereais 5 KG", "preco": 78.00},
    {"nome": "Gran Mix 20 de 5 KG", "preco": 96.00},
    {"nome": "Nativos 500G", "preco": 12.00},
    {"nome": "Saporito Mix 500G", "preco": 12.00},
    # Outros produtos omitidos para simplicidade
]

def listar_produtos():
    """Retorna todos os produtos disponíveis."""
    return produtos

def buscar_produto(nome):
    """Buscar um produto pelo nome."""
    for produto in produtos:
        if nome.lower() in produto["nome"].lower():
            return produto
    return None
