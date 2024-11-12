# finalizar_compra.py

# Importando o carrinho de compras do arquivo carrinho.py
from Carrinho import carrinho

def calcular_frete(cep):
    """Calcula o valor do frete baseado no CEP"""
    # Para simplificação, vamos fazer uma correspondência com os primeiros números do CEP
    if cep.startswith('010') or cep.startswith('020'):
        return 15.00  # Frete para São Paulo (simulado)
    elif cep.startswith('030') or cep.startswith('040'):
        return 30.00  # Frete para Rio de Janeiro (simulado)
    elif cep.startswith('050') or cep.startswith('060'):
        return 45.00  # Frete para outras regiões (simulado)
    else:
        return 60.00  # Frete para locais mais distantes (simulado)

def exibir_resumo_compra():
    """Exibe o resumo da compra e calcula o total com o frete"""
    if carrinho:
        total_produtos = sum([produto['preco'] for produto in carrinho])
        print("\nResumo da Compra:")
        for produto in carrinho:
            print(f"{produto['nome']} - R${produto['preco']:.2f}")
        
        print(f"\nTotal dos produtos: R${total_produtos:.2f}")
        
        # Solicitando o CEP
        cep = input("\nDigite o seu CEP (somente números): ").strip()
        
        # Calculando o valor do frete com base no CEP
        frete = calcular_frete(cep)
        print(f"Frete para o CEP {cep}: R${frete:.2f}")
        
        # Calculando o valor total da compra
        total_com_frete = total_produtos + frete
        print(f"\nValor total com frete: R${total_com_frete:.2f}")
        
        # Escolhendo a forma de pagamento
        forma_pagamento = escolher_forma_pagamento()
        
        # Exibindo o resumo final da compra
        print("\nResumo Final:")
        print(f"Total da compra: R${total_com_frete:.2f}")
        print(f"Forma de pagamento escolhida: {forma_pagamento}")
        print("Pagamento processado com sucesso!\n")

    else:
        print("\nO carrinho está vazio. Não há produtos para calcular a compra.")

def escolher_forma_pagamento():
    """Permite ao usuário escolher uma forma de pagamento"""
    print("\nEscolha a forma de pagamento:")
    print("1. Cartão de Crédito")
    print("2. Boleto Bancário")
    print("3. Pix")
    
    while True:
        opcao_pagamento = input("Escolha uma opção (1, 2, 3): ")
        if opcao_pagamento == "1":
            return "Cartão de Crédito"
        elif opcao_pagamento == "2":
            return "Boleto Bancário"
        elif opcao_pagamento == "3":
            return "Pix"
        else:
            print("Opção inválida. Tente novamente.")

def main():
    """Função principal para finalizar a compra"""
    exibir_resumo_compra()

if __name__ == "__main__":
    main()
