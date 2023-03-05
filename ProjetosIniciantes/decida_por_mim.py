# Faça uma pergunta para o programa para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg


class DecidaPorMim:

    def __init__(self):
        self.resposta = [
            'Com certeza, só faz!',
            'Tanto faz, vc que sabe!',
            'Melhor não fazer isso!',
            'Pelo amor de Deus, não!'
        ]

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50, 10))],
            [sg.Button('Decida por mim')],
            [sg.Button('Sair')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            # ler os valores
            self.eventos, self.valores = self.janela.Read()
            # fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.resposta))


decida = DecidaPorMim()
decida.Iniciar()
