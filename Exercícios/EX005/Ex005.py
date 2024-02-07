# Ex005 Sobrescrever Métodos em Herança
"""Altere a classe Ebook do Exercício 3 para que o método __str__ retorne a string no formato
Ebook: [titulo]
Autor: [autor]
Tamanho do Arquivo: [tamanho_arquivo] MB
Certifique-se de que o método __str__ da classe Livro permaneça inalterado.
"""

from datetime import datetime
import os

file_path = (r"C:\Users\DPass\OneDrive\Área de Trabalho\IEFP\Programação Avançada em Python\Aulas Python "
             r"Avançado\Exercícios\EX005\Ex005.py")


# Function to get file size
def get_file_size_mb(file_path):
    # Get the size of the file in bytes
    size_in_bytes = os.path.getsize(file_path)
    # Convert bytes to megabytes
    size_in_mb = size_in_bytes / (1024 * 1024)
    return round(size_in_mb, 3)


# Creates SuperClass Livro
class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo.strip().capitalize()
        self._autor = autor.strip().capitalize()
        self._ano = ano

    def __str__(self):
        return (f'Título: [{self._titulo}]\n'
                f'Autor: [{self._autor}]\n'
                f'Ano: [{self._ano}]\n')

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


# Creates daughter class
class Ebook(Livro):
    def __init__(self, tamanho_arquivo):
        super().__init__(titulo, autor, ano)
        self._tamanho_arquivo = tamanho_arquivo

    def __str__(self):
        return (f'Ebook: [{self._titulo}]\n'
                f'Autor: [{self._autor}]\n'
                f'Tamanho do arquivo: [{self._tamanho_arquivo}]MB')

    @property
    def tamanho_arquivo(self):
        return f'{self._tamanho_arquivo}'

    @tamanho_arquivo.setter
    def tamanho_arquivo(self, tamanho_arquivo):
        self._tamanho_arquivo = tamanho_arquivo


titulo = input('Digite o título do livro: ')
while True:
    if titulo.strip():
        break
    else:
        print(f'Não digitou um título válido... tente novamente')
        titulo = input('Digite o título do livro: ')

autor = input('Digite o autor do livro: ')
while True:
    if autor.strip():
        break
    else:
        print(f'Não digitou um autor válido... tente novamente')
        autor = input('Digite o autor do livro: ')

while True:
    try:
        ano = int(input('Digite o ano de publicação: '))
        if 1900 < ano <= datetime.today().year:
            break
        print("Por favor, forneça um ano válido.")
    except ValueError:
        print("Por favor, forneça um ano válido.")

print()
livro = Livro(titulo, autor, ano)
print(f'---Livros----')
print(livro)
tamanho_arquivo = get_file_size_mb(file_path)
ebook = Ebook(tamanho_arquivo)
print(f'---Ebooks----')
print(ebook)
