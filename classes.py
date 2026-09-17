class Receita():
    def __init__(self, valor, descricao, categoria):
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def dicionario(self):
        return {
            "valor": self.valor,
            "descricao": self.descricao,
            "categoria": self.categoria
        }