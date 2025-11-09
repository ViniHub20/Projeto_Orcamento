from Calculos_Orcamento import *

def menu():
    print ("""
    Seja Bem-Vindo ao Sistema de Orçamento de Aluguel da R.M

    Escolha qual imóvel gostária de alugar
    1- Casa
    2- Apartamento
    3- Estudio

    """)
    
    escolha_imovel = (input("Escolha:" ))
    
    while escolha_imovel != "1" and escolha_imovel != "2" and escolha_imovel != "3":
        escolha_imovel = (input("""======xx======
Opção inválida! Escolha uma das opções disponíveis."

Digite sua opção: """))
    
    if escolha_imovel == "1":
        casa().calcular()
        
        
    elif escolha_imovel == "2":
        apartamento().calcular()
        
        
    elif escolha_imovel == "3":
        estudio().calcular()
               
menu ()