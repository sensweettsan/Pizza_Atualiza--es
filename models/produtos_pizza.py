class Pizza:
    def __init__(self, nome, tamanho, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco

    def calcular_preco_final(self):
        """Calcula o preço final da pizza considerando o tamanho."""
        if self.tamanho == 'Pequena':
            return self.preco
        elif self.tamanho == 'Média':
            return self.preco * 1.2
        elif self.tamanho == 'Grande':
            return self.preco * 1.5
        else:
            raise ValueError("Tamanho inválido. Escolha entre 'Pequena', 'Média' ou 'Grande'.")

    def exibir_detalhes(self):
        """Exibe os detalhes da pizza."""
        preco_final = self.calcular_preco_final()
        return f"Pizza: {self.nome}\nTamanho: {self.tamanho}\nPreço Final: R${preco_final:.2f}"
