# Jogo de decisões cria finais diferentes baseados nas respostas dadas

# Finais diferentes na historia, com base nas respostas passadas

# Em uma guerra temos dois lados: LadoA e LadoB. Somente o ladoA irá vencer,
# e o ladoB irá perder!Decisões corretas -> vitória, que somente o ladoA irá
# conseguir!
import PySimpleGUI as sg


class JogoDeAventura:
    def __init__(self):
        # Norte = ladoA, Sul = ladoB
        self.pergunta1 = 'Você nasceu no Norte ou no Sul? (n/s)'
        # Espada = ladoA, Escudo = ladoB
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada/escudo)'
        # Linha de frente = ladoA, tatico = ladoB
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico)'
        self.finalHistoria1 = 'Heroi na linha de frente!'
        self.finalHistoria2 = 'Heroi protegendo as tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de batalhar!'

    def Iniciar(self):
        # layout
        layout = [
            [sg.Output(size=(50, 10), key='respostas')],
            [sg.Input(size=(25, 10), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()


jogo = JogoDeAventura()
jogo.Iniciar()
