from modelos.classes import Dados


def main():
    base_de_dados = ("C:\\Users\\DPass\\OneDrive\\Área de Trabalho\\IEFP\\Programação Avançada em Python\\Aulas "
                     "Python Avançado\\Exercícios\\ExPandas\\Alunos_Exercicios.csv")

    analise = Dados(base_de_dados)

    print('------LER TABELA COMPLETA------')
    print(analise.ler_dados())

    print('------CRIAR COLUNA DE MÉDIA------')
    print(analise.media())

    print('------CRIAR COLUNA DE SITUAÇÃO------')
    print(analise.situacao())

    print('------FILTRAR ALUNOS APROVADOS------')
    print(analise.filtro_alunos_aprovados())

    print('------FILTRAR ALUNOS APROVADOS------')
    print(analise.filtro_alunos_reprovados())

    print('------FILTRAR ALUNOS APROVADOS E GUARDAR CSV------')
    analise.guardar('Alunos Aprovados', metodo=analise.filtro_alunos_aprovados)

    print('------FILTRAR ALUNOS REPROVADOS E GUARDAR CSV------')
    analise.guardar('Alunos Reprovados', metodo=analise.filtro_alunos_reprovados)

    print('------GUARDAR CSV COM NOVAS COLUNAS------')
    analise.guardar('Dados Completos')


if __name__ == '__main__':
    main()
