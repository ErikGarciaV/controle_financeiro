from classes import Receita
import json

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
    valor = int(input("\nDigite um valor: ")) 

    if valor == 0:
        menu_inicial()
        return

    descricao = input("\nEscreva uma descrição: ")
    categoria = input("\nA qual categoria essa receita faz parte? ")
    
    if valor > 0  and descricao != "" and categoria != "":
        with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
            dados = json.load(movimentacoes)
            receita = Receita(valor, descricao, categoria)
            dados.append(receita.dicionario())

            with open("movimentacoes.json", "w", encoding="utf-8") as movimentacoes:
                    json.dump(dados, movimentacoes, ensure_ascii=False, indent=4)
    else:
         print(input("\nErro: Todos os campos devem ser preenchidos com valores válidos, pressione Enter para continuar."))
while True:
    escolha = menu_inicial()
    if escolha == 1:
        menu_receita()






        