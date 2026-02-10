opcao = " "

def selecionar (opcao):
    if (opcao == "1"):
      print("Caso opte em alugar um apartamento com 2 quartos, será acrescentado R$ 200,00 na mensalidade")
      quartos = input("Digite quantos quartos deseja: ")
      if quartos == "2":
            aluguel = 700
            aluguel += 200

      print("Para incluir a vaga de garagem o valor acrescentado é de R$ 300,00")
      garagem = input("Deseja garagem? (sim/nao): ")
      if garagem.lower() == "sim":
            aluguel += 300

      print("A empresa R.M oferece um desconto de 5% (cinco por cento) no valor do aluguel de apartamentos para pessoas que não possuem crianças")
      criancas = input("Possui crianças? (sim/nao): ")
      if criancas.lower() == "nao":
            aluguel *= 0.95  # desconto de 5%

    elif (opcao == "2"):
      print("Caso opte em alugar uma casa com 2 quartos, será acrescentado R$ 250,00 na mensalidade")
      quartos = input("Digite quantos quartos deseja: ")
      if quartos == "2":
          aluguel = 900
          aluguel += 250

      print("Para incluir a vaga de garagem o valor acrescentado é de R$ 300,00")
      garagem = input("Deseja garagem? (sim/nao): ")
      if garagem.lower() == "sim":
            aluguel += 300

    elif (opcao == "3"):
      print("Caso opte por adicionar vagas de estacionamento o valor é de R$ 250,00 com 2 (duas) vagas, podendo acrescentar mais vagas no valor de R$ 60,00 cada")
      vagas = int(input("Quantas vagas deseja? (0 ou 2+): "))
      if vagas >= 2:
            aluguel = 1200
            aluguel += 250
            extras = vagas - 2
            aluguel += extras * 60
    
    elif (opcao == "0"):
        print("Saindo do sistema...")
        return

    else:
        print("Opção inválida")
        return
       
    parcelas = int(input("Contrato R$ 2.000,00 em quantas parcelas (1 a 5)? "))
    parcela_contrato = 2000 / parcelas

    print("\n------ RESUMO DO ORÇAMENTO ------")
    print(f"Aluguel mensal: R$ {aluguel:.2f}")
    print(f"Contrato:  R$ 2.000,00 em {parcelas}x de R$ {parcela_contrato:.2f}")
    print(f"Total do primeiro mês: R$ {(aluguel + parcela_contrato):.2f}")
 
def mostrar_menu ():
    print("---Bem-vinda ao Gerador de Orçamento da Imobiliária R.M!---")
    print("Escolha o tipo de locação")
    print("1 - Apartamento: R$ 700,00 | 1 quarto")
    print("2 - Casa: R$ 900,00 | 1 quarto")
    print("3 - Estudio: R$ 1.200,00")
    print("0 - Sair")

while (opcao != "0"):
 mostrar_menu () #mostra menu

 opcao = input("Digite a opção desejada: ")

 selecionar (opcao)