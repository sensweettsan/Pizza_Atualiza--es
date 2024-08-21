from models.produtos_pizza import Pizza
from models.produtos_especiais import PizzaEspecial
from services.produtos_pedidos import Pedido, escolher_sabor, escolher_tamanho

def main():
    pedido = Pedido()

    tabela_precos = {
        "Pequena": 45.00,
        "Média": 50.00,
        "Grande": 75.00
    }

    tabela_sabores = [
        "Margherita",
        "Calabresa",
        "Quatro Queijos",
        "Pepperoni",
        "Frango com Catupiry",
        "Portuguesa"
    ]

    while True:
        print("\n--- Menu de Opções ---")
        print("1. Adicionar Pizza Simples")
        print("2. Adicionar Pizza Especial")
        print("3. Exibir Detalhes do Pedido")
        print("4. Finalizar Pedido")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sabor = escolher_sabor(tabela_sabores)
            if sabor:
                tamanho = escolher_tamanho(tabela_precos)
                if tamanho:
                    preco = tabela_precos[tamanho]
                    pizza = Pizza(sabor, tamanho, preco)
                    pedido.adicionar_pizza(pizza)
                    print("Pizza adicionada ao pedido!")

        elif opcao == "2":
            sabor = escolher_sabor(tabela_sabores)
            if sabor:
                tamanho = escolher_tamanho(tabela_precos)
                if tamanho:
                    adicionais = input("Digite os adicionais separados por vírgula (ou deixe em branco para nenhum): ")
                    lista_adicionais = [adicional.strip() for adicional in adicionais.split(",")] if adicionais else []
                    preco = tabela_precos[tamanho]
                    pizza_especial = PizzaEspecial(sabor, tamanho, preco, lista_adicionais)
                    pedido.adicionar_pizza(pizza_especial)
                    print("Pizza especial adicionada ao pedido!")

        elif opcao == "3":
            print("\n--- Detalhes do Pedido ---")
            print(pedido.exibir_detalhes_pedido())

        elif opcao == "4":
            print("\nFinalizando pedido...")
            print(pedido.exibir_detalhes_pedido())
            print("Pedido finalizado. Obrigado!")s
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()