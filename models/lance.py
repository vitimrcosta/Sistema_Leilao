from datetime import datetime

class Lance:
    def __init__(self, valor: float, participante, leilao, data_hora: datetime):
        self.valor = valor
        self.participante = participante  # Objeto da classe Participante
        self.leilao = leilao              # Objeto da classe Leilao
        self.data_hora = data_hora

    def __str__(self):
        return f"Lance de R${self.valor:.2f} por {self.participante.nome}"