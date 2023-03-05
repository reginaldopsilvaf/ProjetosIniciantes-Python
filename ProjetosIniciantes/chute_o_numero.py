# Projeto 3 - Chute o número
# objetivo: Criar um algoritmo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg


class ChuteONumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu chute:', size=(20, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20, 10))]
        ]
        # criar uma janela
        self.janela = sg.Window('Chute o número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber os valores na tela
                self.LerValoresDaTela()
                # Fazer alguma coisa com esses valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            self.LerValoresDaTela()
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            self.LerValoresDaTela()
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Vc acertou!')
                            break

        except:
            print('Favor digitar apenas números inteiros positivos')
            self.iniciar()

    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.iniciar()
