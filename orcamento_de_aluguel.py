import os   # Usado para limpar a tela do terminal
import csv    # Usado para gerar e escrever o arquivo .CSV
opcao = " "    # Variável que controla o loop do menu (enquanto não for "0", continua)
from colorama import init, Fore   # Usado para colorir textos no terminal

def selecionar (opcao):    # FUNÇÃO PRINCIPAL: GERAR ORÇAMENTO
    #Variáveis para montar o resumo do orçamento
    tipo = ""                   # Guardará o tipo: "Apartamento", "Casa" ou "Estúdio"
    quartos = None               # Guardará a quantidade de quartos (apto/casa)
    garagem = None                # Guardará se tem garagem (True/False)
    desconto_aplicado = False      # True se desconto foi aplicado (apto sem crianças)
    valor_desconto = 0.0              # Valor em reais do desconto aplicado
    vagas = None                      # Guardará as vagas (apenas estúdio)

    aluguel_base = 0.0            # Valor base do aluguel do tipo escolhido
    adicionais = []                 # Lista que guarda os adicionais (ex.: garagem, 2º quarto, vagas extras)

    if (opcao == "1"):
      tipo = "Apartamento"
      aluguel_base = 700.0
      aluguel = aluguel_base

      #Pergunta e valida quartos (1 ou 2)
      print(f"{Fore.CYAN}========LOCAÇÃO APARTAMENTO========\n{Fore.RESET}")
      print(f"{Fore.YELLOW}Caso opte em alugar um apartamento com 2 quartos, será acrescentado R$ 200,00 na mensalidade{Fore.RESET}")
      quartos = restricao_quartos ()
      if quartos == 2:
            aluguel += 200
            adicionais.append(("2º quarto", 200.0))

      #Pergunta e valida garagem (sim/nao)
      print(f"{Fore.YELLOW}Para incluir a vaga de garagem o valor acrescentado é de R$ 300,00{Fore.RESET}")
      garagem = restricao_sim_nao("Deseja garagem? (sim/nao): ")
      if garagem:
          aluguel += 300
          adicionais.append(("Garagem", 300.0))

      #Pergunta e aplica desconto de 5% se NÃO tiver crianças
      print(f"{Fore.YELLOW}A empresa R.M oferece um desconto de 5% no valor do aluguel de apartamentos para pessoas que não possuem crianças{Fore.RESET}")
      criancas = restricao_sim_nao("Possui crianças? (sim/nao): ")
      if not criancas:
            antes = aluguel
            aluguel = round(aluguel * 0.95, 2)
            valor_desconto = round(antes - aluguel, 2)
            desconto_aplicado = True

    elif (opcao == "2"):
       tipo = "Casa"
       aluguel_base = 900.0
       aluguel = aluguel_base
       
       # Pergunta e valida quartos (1 ou 2)
       print(F"{Fore.CYAN}========LOCAÇÃO CASA========\n{Fore.RESET}")
       print(f"{Fore.YELLOW}Caso opte em alugar uma casa com 2 quartos, será acrescentado R$ 250,00 na mensalidade{Fore.RESET}")
       quartos = restricao_quartos()
       if quartos == 2:
            aluguel += 250
            adicionais.append(("2º quarto", 250.0))

       # Pergunta e valida garagem
       print(f"{Fore.YELLOW}Para incluir a vaga de garagem o valor acrescentado é de R$ 300,00{Fore.RESET}")
       garagem = restricao_sim_nao("Deseja garagem? (sim/nao): ")
       if garagem:
          aluguel += 300
          adicionais.append(("Garagem", 300.0))

    elif (opcao == "3"):
      tipo = "Estúdio"
      aluguel_base = 1200.0
      aluguel = aluguel_base
      
      # Pergunta e valida vagas (0 ou 2+; não aceita 1)
      print(f"{Fore.CYAN}========LOCAÇÃO ESTÚDIO========\n{Fore.RESET}")
      print(f"{Fore.YELLOW}Caso opte por adicionar vagas de estacionamento o valor é de R$ 250,00 com 2 (duas) vagas, podendo acrescentar mais vagas no valor de R$ 60,00 cada{Fore.RESET}")
      vagas = restricao_vagas_estudio()
      if vagas >= 2:          # Se vagas >= 2 aplica pacote e extras
            aluguel += 250
            adicionais.append(("Pacote 2 vagas", 250.0))
            extras = vagas - 2
            if extras > 0:
                aluguel += extras * 60
                adicionais.append((f"Vagas extras ({extras}x)", extras * 60.0))
    
    elif (opcao == "0"):
        print("Saindo do sistema...")
        return

    else:
        print("Opção inválida")
        return
       
    # CONTRATO E PARCELAMENTO 
    parcelas = restricao_parcelas()   # Valida número entre 1 e 5
    parcela_contrato = round(2000 / parcelas, 2)    # Calcula valor de cada parcela do contrato

    print(f"{Fore.LIGHTGREEN_EX}------ RESUMO DO ORÇAMENTO ------{Fore.RESET}")
    print(f"Tipo: {tipo}")

     # Se for apartamento ou casa, mostra quartos e garagem
    if tipo in ("Apartamento", "Casa"):
        print(f"Quartos: {quartos}")
        print(f"Garagem: {'Sim' if garagem else 'Não'}")
        if tipo == "Apartamento":           # Só apartamento tem desconto
            print(f"Desconto aplicado: {'Sim' if desconto_aplicado else 'Não'}")
    else:
        print(f"Vagas no estúdio: {vagas}")

    print(f"{Fore.LIGHTGREEN_EX}---------------------------------{Fore.RESET}")
    print(f"Aluguel base: R$ {aluguel_base:.2f}")

 # Mostra os adicionais (se houver)
    if adicionais:
        print("Adicionais:")
        for nome, valor in adicionais:
            print(f"  - {nome}: R$ {valor:.2f}")
    else:
        print("Adicionais: nenhum")

 # Mostra desconto aplicado (se houver)
    if desconto_aplicado:
        print(f"Desconto: - R$ {valor_desconto:.2f}")
    else:
        if tipo == "Apartamento":
            print("Desconto: não aplicado")
        else:
            print("Desconto: não se aplica")

    # Mostra valores finais
    print(f"{Fore.LIGHTGREEN_EX}---------------------------------{Fore.RESET}")
    print(f"Aluguel mensal final: R$ {aluguel:.2f}")
    print(f"Contrato: R$ 2.000,00 em {parcelas}x de R$ {parcela_contrato:.2f}")
    print(f"Total do primeiro mês: R$ {(aluguel + parcela_contrato):.2f}")
    print(f"{Fore.LIGHTGREEN_EX}---------------------------------{Fore.RESET}")
  
   # PERGUNTA SE DESEJA GERAR CSV
    gerar = restricao_sim_nao("Deseja gerar o arquivo CSV com as 12 parcelas? (sim/nao): ")
    if gerar:
     nome_arquivo = "orcamento_12_parcelas.csv"
     gerar_csv_12_meses(nome_arquivo, aluguel, parcelas, parcela_contrato)
     print(f" CSV gerado com sucesso: {nome_arquivo}")


 # FUNÇÃO: MOSTRAR MENU
