# Ex001 Getters e Setters Básicos
"""Crie uma classe Livro com atributos privados titulo, autor, ano de publicação.
Utilize getterse setters para aceder e modificar estes atributos.
Os setters devem garantir que tanto o título quanto o nome do autor sejam strings não vazias
e que o ano seja num intervalo razoável entre 1900 e o ano atual.
"""

from datetime import datetime


# Input validation functions
def validar_titulo(titulo):
    while True:
        if titulo.strip():
            return titulo.strip().capitalize()
        else:
            print(f'Não digitou um título válido... tente novamente')
            titulo = input('Digite o título do livro: ')


def validar_autor(autor):
    while True:
        if autor.strip():
            return autor.strip().capitalize()
        else:
            print(f'Não digitou um autor válido... tente novamente')
            autor = input('Digite o autor do livro: ')


def validar_ano():
    while True:
        try:
            ano = int(input('Digite o ano de publicação: '))
            if 1900 < ano <= datetime.today().year:
                return ano
            print("Por favor, forneça um ano válido.")
        except ValueError:
            print("Por favor, forneça um ano válido.")


class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo.strip().capitalize()
        self._autor = autor.strip().capitalize()
        self._ano = ano


    @property
    def titulo(self):
        return f'Não digitou título...' if titulo == "" else f'Título: {self._titulo}'

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo.strip().capitalize()

    @property
    def autor(self):
        return f'Não digitou o autor...' if autor == "" else f'Autor: {self._autor}'

    @autor.setter
    def autor(self, autor):
        self._autor = autor.strip().capitalize()


    @property
    def ano(self):
        ano_actual = datetime.today().year
        return f'Não digitou um ano válido...' if ano <= 1900 or ano > ano_actual else f'Ano de Publicação: {self._ano}'

    @ano.setter
    def ano(self, ano):
        self._ano = ano


titulo = input('Digite o título do livro: ')
titulo = validar_titulo(titulo)
autor = input('Digite o autor do livro: ')
autor = validar_autor(autor)
ano = validar_ano()


livro = Livro(titulo, autor, ano)

print(livro.titulo)
print(livro.autor)
print(livro.ano)


