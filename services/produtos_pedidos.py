class Pedido:
    contador_pedidos = 0

    def __init__(self):
        Pedido.contador_pedidos += 1
        self.numero_pedido = Pedido.contador_pedidos
        self.pizzas = []

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total(self):
        return sum(pizza.calcular_preco_final() for pizza in self.pizzas)

    def exibir_detalhes_pedido(self):
        detalhes = f"Pedido Número: {self.numero_pedido}\nPizzas no Pedido:\n"
        for pizza in self.pizzas:
            detalhes += pizza.exibir_detalhes() + "\n\n"
        detalhes += f"Total do Pedido: R${self.calcular_total():.2f}"
        return detalhes


def mostrar_sabores(sabores):
    print("\nSabores disponíveis:")
    for i, sabor in enumerate(sabores, start=1):
        print(f"{i}. {sabor}")


def escolher_sabor(sabores):
    mostrar_sabores(sabores)
    sabor_idx = int(input("Escolha o número do sabor: ")) - 1
    if 0 <= sabor_idx < len(sabores):
        return sabores[sabor_idx]
    else:
        print("Número do sabor inválido.")
        return None


def escolher_tamanho(tamanhos_precos):
    print("\nTamanhos disponíveis:")
    for tamanho, preco in tamanhos_precos.items():
        print(f"{tamanho}: R${preco:.2f}")
    tamanho = input("Escolha o tamanho (Pequena, Média, Grande): ")
    return tamanhos_precos.get(tamanho)

