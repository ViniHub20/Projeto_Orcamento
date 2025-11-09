class imovel():
    def __init__(self):
        self.valor = 0
        self.valor_contrato = 2000
        self.qtd_parcelas = 0
        
        
    def finalizar_orcamento(self):
        opcao_contrato = input("""
O valor do contrato é 2000
Poderá ser parcelado em até 5 vezes

1- À Vista
2- Parcelar

Digite sua forma de pagamento para o contrato: """)
        
        while opcao_contrato != "1" and opcao_contrato != "2" and opcao_contrato != "3":
            opcao_contrato = input("""
Opção inválida!

Escolha uma das opções existêntes: """).strip()
            
        if opcao_contrato == "1":
            print (f"""
Orçamento de Aluguel

Valor de aluguel orçado: R${round(self.valor,2)}
Valor do contrato: R${round(self.valor_contrato,2)}
Quantidade de parcelas: {self.qtd_parcelas}""")
            
        elif opcao_contrato == "2":
            while True:
                try:
                    self.qtd_parcelas = int(input("Digite o número de parcelas que deseja realizar ( máximo de 5 parcelas): "))
                    
                    while self.qtd_parcelas > 5 or self.qtd_parcelas < 1:
                        self.qtd_parcelas = int(input("""
Quantidade de parcelas inválida!

Digite um número de parcelas ( 1 até 5): """))
                    
                    break 
                  
                except ValueError:
                    print ("Resposta Inválida!")
            
            print (f"""
Orçamento de Aluguel

Valor de aluguel orçado: R${round(self.valor,2)}
Valor do contrato: R${round(self.valor_contrato / self.qtd_parcelas,2)}
Quantidade de parcelas: {self.qtd_parcelas}""")

        self.arquivo_csv()
        
    def arquivo_csv(self):
        import csv
        
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        if self.qtd_parcelas > 0:
            valor_parcela_contrato = self.valor_contrato / self.qtd_parcelas
        else:
            valor_parcela_contrato = 0

        with open("orcamento_parcelas.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=":")
            escritor.writerow(["Mês", " Valor da Parcela"])

            for i, mes in enumerate(meses):
               
                if i < self.qtd_parcelas:
                    valor_total = self.valor + valor_parcela_contrato
                else:
                    valor_total = self.valor

                escritor.writerow([mes, f" {valor_total:.2f}"])

        print("\nSua tabela com o Orçamento de Parcelas foi gerado com sucesso!")
    
class casa(imovel):
    def __init__(self):
        super().__init__()
        self.valor = 900
    
    def calcular(self):
        qtd_quartos = (input("""A mensalidade para casas de 1 quarto é de R$900,00.
Caso preferir uma casa de 2 quartos, serão adicionados R$250,00 em sua mensalidade.

Digite a quantidade de quartos que deseja para sua casa: """))
        
        while qtd_quartos != "1" and qtd_quartos != "2":
            qtd_quartos = input("""======xx======
Quantidade inválida!

Digite uma quantidade disponivel: """)
        
        if qtd_quartos == "2":
            self.valor += 250 

        garagem = input("""Será possivel também adicionar uma garagem em sua casa.
Serão adicionados R$300,00 em sua mensalidade.

Deseja adicionar uma garagem? [S/N]: """).lower().strip()
        
        while garagem != "s" and garagem != "n":
            garagem = input("""======xx======
Opção Inválida! Digite S para aceitar ou N para negar.
                            
Digite sua escolha: """).lower().strip()
        
        if garagem == "s":
            self.valor += 300
        
        self.finalizar_orcamento()
      
class apartamento(imovel):
    def __init__(self):
        super().__init__()
        self.valor = 700
        
    def calcular(self):
        qtd_quarto = (input("""A mensalidade para apartamentos de 1 quarto é de R$700,00.
Caso preferir um apartamento de 2 quartos, serão adicionados R$200,00 em sua mensalidade.

Digite a quantidade de quartos que deseja para seu apartamento: """))
        
        while qtd_quarto != "1" and qtd_quarto != "2":
            qtd_quarto = input("""======xx======
Quantidade inválida!

Digite uma quantidade disponivel: """)
            
        if qtd_quarto == "2":
            self.valor += 200
        
        garagem = input ("""Será possivel também adicionar uma garagem em seu apartamento.
Serão adicionados R$300,00 em sua mensalidade.

Deseja adicionar uma garagem? [S/N]: """).lower().strip()
        
        while garagem != "s" and garagem != "n":
            garagem = input("""======xx======
Opção Inválida! Digite S para aceitar ou N para negar.
                            
Digite sua escolha: """).lower().strip()
            
        if garagem == "s":
            self.valor += 300
        
        crianca = input ("""
Você possui alguma criança? [S/N]: """).lower().strip()
        
        while crianca != "s" and crianca != "n":
            crianca = input("""======xx======
Opção Inválida! Digite S para confirmar ou N para negar.
                            
Digite sua escolha: """).lower().strip()
        
        if crianca == "n":
            self.valor = self.valor - (self.valor * 0.05)
        
        self.finalizar_orcamento()
    
class estudio(imovel):
    def __init__(self):
        super().__init__()
        self.valor = 1200
        
    def calcular(self):
        vagas = input("""A mensalidade para o aluguel de um estudio é de R$1200,00.
Caso desejar temos 2 pacotes para vagas de estacionamento.
O pacote inicial inclui 2 vagas por R$250,00.
O pacote plus inclui as 2 vagas por R$250,00 junto de vagas adicionais, onde você decidirá a quantidade que deseja, sendo cobrado R$60,00 por vaga.

1- Comprar apenas o Estudio.
2- Pacote Inicial ( Estudio + 2 vagas de estacionamento )
3- Pacote Plus ( Estudio + 2 vagas de estacionamento + vagas adicionais )

Escolha uma das opções: """)
        
        while vagas != "1" and vagas != "2" and vagas != "3":
            vagas = input("""Opção Inválida!
                          
Escolha uma das opções existentes: """)
            
        if vagas == "2":
            self.valor += 250
        
        elif vagas == "3":
            self.valor += 250
            while True:
                try:
                    vagas_adc = int(input("Digite o número de vagas adicionais deseja acrescentar: "))
                    self.valor += (60 * vagas_adc)
                    break
                
                except ValueError:
                    print ("Digite um número de vagas")
                    
        
        self.finalizar_orcamento()
