'''por implementar
from datetime import datetime


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


class Ebook(Livro):
    def __init__(self, tamanho_arquivo):
        super().__init__(titulo, autor, ano)
        self._tamanho_arquivo = tamanho_arquivo

    def __str__(self):
        return (f'Ebook: {self._titulo}\n'
                f'Autor: {self._autor}\n'
                f'Ano: {self._ano}\n'
                f'Tamanho: {self._tamanho_arquivo}MB')

    @property
    def tamanho_arquivo(self):
        return f'{self._tamanho_arquivo}'

    @tamanho_arquivo.setter
    def tamanho_arquivo(self, tamanho_arquivo):
        self._tamanho_arquivo = tamanho_arquivo'''
