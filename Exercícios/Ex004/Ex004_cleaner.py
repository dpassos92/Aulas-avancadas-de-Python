# Ex004 Complexidade com Herança
'''Crie uma classe Biblioteca que pode armazenar objetos do tipo Livro e Ebook.
Implemente métodos para adicionar livros à biblioteca e mostrar todos os livros.
Dica: Use uma lista para armazenar os objetos.
'''

from datetime import datetime
import os

file_path = (r"C:\Users\DPass\OneDrive\Área de Trabalho\IEFP\Programação Avançada em Python\Aulas Python "
             r"Avançado\Exercícios\EX004\Ex004.py")


def operacoes():
    while True:
        titulo = input('Digite o título do livro: ')
        titulo = validar_titulo(titulo)
        autor = input('Digite o autor do livro: ')
        autor = validar_autor(autor)
        ano = validar_ano()

        opcao = input('Deseja adicionar como um Livro ou um Ebook? [L/E] ').strip().upper()
        while opcao not in "LE":
            print('Opção inválida... tente novamente')
            opcao = input('Deseja adicionar como Livro ou um Ebook? [L/E] ').strip().upper()

        if opcao == 'L':
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
        elif opcao == 'E':
            tamanho_arquivo = get_file_size_mb(file_path)
            ebook = Ebook(titulo, autor, ano, tamanho_arquivo)
            biblioteca.adicionar_livro(ebook)

        continuar = input('Deseja adicionar mais livros/ebooks? [S/N] ').strip().upper()
        if continuar != 'S':
            break


# Function to get file size
def get_file_size_mb(file_path):
    # Get the size of the file in bytes
    size_in_bytes = os.path.getsize(file_path)
    # Convert bytes to megabytes
    size_in_mb = size_in_bytes / (1024 * 1024)
    return round(size_in_mb, 3)


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
        return f'Título: {self._titulo}'

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo.strip().capitalize()

    @property
    def autor(self):
        return f'Autor: {self._autor}'

    @autor.setter
    def autor(self, autor):
        self._autor = autor.strip().capitalize()

    @property
    def ano(self):
        ano_actual = datetime.today().year
        return f'Ano de Publicação: {self._ano}'

    @ano.setter
    def ano(self, ano):
        self._ano = ano


# Creates daughter class
class Ebook(Livro):
    def __init__(self, titulo, autor, ano, tamanho_arquivo):
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
        self._tamanho_arquivo = tamanho_arquivo


class Biblioteca:
    def __init__(self):
        self._livros = []
        self._ebooks = []

    def adicionar_livro(self, item):
        if isinstance(item, Livro):
            if isinstance(item, Ebook):
                self._ebooks.append(item)
            else:
                self._livros.append(item)
        else:
            print("Erro: O objeto não é do tipo Livro ou Ebook.")

    def mostrar_livros(self):
        print("Livros:")
        for livro in self._livros:
            print(livro)
        print("\nEbooks:")
        for ebook in self._ebooks:
            print(ebook)


# Main program
biblioteca = Biblioteca()  # Create the library object outside the loop

operacoes()

# show books in biblioteca
print(f'----Lista de Livros/Ebooks----')
biblioteca.mostrar_livros()
