import json
import os

class BaseDeDados:
    def __init__(self):
        # Verifica se o arquivo de dados existe ## Função construtora() ## Se não, Cadastrar
        if os.path.exists('dados.json'):
            # Se existe, carrega os dados para o dicionário
            with open('dados.json', 'r') as f:
                self.cadastro = json.load(f)

        else:
            self.cadastro = {}

    # Os outros métodos da classe BaseDeDados (iserir, etc. vão aqui)

    def inserir(self, cpf, nome, email):
        # Se CPF dentro cadastro - validador do CPF
        if cpf in self.cadastro:
            print('CPF já cadastrado.')
        else:
            self.cadastro[cpf] = {'nome': nome, 'email': email, 'saldo': 0.0}
            #Se não cadastrado - Inserir no dicionario - saldo padrão 0.0 (pré definido)

    def listar(self):
        # Função criada apenas para cado precise 
        # em algum momento chamar o print do dicionario de clientes
        for cpf, dados in self.cadastro.items():
            print(f"CPF: {cpf}, Nome: {dados['nome']}, Email: {dados['email']}, Saldo: {dados['saldo']}")

    def apagar(self, cpf):
        # Função criada apenas para manutenção de código
        # Caso precise deletar algum cliente
        if cpf in self.cadastro:
            del self.cadastro[cpf]
        else:
            print('CPF não encontrado.')

    def atualizar_email(self, cpf, novo_email):
        # Função criada apenas para manutenção de código
        # Caso precise atualizar email do cliente
        if cpf in self.cadastro:
            self.cadastro[cpf]['email'] = novo_email
            # atualizando  Chave / Valor do dicionario - cadastro
        else:
            print('CPF não encontrado.')

#       FUNÇÕES  DE VALIDAÇÃO DE SALDO
#       ------------------------------

    def verificar_saldo(self, cpf): # Opção 1
        if cpf in self.cadastro:
            return self.cadastro[cpf]['saldo']
            # Se CPF cadastrado - retornar chave [cpf] / valor ['saldo']
        else:
            print('CPF não encontrado.')
            return None # Olhar em Menu para entender!

    def depositar_dinheiro(self, cpf, valor): # valor - Opções 2 e 3
        if cpf in self.cadastro:
            self.cadastro[cpf]['saldo'] += valor
            # Em dicionário cadastro = { key [cpf] : value ['saldo'] }
            # adicionar valor em 'saldo' no dicionario

        else:
            print('CPF não encontrado.')
            
    def sacar_dinheiro(self, cpf, valor): # valor - Opções 2 e 3
        if cpf in self.cadastro:
            # se 'saldo' maior ou igual a 'valor': subtrair 'valor' de 'saldo'
            if self.cadastro[cpf]['saldo'] >= valor:
                self.cadastro[cpf]['saldo'] -= valor
            #Se não o valor vai ser menor que saldo logo: print - saldo insuf.
            else:
                print('Saldo insuficiente.')
        else:
            print('CPF não encontrado.')

    def salvar_dados(self): #salvando dados em cadastro - dados.json
        # Salva o dicionário no arquivo de dados
        with open('dados.json', 'w') as f:
            json.dump(self.cadastro, f)