class Receita:
    def __init__(self, valor, descricao, categoria):
        self.tipo = "Receita"
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def dicionario(self):
        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "descricao": self.descricao,
            "categoria": self.categoria
        }

class Despesa:
    def __init__(self, valor, descricao, categoria):
        self.tipo = "Despesa"
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def dicionario(self):
        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "descricao": self.descricao,
            "categoria": self.categoria
        }