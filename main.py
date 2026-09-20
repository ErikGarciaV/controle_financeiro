from classes import Receita, Despesa
import json

with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
    dados = json.load(movimentacoes)
    saldo = 0
    for movimentacao in dados:
        if movimentacao["tipo"] == "Receita":
            saldo += movimentacao["valor"]
        elif movimentacao["tipo"] == "Despesa":
            saldo -= movimentacao["valor"] 

def menu_inicial():
    print("""
CONTROLE FINANCEIRO

1 - Adicionar receita
2 - Adicionar despesa
3 - Listar movimentações
4 - Ver saldo
5 - Ver relatório
6 - Sair
 """)

    escolha = int(input("Digite um numero: "))
    return escolha

def menu_receita():
    print("\nAdicionar Receita\n\nDigite 0 para voltar")
    valor = float(input("\nDigite um valor: ")) 

    if valor == 0:
        menu_inicial()
        return

    descricao = input("\nEscreva uma descrição: ").lower()
    categoria = input("\nA qual categoria essa receita faz parte? ").lower()
    
    if valor > 0  and descricao != "" and categoria != "":
        with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
            dados = json.load(movimentacoes)
            receita = Receita(valor, descricao, categoria)
            dados.append(receita.dicionario())

            with open("movimentacoes.json", "w", encoding="utf-8") as movimentacoes:
                    json.dump(dados, movimentacoes, ensure_ascii=False, indent=4)
    else:
         print(input("\nErro: Todos os campos devem ser preenchidos com valores válidos, pressione Enter para continuar."))
def menu_despesa():
    print("\nAdicionar Despesa\n\nDigite 0 para voltar")
    valor = float(input("\nDigite um valor: ")) 

    if valor == 0:
        menu_inicial()
        return

    descricao = input("\nEscreva uma descrição: ").lower()
    categoria = input("\nA qual categoria essa despesa faz parte? ").lower()

    if valor > 0 and descricao != "" and categoria != "":
        with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
            dados = json.load(movimentacoes)
            despesa = Despesa(valor, descricao, categoria)
            dados.append(despesa.dicionario())
            with open("movimentacoes.json", "w", encoding="utf-8") as movimentacoes:
                json.dump(dados, movimentacoes, ensure_ascii=False, indent=4)
    else:
        print(input("\nErro: Todos os campos devem ser preenchidos com valores válidos, pressione Enter para continuar."))

def menu_listar():
    with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
        dados = json.load(movimentacoes)

        for movimetacao in dados:
            print(f"{movimetacao['tipo']} \n    valor: R${movimetacao['valor']} \n    descrição: {movimetacao['descricao']} \n    categoria: {movimetacao['categoria']}")
    input("\nPressione ENTER para continuar...")

def menu_saldo():
    print(f"seu saldo é de: R${saldo}")
    input("\nPressione ENTER para continuar...")

    
while True:
    escolha = menu_inicial()
    if escolha == 1:
        menu_receita()     
    elif escolha == 2:
        menu_despesa()  
    elif escolha == 3:
        menu_listar()
    elif escolha == 4:
        menu_saldo()