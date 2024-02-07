from datetime import datetime

class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo.strip().capitalize()
        self._autor = autor.strip().capitalize()
        self._ano = ano

    @property
    def titulo(self):
        return f'Título: {self._titulo}'

    @titulo.setter
    def titulo(self, titulo):
        if titulo.strip() != "":
            self._titulo = titulo.strip().capitalize()
        else:
            print("Título inválido. Não foi feita nenhuma modificação.")

    @property
    def autor(self):
        return f'Autor: {self._autor}'

    @autor.setter
    def autor(self, autor):
        if autor.strip() != "":
            self._autor = autor.strip().capitalize()
        else:
            print("Autor inválido. Não foi feita nenhuma modificação.")

    @property
    def ano(self):
        ano_atual = datetime.today().year
        if 1900 <= self._ano <= ano_atual:
            return f'Ano de Publicação: {self._ano}'
        else:
            return 'Ano de publicação inválido.'

    @ano.setter
    def ano(self, ano):
        ano_atual = datetime.today().year
        if 1900 <= ano <= ano_atual:
            self._ano = ano
        else:
            print("Ano de publicação inválido. Não foi feita nenhuma modificação.")

# Teste do código
titulo = input('Digite o título do livro: ')
autor = input('Digite o autor do livro: ')
ano = int(input('Digite o ano de publicação: '))

livro = Livro(titulo, autor, ano)

print(livro.titulo)
print(livro.autor)
print(livro.ano)
