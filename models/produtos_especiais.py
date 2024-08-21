from models.produtos_pizza import Pizza

class PizzaEspecial(Pizza):
    def __init__(self, nome, tamanho, preco, adicionais=None):
        super().__init__(nome, tamanho, preco)
        self.adicionais = adicionais if adicionais is not None else []

    def calcular_preco_final(self):
        """Calcula o preço final da pizza considerando o tamanho e os adicionais."""
        preco_base = super().calcular_preco_final()
        custo_adicionais = len(self.adicionais) * 2.50  # Cada adicional custa R$ 2,50
        return preco_base + custo_adicionais

    def exibir_detalhes(self):
        """Exibe os detalhes da pizza especial, incluindo os adicionais."""
        detalhes_base = super().exibir_detalhes()
        if self.adicionais:
            detalhes_adicionais = "\nAdicionais: " + ", ".join(self.adicionais)
        else:
            detalhes_adicionais = "\nAdicionais: Nenhum"
        return detalhes_base + detalhes_adicionais