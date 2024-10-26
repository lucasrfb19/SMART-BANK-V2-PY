from datetime import datetime
data_hora_atual = datetime.now()
mascara_br = "%d/%m/%Y %H:%M"
#Definindo classes e funções
class saldo():
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial
        saldo_inicial = 0

class deposito ():
    def __init__(self, deposito):
        self.deposito = deposito

class saque():
    def __init__(self, saque):
        self.saque = saque
    
class saldo_atual (saldo, deposito, saque):
    def __init__(self, saldo_inicial, deposito, saque):
        self.saldo_atual = saldo_atual
        saldo_atual = saldo_inicial + deposito - saque
        print("Esse é o seu saldo atual: R$ " + saldo_atual)

class Cliente():
    def __init__(self, cpf, Nome, DataNascimento, Endereco, Idade = None):
        self.cpf = cpf
        self.Nome = Nome
        self.DataNascimento = DataNascimento
        self.Endereco = Endereco 
        self.Idade = Idade
        


class Conta():
    def __init__(self, Agencia, cpf, Conta_Corrente):
         self.cpf = cpf
         self.Agencia = Agencia
         self.Conta_Corrente = Conta_Corrente
        
         



#Definir sistemas de "interface"
bem_vindo = f"""
    -------Bem-Vindo ao Smart Bank-------
"""
print(data_hora_atual.strftime(mascara_br))
acesso = str(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           - Abrir Conta 
           - Já sou correntista               
           - Sair
  """))

if acesso == "Abrir Conta":
    usuario_um = Cliente(cpf = "123.456.567-19", Nome = "Lucas Barros", DataNascimento = "12/08/2005", Endereco = "Rua R, Bairro B, Cidade C-SP")
    print(f"CPF: {usuario_um.cpf} | Nome: {usuario_um.Nome} | Data de Nascimento: {usuario_um.DataNascimento} | Endereço: {usuario_um.Endereco}")
    print("Usuário criado com sucesso!")
    print("Estamos criando sua conta... Aguarde um instante...")
    conta_um = Conta(cpf = "123.456.567-19", Agencia = "0001", Conta_Corrente= 14569)
    print(f"Agência: {conta_um.Agencia} | Conta-Corrente: {conta_um.Conta_Corrente}")
    print("Conta criada com sucesso!")
#Primeiras operações após abrir conta
if acesso == "Abrir Conta":
    operar = str(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           - Primeiro depósito             
           - Sair
  """))
    if operar == "Primeiro depósito": #Primeira estrutura de decisão: elemento um (1/2)
        deposito = (float(input("Informe o valor: R$")))
        print("Depósito realizado com sucesso!")
        #Após cada decisão, uma nova estrutura surgirá.
        if deposito >= 1.0: #Dentro da primeira estrutura, surge a segunda: elemento um (1/4)
           nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Sair
            """))
        if nova_operar == "Novo depósito": #Dentro da primeira estrutura, surge a segunda: elemento dois (2/4)
                deposito = (float(input("Informe o valor: R$")))
                print("Depósito realizado com sucesso!")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
        if nova_operar == "Realizar saque": #Dentro da primeira estrutura, surge a segunda: elemento três (3/4)
                saque = (float(input("Informe o valor: R$")))
                print("Saque realizado com sucesso!")
        if saque >= 1: #Dentro da segunda estrutura, surge a terceira: elemento um (1/4)
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
        if nova_operar == "Conferir extrato": #Dentro da primeira estrutura, surge a segunda: elemento quatro (4/4)
            saldo = deposito - saque
            print(f"Você tem: R${saldo} disponíveis")
            nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Novo depósito": #Dentro da primeira estrutura, surge a segunda: elemento dois (2/4)
                deposito = (float(input("Informe o valor: R$")))
                print("Depósito realizado com sucesso!")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Realizar saque": #Dentro da primeira estrutura, surge a segunda: elemento três (3/4)
                saque = (float(input("Informe o valor: R$")))
                print("Saque realizado com sucesso!")
            if saque >= 1: #Dentro da segunda estrutura, surge a terceira: elemento um (1/4)
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Conferir extrato": #Dentro da primeira estrutura, surge a segunda: elemento quatro (4/4)
                saldo = deposito - saque
                print(f"Você tem: R${saldo} disponíveis")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
    while nova_operar == "Sair":
            print("Sistema finalizado! Volte sempre!")
            break
    while operar == "Sair": #Primeira estrutura de decisão: elemento dois (2/2)
        print("Sistema finalizado! Volte sempre!")
        break

    
if acesso == "Já sou correntista":
    validar_acesso = input(str("Informe seu CPF:"))
    validar_acesso_cc = input(int("Informe a conta corrente:"))
    if validar_acesso == "123.456.567-19" and validar_acesso_cc == 14569: 
        operar = str(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           - Primeiro depósito             
           - Sair
  """))
    if operar == "Primeiro depósito": #Primeira estrutura de decisão: elemento um (1/2)
        deposito = (float(input("Informe o valor: R$")))
        print("Depósito realizado com sucesso!")
        #Após cada decisão, uma nova estrutura surgirá.
        if deposito >= 1.0: #Dentro da primeira estrutura, surge a segunda: elemento um (1/4)
           nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Sair
            """))
        if nova_operar == "Novo depósito": #Dentro da primeira estrutura, surge a segunda: elemento dois (2/4)
                deposito = (float(input("Informe o valor: R$")))
                print("Depósito realizado com sucesso!")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
        if nova_operar == "Realizar saque": #Dentro da primeira estrutura, surge a segunda: elemento três (3/4)
                saque = (float(input("Informe o valor: R$")))
                print("Saque realizado com sucesso!")
        if saque >= 1: #Dentro da segunda estrutura, surge a terceira: elemento um (1/4)
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
        if nova_operar == "Conferir extrato": #Dentro da primeira estrutura, surge a segunda: elemento quatro (4/4)
            saldo = deposito - saque
            print(f"Você tem: R${saldo} disponíveis")
            nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Novo depósito": #Dentro da primeira estrutura, surge a segunda: elemento dois (2/4)
                deposito = (float(input("Informe o valor: R$")))
                print("Depósito realizado com sucesso!")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Realizar saque": #Dentro da primeira estrutura, surge a segunda: elemento três (3/4)
                saque = (float(input("Informe o valor: R$")))
                print("Saque realizado com sucesso!")
            if saque >= 1: #Dentro da segunda estrutura, surge a terceira: elemento um (1/4)
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
            if nova_operar == "Conferir extrato": #Dentro da primeira estrutura, surge a segunda: elemento quatro (4/4)
                saldo = deposito - saque
                print(f"Você tem: R${saldo} disponíveis")
                nova_operar = str(input("""
            -------INFORME A OPÇÃO DESEJADA:
                  
            - Novo depósito 
            - Realizar saque               
            - Conferir extrato
            - Sair
            """))
    while nova_operar == "Sair":
            print("Sistema finalizado! Volte sempre!")
            break
    while operar == "Sair": #Primeira estrutura de decisão: elemento dois (2/2)
        print("Sistema finalizado! Volte sempre!")
        break

while acesso == "Sair":
    print("Sistema finalizado! Volte sempre!")
    break


