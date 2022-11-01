import tkinter
import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# cores --------------------------------
co0 = "#FFFFFF"  # white 
co1 = "#333333"  # black 
co2 = "#fcc058"  # orange
co3 = "#fff873"  # yellow 
co4 = "#34eb3d"   # green 
co5 = "#e85151"   # red 
fundo = "#3b3b3b"

#Configuration of window
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#divisao janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando o frame cima
    #jogador
app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=15, y=70)
app_1_linha = Label(frame_cima, text='', height=6, anchor='center', font=('Ivy 10 bold'), bg=co4, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_ponto = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_ponto.place(x=60, y=20)
    
app_div = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_div.place(x=126, y=20)
    #PC
app_2_ponto = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_ponto.place(x=160, y=20)
app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=215, y=70)
app_2_linha = Label(frame_cima, text='', height=6, anchor='center', font=('Ivy 10 bold'), bg=co5, fg=co0)
app_2_linha.place(x=254, y=0)

app_pc = Label(frame_baixo, text='', height=6, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=0)


global voce
global pc
global rodadas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rodadas = 5



#função logica do jogo
def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_pc

    if rodadas > 0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i

        app_pc['text'] = pc
        app_pc['fg'] = co1


        #escolhas iguais
        if voce == 'Pedra' and pc == 'Pedra':
            print('empate')
            frame_cima['bg'] = co3
            app_1['bg'] = co3
            app_1_ponto['bg'] = co3
            app_div['bg'] = co3
            app_2['bg'] = co3
            app_2_ponto['bg'] = co3
        if voce == 'Papel' and pc == 'Papel':
            print('empate')
            frame_cima['bg'] = co3
            app_1['bg'] = co3
            app_1_ponto['bg'] = co3
            app_div['bg'] = co3
            app_2['bg'] = co3
            app_2_ponto['bg'] = co3
        if voce == 'Tesoura' and pc == 'Tesoura':
            print('empate')
            frame_cima['bg'] = co3
            app_1['bg'] = co3
            app_1_ponto['bg'] = co3
            app_div['bg'] = co3
            app_2['bg'] = co3
            app_2_ponto['bg'] = co3

        #voce ganha
        if voce == 'Pedra' and pc == 'Tesoura':
            print('ganhou')
            frame_cima['bg'] = co4
            app_1['bg'] = co4
            app_1_ponto['bg'] = co4
            app_div['bg'] = co4
            app_2['bg'] = co4
            app_2_ponto['bg'] = co4
            pontos_voce += 10
        if voce == 'Papel' and pc == 'Pedra':
            print('ganhou')
            frame_cima['bg'] = co4
            app_1['bg'] = co4
            app_1_ponto['bg'] = co4
            app_div['bg'] = co4
            app_2['bg'] = co4
            app_2_ponto['bg'] = co4
            pontos_voce += 10
        if voce == 'Tesoura' and pc == 'Papel':
            print('ganhou')
            frame_cima['bg'] = co4
            app_1['bg'] = co4
            app_1_ponto['bg'] = co4
            app_div['bg'] = co4
            app_2['bg'] = co4
            app_2_ponto['bg'] = co4
            pontos_voce += 10

        #voce perde
        if voce == 'Pedra' and pc == 'Papel':
            print('perdeu')
            frame_cima['bg'] = co5
            app_1['bg'] = co5
            app_1_ponto['bg'] = co5
            app_div['bg'] = co5
            app_2['bg'] = co5
            app_2_ponto['bg'] = co5
            pontos_pc += 10
        if voce == 'Papel' and pc == 'Tesoura':
            print('perdeu')
            frame_cima['bg'] = co5
            app_1['bg'] = co5
            app_1_ponto['bg'] = co5
            app_div['bg'] = co5
            app_2['bg'] = co5
            app_2_ponto['bg'] = co5
            pontos_pc += 10
        if voce == 'Tesoura' and pc == 'Pedra':
            print('perdeu')
            frame_cima['bg'] = co5
            app_1['bg'] = co5
            app_1_ponto['bg'] = co5
            app_div['bg'] = co5
            app_2['bg'] = co5
            app_2_ponto['bg'] = co5
            pontos_pc += 10
    
        #atualiza pontos
        app_1_ponto['text'] = pontos_voce
        app_2_ponto['text'] = pontos_pc

        #atualiza rodadas
        rodadas -= 1
    else:
        fim_do_jogo()

#função inicia o jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=100, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=180, y=60)

#função termina o jogo
def fim_do_jogo():
    global rodadas
    global pontos_voce
    global pontos_pc
    
    pontos_pc = 0
    pontos_voce = 0
    rodadas = 5

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_voce = int(app_1_ponto['text'])
    jogador_pc = int(app_2_ponto['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text='Você GANHOU!!!', height=6, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=50, y=2)
    elif jogador_voce < jogador_pc:
        app_vencedor = Label(frame_baixo, text='Você PERDEU!!!', height=6, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=50, y=2)
    else:
        app_vencedor = Label(frame_baixo, text='EMPATE!!!', height=6, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=50, y=2)

    def jogarNovamente():
        app_1_ponto['text'] = '0'
        app_2_ponto['text'] = '0'
        app_vencedor.destroy()
        
        b_jogarNovamente.destroy()
        
        iniciar_jogo()
        
    b_jogarNovamente = Button(frame_baixo, command=jogarNovamente,  width=30, text='Jogar de novo', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_jogarNovamente.place(x=5, y=151)


#configurando frame baixo 
b_jogar = Button(frame_baixo, command=iniciar_jogo,  width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
b_jogar.place(x=5, y=151)


janela.mainloop()