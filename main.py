from datetime import datetime
from classes import Receita, Despesa
import json
import subprocess



def menu_inicial():
    subprocess.run("cls", shell=True)
    print("""
╔═══════════════════════════════╗
║      CONTROLE FINANCEIRO      ║ 
╠═══════════════════════════════╣
║1 - Adicionar receita          ║
║2 - Adicionar despesa          ║
║3 - Listar movimentações       ║
║4 - Ver saldo                  ║
║5 - Relatórios                 ║
║6 - Sair                       ║
╚═══════════════════════════════╝""")

    escolha = int(input("Digite um numero: "))
    return escolha

def menu_receita():
    subprocess.run("cls", shell=True)
    print("""
╔═══════════════════════════════╗
║       ADICIONAR RECEITA       ║ 
╠═══════════════════════════════╣
║   digite 0 se quiser voltar   ║
╚═══════════════════════════════╝""")
    valor = float(input("\nDigite um valor: ")) 

    if valor == 0:
        menu_inicial()
        return

    descricao = input("Escreva uma descrição: ").lower()
    categoria = input("A qual categoria essa receita faz parte? ").lower()
    
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
    subprocess.run("cls", shell=True)
    print("""
╔═══════════════════════════════╗
║       ADICIONAR DESPESA       ║ 
╠═══════════════════════════════╣
║   digite 0 se quiser voltar   ║
╚═══════════════════════════════╝""")
    valor = float(input("\nDigite um valor: ")) 

    if valor == 0:
        menu_inicial()
        return

    descricao = input("Escreva uma descrição: ").lower()
    categoria = input("A qual categoria essa despesa faz parte? ").lower()

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
    subprocess.run("cls", shell=True)
    with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
        dados = json.load(movimentacoes)
        tipo = ""
        for movimentacao in dados:
            if movimentacao["tipo"] == "Receita":
                tipo = "+"
            elif movimentacao["tipo"] == "Despesa":
                tipo = "-"
            
            if movimentacao["mes"] == datetime.now().month:
                print(f"{movimentacao['descricao']} {tipo} R${movimentacao['valor']}")
    input("\nPressione ENTER para continuar...")

def calcular_saldo():
    saldo = 0
    with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
        dados = json.load(movimentacoes)
        for movimentacao in dados:
            if movimentacao["tipo"] == "Receita":
                saldo += movimentacao["valor"]
            elif movimentacao["tipo"] == "Despesa":
                saldo -= movimentacao["valor"]
    return saldo

def menu_saldo():
    subprocess.run("cls", shell=True)
    saldo = calcular_saldo()

    print(f"""
╔═══════════════════════════════╗
║             SALDO             ║ 
╠═══════════════════════════════╣
            R${saldo}           
╚═══════════════════════════════╝""")
    
    input("\nPressione ENTER para continuar...")
    return saldo

def menu_relatorios():
    subprocess.run("cls", shell=True)
    saldo = calcular_saldo()
    def relatorio_mensal():
        subprocess.run("cls", shell=True)
        total_receitas = 0
        total_despesas = 0
        with open("movimentacoes.json", "r", encoding="utf-8") as movimentacoes:
            dados = json.load(movimentacoes)
            for movimentacao in dados:
                if movimentacao["tipo"] == "Receita" and movimentacao["mes"] == datetime.now().month:
                    total_receitas += movimentacao["valor"]
                elif movimentacao["tipo"] == "Despesa" and movimentacao["mes"] == datetime.now().month:
                    total_despesas += movimentacao["valor"]
            saldo_mensal = total_receitas - total_despesas
            print(f"""
╔═══════════════════════════════╗
║       RELATÓRIO MENSAL        ║
╠═══════════════════════════════╣
║Receitas: R${total_receitas}
║Despesas: R${total_despesas}
╠═══════════════════════════════╣
║Saldo: R${saldo_mensal}
╚═══════════════════════════════╝
 """)
            
        input("\nPressione ENTER para continuar...")

    while True:
        print(f"""
╔═══════════════════════════════╗
║          RELATÓRIOS           ║ 
╠═══════════════════════════════╣
║1 - Relatório Mensal           ║
║2 - Gastos por Categoria       ║
║3 - Maior Despesa              ║
║4 - Voltar                     ║
╚═══════════════════════════════╝""")
        escolha = int(input("\nDigite um numero: "))
        if escolha == 1:
            relatorio_mensal()     
        elif escolha == 4:
            break

    



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
    elif escolha == 5:
        menu_relatorios()
    elif escolha == 6:
        break