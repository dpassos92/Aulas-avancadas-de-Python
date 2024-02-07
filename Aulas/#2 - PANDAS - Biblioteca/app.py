from modelos.classes import Dados


def main():
    base_de_dados = ('C:\\Users\\DPass\\OneDrive\\Área de Trabalho\\IEFP\\Programação Avançada em Python\\Aulas Python '
                     'Avançado\\Aulas\\#2 - PANDAS - Biblioteca\\imoveis.csv')

    analise = Dados(base_de_dados)

    print('------LER TABELA COMPLETA------')
    print(analise.dados)

    print('------LER INÍCIO DA TABELA ------')
    print(analise.ler_inicio(10))

    print('------LER FIM DA TABELA ------')
    print(analise.ler_final(10))

    print('------LER TIPO DA TABELA ------')
    print(analise.ler_tipo())

    print('------LER COLUNAS DA TABELA ------')
    print(analise.ler_colunas())

    print('------LER TIPO DADO CABEÇALHO ------')
    print(analise.tipo_dado_cabecalho('Tipo'))

    print('------VER MÉDIA DE RENDAS POR TIPO DE IMÓVEL ------')
    print(analise.media_rendas('Tipo', 'Valor'))

    print('------VER PERCENTAGEM POR TIPO DE IMÓVEL ------')
    print(analise.percentagem_tipo())

    print('------MOSTRAR VALORES NULOS ------')
    print(analise.mostrar_valores_nulos().head(15))

    print('------REMOVER VALORES NULOS ------')
    analise.remover_valores_nulos(0)

    print('------MOSTRAR VALORES NULOS ------')
    print(analise.mostrar_valores_nulos().head(15))

    print('------ENCONTRAR VALORES A ZERO ------')
    print(analise.encontrar_valores_zero())

    print('------REMOVER VALORES A ZERO ------')
    print(analise.remover_valores_zero())

    print('------ENCONTRAR VALORES A ZERO ------')
    print(analise.encontrar_valores_zero())

    print('------FILTRO DE QUARTOS ------')
    print(analise.filtro_quarto(1))

    print('------FILTRO DE ALUGUER INFERIOR A: ------')
    print(analise.filtro_aluguer(500).head(35))

    print('------FILTRO QUARTO IGUAL A 1 E ALUGUER INFERIOR A 500 ------')
    print(analise.filtro_quarto_aluguer())

    print('------FILTRO QUARTO IGUAL OU SUPERIOR A 2 E ALUGUER INFERIOR A 750 E AREA MAIOR QUE 70------')
    print(analise.filtro_quarto_aluguer_area())

    #analise.guardar('teste123.csv', metodo=analise.media, separador=';')

    print('------CRIAR COLUNA DE DESPESAS MENSAIS------')
    print(analise.despesas_mensais())

    print('------CRIAR COLUNA DE DESPESAS ANUAIS------')
    print(analise.despesas_anuais())


if __name__ == '__main__':
    main()
