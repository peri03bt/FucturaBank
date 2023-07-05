from basededados import BaseDeDados

def menu_principal():
    base_dados = BaseDeDados()  # Cria a instância do BaseDeDados
    
    while True:
        print("""
        0-Criar Conta
        1-Verificar Saldo
        2-Depositar Dinheiro
        3-Sacar Dinheiro
        4-Sair
        """)
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            # Solicita as informações necessárias para criar uma conta
            cpf = input("Digite seu CPF: ")
            nome = input("Digite seu Nome: ")
            email = input("Digite seu Email: ")
            base_dados.inserir(cpf, nome, email)  
            # Classe BaseDeDados. metódo inserir [Função de baseDeDados] (Parametros)
            # Classe.Metódo(Parametros)
        
        elif opcao == 1:
            # O código para verificar o saldo vai aqui
            cpf = input("Digite seu CPF: ")
            saldo = base_dados.verificar_saldo(cpf)
            if saldo is not None:
                print(f"Seu saldo é: {saldo}")
            
        elif opcao == 2:
            # O código para depositar dinheiro vai aqui
            cpf = input("Digite seu CPF: ")
            valor = float(input("Digite o valor a depositar: "))
            base_dados.depositar_dinheiro(cpf, valor)
            
        elif opcao == 3:
            # O código para sacar dinheiro vai aqui
            cpf = input("Digite seu CPF: ")
            valor = float(input("Digite o valor a sacar: "))
            base_dados.sacar_dinheiro(cpf, valor)
            
        elif opcao == 4:
            base_dados.salvar_dados()  # Salva os dados antes de sair
            break

        else:
            print("Opção inválida, tente novamente.")