import pandas as pd


class Dados:
    def __init__(self, dados):
        self._dados = pd.read_csv(dados)

    @property
    def dados(self):
        return self._dados

    def ler_dados(self):
        return self.dados

    def media(self):
        media_exercicios = (self.dados['Exercício 1'] + self.dados['Exercício 2'] + self.dados['Exercício 3'] +
                            self.dados['Exercício 4'] + self.dados['Exercício 5']) / 5
        self.dados['Nota Final'] = media_exercicios
        return self.dados

    def situacao(self):
        situacoes = []
        for nota in self.dados['Nota Final']:
            if nota >= 9.5:
                situacoes.append('Aprovado')
            else:
                situacoes.append('Reprovado')
        self.dados['Situação'] = situacoes
        return self.dados

    def filtro_alunos_aprovados(self):
        filtro_aprovados = self.dados['Situação'] == 'Aprovado'
        return self.dados[filtro_aprovados]

    def filtro_alunos_reprovados(self):
        filtro_reprovados = self.dados['Situação'] == 'Reprovado'
        return self.dados[filtro_reprovados]

    def guardar(self, nome_arquivo, metodo=None, separador=';'):  # UTF-8-sig #
        # decidir o que guardar
        if metodo:
            df_para_guardar = metodo()
        else:
            df_para_guardar = self.dados

        # guardar o que foi decidido acima
        df_para_guardar.to_csv(nome_arquivo, index=False, sep=separador, encoding='UTF-8-sig')
        print(f'Nome do arquivo guardado com sucesso')