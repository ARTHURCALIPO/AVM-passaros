# Importando a lista de produtos do arquivo produtos.py
from Produtos import produtos

# Lista para armazenar os produtos no carrinho
carrinho = []

def mostrar_produtos():
    """Exibe os produtos disponíveis para compra"""
    print("\nProdutos disponíveis:")
    for idx, produto in enumerate(produtos, 1):
        print(f"{idx}. {produto['nome']} - R${produto['preco']:.2f}")

def adicionar_ao_carrinho(indice):
    """Adiciona o produto selecionado ao carrinho"""
    if 0 < indice <= len(produtos):
        produto = produtos[indice - 1]
        carrinho.append(produto)
        print(f"{produto['nome']} foi adicionado ao carrinho!")
    else:
        print("Seleção inválida! Tente novamente.")

def exibir_carrinho():
    """Exibe os produtos no carrinho"""
    if carrinho:
        print("\nCarrinho de Compras:")
        for produto in carrinho:
            print(f"{produto['nome']} - R${produto['preco']:.2f}")
        total = sum([produto['preco'] for produto in carrinho])
        print(f"Total: R${total:.2f}")
    else:
        print("\nO carrinho está vazio!")

def main():
    """Função principal para interação com o usuário"""
    while True:
        mostrar_produtos()
        
        print("\nOpções:")
        print("1. Adicionar produto ao carrinho")
        print("2. Exibir carrinho")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2, 3): ")
        
        if opcao == "1":
            try:
                produto_escolhido = int(input("Digite o número do produto que deseja adicionar: "))
                adicionar_ao_carrinho(produto_escolhido)
            except ValueError:
                print("Entrada inválida! Digite um número.")
        
        elif opcao == "2":
            exibir_carrinho()
        
        elif opcao == "3":
            print("Saindo... Obrigado por comprar conosco!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")