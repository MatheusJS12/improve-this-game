from personagem import Personagem
from colorama import Fore, Back, Style, init
from util import Util

init(autoreset=True)

itens = [{'item': 'poção vermelha', 'qnt': '3'},
        {'item': 'poção azul', 'qnt': '3'},
        {'item': 'poção verde', 'qnt': '3'}]
heroi_status = {'nome': '', 'força': '', 'defesa': '', 'vida_max': '', 'vida_temp': ''}

class Heroi(Personagem):
    def _init_(self):
        super()._init_(nome = '', idade = 0, vida = 100, defesa = 0, ataque = 0)
        niveis_bondade = ['Baixa', 'Média', 'Alta']
        self.itens = itens
        pass
    def personalizacao(self):
        Util.limpar_tela()
        self.nome = str(input(Style.BRIGHT + 'Insira o nome do seu herói: ' + Style.NORMAL).strip().capitalize())
        Util.limpar_tela()
        print('Cuidado! Agora você definirá os seguinte status:')
        Util.separacao_cabecalho()
        print(Fore.GREEN + '{:^50}'.format('Força') + Fore.BLUE + '\n{:^50}'.format('Defesa') + Fore.RED + '\n{:^50}'.format('Vida'))
        Util.separacao_cabecalho()
        print('Total de pontos de status: ' + Fore.YELLOW + '120' + Fore.RESET)
        Util.pausa(3)

        try:
            self.ataque = int(input('\nPontos em força: '))
            self.defesa = int(input('Pontos em defesa: '))
            self.vida = int(input('Pontos em vida: '))
        except ValueError:
            print('Adicione um número positivo inteiro!')
            
        soma_status = self.ataque + self.defesa + self.vida
        if soma_status > 120:
            print('Seus pontos de status totais superam o limite permitido!')
            return
        if self.ataque < 1:
            print('Seu status força deve conter, no mínimo, 1 ponto!')
            return
        if self.defesa < 1:
            print('Seu status defesa deve conter, no mínimo, 1 ponto!')
            return
        if self.vida < 1:
            print('Seu status vida deve conter, no mínimo, 1 ponto!')
            return
        heroi_status['nome'] = self.nome
        heroi_status['força'] = self.ataque
        heroi_status['defesa'] = self.defesa
        heroi_status['vida'] = self.vida
        heroi_status['vida_temp'] = self.vida


    def exibir_info(self):
        print(self.nome)
    def usar_pocao():
        print('Poções disponíveis:')
        print('1 -' + Fore.YELLOW + 'Poção vermelha' + Fore.WHITE)
        print('2 -' + Fore.YELLOW + 'Poção azul' + Fore.WHITE)
        print('3 -' + Fore.YELLOW + 'Poção verde' + Fore.WHITE)
        try:
            opcao = int(input('Selecione a poção que deseja usar: '))
        except ValueError:
            print('Você não selecionou uma das opções de poções válidas')
        if opcao == 1:
            qnt_pocao_vermelha = itens[0]['qnt']
            if qnt_pocao_vermelha == 0:
                print(Fore.RED + 'Suas poções vermelhas acabaram!' + Fore.WHITE)
            else:
                qnt_pocao_atual = qnt_pocao_vermelha - 1
                itens[0]['qnt'] = qnt_pocao_atual
        elif opcao == 2:
            qnt_pocao_azul = itens[1]['qnt']
            if qnt_pocao_azul == 0:
                print(Fore.RED + 'Suas poções azuis acabaram!' + Fore.WHITE)
            else:
                qnt_pocao_atual = qnt_pocao_azul - 1
                itens[1]['qnt'] = qnt_pocao_atual
        elif opcao == 3:
            qnt_pocao_verde = itens[2]['qnt']
            if qnt_pocao_verde == 0:
                print(Fore.RED + 'Suas poções verdes acabaram!' + Fore.WHITE)
            else:
                qnt_pocao_atual = qnt_pocao_verde - 1
                itens[2]['qnt'] = qnt_pocao_atual
        pass

Heroi.usar_pocao()