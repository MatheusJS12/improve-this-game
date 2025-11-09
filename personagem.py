class Personagem:
    def __init__(self, nome, vida, defesa, ataque, bondade, estatos):
        self.estatos = estatos
        self.bondade = bondade
        self.nome = nome
        self.defesa = defesa
        self.ataque = ataque
        self.vidabase = vida
        self.ataquebase = ataque
        self.defesabase = defesa
        self.itens = [{'item': 'poção vermelha', 'qnt': 3},
        {'item': 'poção azul', 'qnt': 3},
        {'item': 'poção verde', 'qnt': 3}]

    def update_nome(self, nome_editado):
        
        self.nome = nome_editado
    def downgrade_bondade(self, diminuir):
        self.bondade -= diminuir

    def update_bondade(self, aumentar):
        self.bondade += aumentar
    
    def morrer(self):
        self.estatos = 2

    def ganhar_itens(Self, itens):
        qnt_pocao_vermelha = itens[0]['qnt']
        qnt_pocao_atual = qnt_pocao_vermelha + 2
        itens[0]['qnt'] = qnt_pocao_atual
        qnt_pocao_azul = itens[0]['qnt']
        qnt_pocao_atual = qnt_pocao_azul + 2
        itens[0]['qnt'] = qnt_pocao_atual
        qnt_pocao_verde = itens[0]['qnt']
        qnt_pocao_atual = qnt_pocao_verde + 2
        itens[0]['qnt'] = qnt_pocao_atual

        print ('Parabens, você ganhou 2 poções de cada tipo')



    def __str__(self):
        return f'Personagem: {self.nome}, Bondade: {self.bondade}, itins: {self.itens}'