def mostrar_menu ():
    print(f"{Fore.MAGENTA}---GERADOR DE ORÇAMENTO IMOBILIÁRIA R.M---{Fore.RESET}")
    print("LOCAÇÕES DISPONIVEIS:")
    print("1 - Apartamento: R$ 700,00 | 1 quarto")
    print("2 - Casa: R$ 900,00 | 1 quarto")
    print("3 - Estudio: R$ 1.200,00")
    print("0 - Sair")

# FUNÇÕES DE RESTRIÇÃO (VALIDAÇÃO)
def restricao_opcao_menu ():          #Lê e valida a opção do menu. Só aceita 0, 1, 2 ou 3.
    while True:
        resposta = input(F"{Fore.BLUE}Digite a opção desejada (0-3): {Fore.RESET}").strip()
        if resposta in ("0", "1", "2", "3"):
            return resposta
        print("Opção inválida. Digite 0, 1, 2 ou 3.")

def restricao_quartos ():            #Lê e valida quantidade de quartos. Só aceita 1 ou 2.
    while True:
        resposta = input("Digite quantos quartos deseja (1 ou 2): ").strip()
        if resposta in ("1", "2"):
            return int(resposta)
        print("Inválido. Digite apenas 1 ou 2.")

def restricao_sim_nao (msg):         #Lê e valida respostas do tipo sim/nao. Retorna True para sim, False para não.
     while True:
        resposta = input(msg).strip().lower()

        if resposta in ("sim", "s"):
            return True

        elif resposta in ("nao", "não", "n"):
            return False

        else:
            print("Digite apenas sim ou nao (ou s/n).")

