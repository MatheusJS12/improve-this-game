class npc():
    def _inti_(self, nome, defesa, ataque, nível_de_bondade):
        self.nome = nome
        self.defesa = defesa
        self.ataque = ataque
        self.nível_de_bondade = nível_de_bondade
    def upbondade(self):
        if self.nível_de_bondade > 10:
            print('bondade tão alta que não pode mudar')
            pass
        elif self.nível_de_bondade < 10 and self.nível_de_bondade > -10:
            self.nível_de_bondade += 1
            return self.nível_de_bondade
        else:
            print('O personagem é um vilão')
    def downbondade(self):
        if self.nível_de_bondade > 10:
            print('bondade tão alta que não pode mudar')
            pass
        elif self.nível_de_bondade < 10 and self.nível_de_bondade > -10:
            self.nível_de_bondade -= 1
            return self.nível_de_bondade
        else:
            print('O personagem é um vilão')