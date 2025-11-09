import random
from personagem import Personagem
from util import Util
from colorama import Fore, Back, Style, init
class Batalha():
    def __init__(self, personagem1, personagem2):
        self.p1 = personagem1
        self.p2 = personagem2

    def defesa(self, defensor, dano_recebido):

        dados_defesa = random.randint(1, 10)

        if dados_defesa == 10:
            print(f'{defensor.nome} realizou uma defesa perfeita! Nenhum dano recebido.')
            return 0 

        elif 1 < dados_defesa < 10:
            if defensor.defesa >= 1:
                final_na_defesa = defensor.defesa * 2
                possibilidade_de_defesa = defensor.defesa / final_na_defesa
                chance = random.random()
            else:
                return dano_recebido

            if chance < possibilidade_de_defesa:
                print(f'{defensor.nome} se defendeu parcialmente! Dano reduzido pela metade.')
                return dano_recebido / 2
            else:
                print(f'{defensor.nome} falhou na defesa! Recebe o dano total.')
                return dano_recebido
        else:
            print(f'{defensor.nome} não conseguiu se defender. Recebe o dano total.')
            return dano_recebido
    def atacar(self, atacante, defensor):
        dados_ataque = random.randint(1, 10)
        print(f'\n{atacante.nome} tenta atacar {defensor.nome} (rolagem: {dados_ataque})')

        if dados_ataque == 1:
            print('Ataque mal-sucedido! Nenhum dano causado.')
            dano = 0
        elif dados_ataque == 10:
            dano = atacante.ataque * 1.5
            print('Acerto crítico! Dano aumentado.')
        else:
            dano = atacante.ataque

        dano_final = self.defesa(defensor, dano)
        defensor.vida -= dano_final

        print(f'{defensor.nome} recebeu {dano_final:.2f} de dano. Vida restante: {defensor.vida:.2f}')

        if defensor.vida <= 0:
            print(f' {defensor.nome} foi derrotado!\n')
    def atacar_sem_defesa(self, atacante, defensor):
        dados_ataque_sem = random.randint(1, 10)
        if dados_ataque_sem == 1:
            print('Ataque mal-sucedido! Nenhum dano causado.')
            dano = 0
        elif dados_ataque_sem == 10:
            print('Acerto crítico! Dano aumentado.')
            dano = atacante.ataque * 1.5
        else:
            dano = atacante.ataque
        dano_fim = dano
        defensor.vida -= dano_fim
        print(f'{defensor.nome} recebeu {dano_fim:.2f} de dano. Vida restante: {defensor.vida:.2f}')
        if defensor.vida <= 0:
            print(f' {defensor.nome} foi derrotado!\n')
    def ambos_defende():
        print('Ambos se defenderam, por isso niguem recebel dano')
    def usar_pocao(self,usuario ,itens):
        print('Poções disponíveis:')
        print('1 -' + Fore.YELLOW + 'Poção vermelha' + Fore.WHITE ,': Para ganhar força')
        print('2 -' + Fore.YELLOW + 'Poção azul' + Fore.WHITE ,': Para ganhar defesa')
        print('3 -' + Fore.YELLOW + 'Poção verde' + Fore.WHITE ,': Para ganhar força vida')
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
                usuario.ataque += usuario.ataque * 1.1
                

        elif opcao == 2:
            qnt_pocao_azul = itens[1]['qnt']
            if qnt_pocao_azul == 0:
                print(Fore.RED + 'Suas poções azuis acabaram!' + Fore.WHITE)
            else:
                qnt_pocao_atual = qnt_pocao_azul - 1
                itens[1]['qnt'] = qnt_pocao_atual
                usuario.defesa += usuario.defesa * 1.1
                

        elif opcao == 3:
            qnt_pocao_verde = itens[2]['qnt']
            if qnt_pocao_verde == 0:
                print(Fore.RED + 'Suas poções verdes acabaram!' + Fore.WHITE)
            else:
                qnt_pocao_atual = qnt_pocao_verde - 1
                itens[2]['qnt'] = qnt_pocao_atual
                if usuario.vida >= usuario.vidabase:
                    usuario.vida = usuario.vidabase
                else:
                    usuario.vida += usuario.vida * 1.1