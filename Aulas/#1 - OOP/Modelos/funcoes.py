from Modelos.classes import Personagem, Mago


def main():
    personagem = Personagem('Alfredo')
    print(personagem)
    print('\n\n')
    novo_mago = Mago('Ricardo')
    print(novo_mago.nome)
