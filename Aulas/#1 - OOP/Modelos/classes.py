class Personagem:
    def __init__(self, nome):
        self._nome = nome.strip().capitalize()
        self._vida = 100
        self._experiencia = 0
        self._nivel = 1

    def __str__(self):
        return (f'---- Personagem ----\n'
                f'NOME: {self._nome}\n'
                f'PONTOS VITAIS: {self._vida}\n'
                f'XP: {self._experiencia}\n'
                f'NÍVEL: {self._nivel}\n')


    @property
    def nome(self):
        return f'PERSONAGEM: {self._nome}'

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.strip().capitalize()

    @property
    def vida(self):
        return f'PONTOS VITAIS: {self._vida}'

    @property
    def experiencia(self):
        return f'XP: {self._experiencia}'

    @property
    def nivel(self):
        return f'NÍVEL: {self._nivel}'


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._poder = None
        self.varinha = 'Pau'

    def __str__(self):
        return (f'---- Mago ----\n'
                f'NOME: {self._nome}\n'
                f'PONTOS VITAIS: {self._vida}\n'
                f'XP: {self._experiencia}\n'
                f'NÍVEL: {self._nivel}\n'
                f'PODER: {self.poder}\n'
                f'VARINHA: {self.varinha}')

    @property
    def poder(self):
        return f'Nenhum poder disponível' if self._poder == None else f'PODER: {self._poder}'

    @poder.setter
    def poder(self, novo_poder):
        self._poder = novo_poder