def restricao_parcelas ():          #Lê e valida as parcelas do contrato. Só aceita números de 1 a 5. Usa try/except para evitar erro quando o usuário digita letras.
    while True:
        try:
            print(f"{Fore.YELLOW}O valor do contrado a ser confirmado é de R$ 2.000,00! {Fore.RESET}")
            parcelas = int(input("Quantas vezes deseja parcelar o contrato (1 a 5)? "))
            if 1 <= parcelas <= 5:
                return parcelas
            else:
                print("Digite um número entre 1 e 5.")
        
        except ValueError:
            print("Digite apenas números.")

def restricao_vagas_estudio():      # Lê e valida vagas do estúdio. Aceita 0 ou 2 ou mais. Não aceita 1 vaga
    while True:
        try:
            vagas = int(input("Quantas vagas deseja? (0 ou 2+): "))
            
            if vagas == 1:
                print("Não existe opção de 1 vaga.")
                continue

            if vagas >= 0:
                return vagas
            else:
                print("Número inválido.")
        
        except ValueError:
            print("Digite apenas números.")

# FUNÇÃO: GERAR CSV + EXIBIR NO TERMINAL
def gerar_csv_12_meses(nome_arquivo, aluguel_mensal, parcelas_contrato, parcela_contrato):

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["mes", "aluguel_mensal", "parcela_contrato", "total_mes"])

        print(f"{Fore.LIGHTGREEN_EX}\n PARCELAMENTO (12 MESES){Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}---------------------------------------------{Fore.RESET}")
        print("Mes | Aluguel | Parcela Contrato | Total")

        for mes in range(1, 13):
            contrato_mes = parcela_contrato if mes <= parcelas_contrato else 0.00
            total_mes = round(aluguel_mensal + contrato_mes, 2)

            writer.writerow([mes, f"{aluguel_mensal:.2f}", f"{contrato_mes:.2f}", f"{total_mes:.2f}"])
            print(f"{mes:02}  |  R$ {aluguel_mensal:.2f}  |  R$ {contrato_mes:.2f}  |  R$ {total_mes:.2f}")
        print(f"{Fore.LIGHTGREEN_EX}---------------------------------------------{Fore.RESET}")


def pausar_sistema ():        #Pausa o sistema até o usuário apertar ENTER
 input (f"Digite ENTER para voltar ao MENU...")

def limpar_tela ():      
 os.system('cls'if os.name == "nt" else 'clear')

# LOOP PRINCIPAL DO PROGRAMA
while (opcao != "0"):
 mostrar_menu () 

 opcao = restricao_opcao_menu ()

 limpar_tela ()

 if opcao == "0":
        print("Saindo do sistema...")
        break

 selecionar (opcao)

 pausar_sistema ()

 limpar_tela ()