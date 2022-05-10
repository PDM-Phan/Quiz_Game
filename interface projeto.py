from ast import Or
from locale import windows_locale
from PySimpleGUI import PySimpleGUI as sg
#TELA DE INTRODUÇÃO

def JanelaIntrod():
    sg.theme('DarkGreen7')
    layoutintrod = [
        [sg.Text('JOGO QUIZ SERES MITOLÓGICOS')],
        [sg.Text()],
        [sg.Text('esse jogo...')],
        [sg.Text()],
        [sg.Button('Logar como Administrador'), sg.Button('Logar como Usuário')]
    ]
    return sg.Window('QUIZ SERES MITOLÓGICOS', Layout = layoutintrod, finalize=True)

def JanelaUsuario():
    sg.theme('DarkGreen7')
    layoutusuar = [
        [sg.Text('FAÇA O LOGIN')],
        [sg.Text()],
        [sg.Text('Login: '), sg.Input(key = 'loginusuar')],
        [sg.Text('Senha'), sg.Input(key = 'senhausuar', password_char= '*')],
        [sg.Text()],
        [sg.Button('Cadastrar novo usuário')]
        ]
    return sg.Window('USUÁRIO(A)', Layout = layoutusuar, finalize=True)

def JanelaAdm():
    sg.theme('DarkGreen7')
    layoutadm = [
        [sg.Text('FAÇA O LOGIN')],
        [sg.Text()],
        [sg.Text('Login: '), sg.Input(key = 'loginadm')],
        [sg.Text('Senha'), sg.Input(key = 'senhaadm', password_char= '*')],
        [sg.Text()],
        [sg.Button('Cadastrar novo usuário')]
        ]
    return sg.Window('ADMINISTRADOR(A)', Layout = layoutadm, finalize=True)

def JanelaCad():
    sg.theme('DarkGreen7')
    layoutcad = [
        [sg.Text('CADASTRO')],
        [sg.Text()],
        [sg.Text('Digite seu nome:'), sg.Input(key='nome')],
        [sg.Text('Crie um login: '), sg.Input(key = 'novologin')],
        [sg.Text('Crie uma senha:'), sg.Input(key = 'novasenha', password_char= '*')],
        [sg.Text()],
        [sg.Checkbox('Cadastrar como usuário', key = 'usuario'), sg.Checkbox('Cadastrar como administrador', key = 'adm'),]
        [sg.Button('Cadastrar')]
        ]
    return sg.Window('CADASTRO', Layout = layoutcad, finalize=True)

def JanelaPerguntas():
    sg.theme('DarkGreen7')
    layoutperg = [
        [sg.Text('Pergunta: ', '#pergunta#')],
        [sg.Text('Alternativas: ' + '\nA: #X\nB: #Z\nC: #S\nD: #M\nE: #D')],
        [sg.Text('Qual a alternativa correta?')],
        [sg.Button('A'),sg.Button('B'),sg.Button('C'),sg.Button('D'),sg.Button('E'),],
        [sg.Text('Score' + ' #pontuação#')],
        [sg.Button('Próxima pergunta')]
    ]
    return sg.Window('PERGUNTAS', Layout = layoutperg, finalize=True)

#JANELAS

janela1, janela2, janela3, janela4, janela5 = JanelaIntrod(), None, None, None, None

#EVENTOS

while True:
    window, evento, valores = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and evento == sg.WIN_CLOSED:
        break

    #proxima janela
    if window == janela1 and evento == 'Logar como Administrador':
        janela2 = JanelaAdm()
        janela1.hide

    if window == janela1 and evento == 'Logar como Usuário':
        janela3 = JanelaUsuario()
        janela1.hide