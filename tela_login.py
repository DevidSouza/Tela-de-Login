from tkinter import *
from tkinter import ttk
from tkinter import messagebox


cores = {'azulbb': '#02a6d8', 'pretofra': '#302d2c', 'branco': '#f9f9f9'}
arq = 'dados_de_login.txt'

jan = Tk()

jan.title('')
jan.geometry('300x320')
jan.resizable(False, False)
jan.config(bg=cores['branco'])

imagem = PhotoImage(file='imagens/seta-esquerda.png', width=32, height=32)
jan.iconphoto(False, PhotoImage(file='imagens/login.png'))

estilo_da_janela = ttk.Style(jan)
estilo_da_janela.theme_use('clam')

frame_cima = Frame(jan, width=300, height=50, bg=cores['branco'])
frame_cima.grid(row=0, column=0)

label_login = Label(frame_cima, text='LOGIN', width=5, height=1, fg=cores['preto'], bg=cores['branco'], font=('YuGothicMedium 25'))
label_login.place(x=8, y=10)

frame_linha_azul = Frame(jan, width=280, height=5, bg=cores['azulbb'])
frame_linha_azul.grid(row=1, column=0)

frame_baixo = Frame(jan, width=300, height=260, bg=cores['branco'])
frame_baixo.grid(row=2, column=0)

label_nome = Label(frame_baixo, text='Nome/Email *', width=10, height=1, fg=cores['preto'], bg=cores['branco'], font=('Arial 10 bold'))
label_nome.place(x=17, y=20)

entry_nome = ttk.Entry(frame_baixo, width=28, font=('Arial 12'))
entry_nome.place(x=18, y=50)

label_senha = Label(frame_baixo, text='Senha *', width=6, height=1, fg=cores['preto'], bg=cores['branco'], font=('Arial 10 bold'))
label_senha.place(x=14, y=80)

entry_senha = ttk.Entry(frame_baixo, width=28, font=('Arial 12'), show='*')
entry_senha.place(x=18, y=110)


def login():
    nome = str(entry_nome.get().strip()).capitalize()
    senha = str(entry_senha.get().strip())

    try:
        abri_arquivo = open(arq, 'rt')
        dados = abri_arquivo.read().split()

        # captura o usuário para personalizar messagebox
        for p, d in enumerate(dados):
            if d == 'Senha:':
                if senha == dados[p + 1]:
                    usuario = dados[p - 1]

        if nome in dados and senha in dados:
            messagebox.showinfo('Logado Com Sucesso', f'Seja Bem-Vindo(a) de Volta, {usuario}!')
            objetos = [entry_nome, label_nome, label_senha, entry_senha, label_login, botao_login, botao_cadastre_se]
            for ob in objetos:
                ob.destroy()

            label_usuario_logado = Label(frame_cima, text=f'Usuário:      {usuario}', fg=cores['preto'], bg=cores['branco'],
                                font=('YuGothicMedium 20'))
            label_usuario_logado.place(x=2, y=4)

            label_bem_vindo = Label(frame_baixo, text='Seja bem vindo!', width=15, bg=cores['branco'], fg=cores['azulbb'], font=('Ivy 20'))
            label_bem_vindo.pack(anchor=CENTER, pady=40)
        elif nome == '' or senha == '':
            messagebox.showerror('Erro de Login', 'Você precisa preenchar todos os campos para acessar sua conta.')
            jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
        else:
            jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
            messagebox.showerror('Erro de Login', 'O nome ou o email que você inseriu não está\nconectado a uma conta. Encontre sua conta e entre.')
    except:
        jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
        abri_arquivo = open(arq, 'at')
        messagebox.showerror('Erro!', 'Você ainda não possue um cadastro.\nCadastre-se antes de fazer login.')

    jan.iconphoto(False, PhotoImage(file='imagens/login.png'))


botao_login = Button(frame_baixo, command=login, text='Login', width=31, height=1, pady=5,
                     bg=cores['azulbb'], fg=cores['branco'], font=('Arial 10 bold'), overrelief=RIDGE)
botao_login.place(x=18, y=170)


def cadastre_se():

    # funão que é chamada sempre que o usuário digita alguma coisa
    def on_write(*args):
        s = var.get()
        if len(s) > 0 and s.isalpha():
            var.set(s[:10])
        else:
            var.set(s[:-1])

    var = StringVar()
    # rastreia cada digitação do usuário e executa a função on_write
    var.trace_add('write', on_write)

    botao_login.place(x=5000), botao_cadastre_se.place(x=5000), entry_nome.place(x=3000)

    entry_senha.delete(0, END), entry_nome.delete(0, END)

    entry_senha['width'] = 12
    label_nome['text'] = 'Nome *'
    label_nome['width'] = 5


    def voltar():

        entry_senha.delete(0, END)

        objetos = [entry_nome_cadastro, label_usuario, entry_usuario, label_repetir_senha,
                   entry_repetir_senha, label_email, entry_email, botao_cadastrar, botao_voltar]
        for ob in objetos:
            ob.destroy()

        entry_nome.place(x=18, y=50)
        entry_nome['width'] = 28

        entry_senha['width'] = 28
        entry_senha.place(x=18, y=110)

        botao_login.place(x=18, y=170)

        botao_cadastre_se.place(x=68, y=220)


    botao_voltar = Button(frame_cima, width=32, command=voltar, height=32, bg=cores['branco'], image=imagem, relief=FLAT, overrelief=RIDGE)
    botao_voltar.place(x=250, y=5)

    entry_nome_cadastro = ttk.Entry(frame_baixo, textvariable=var, width=12, font=('Arial 12'))
    entry_nome_cadastro.place(x=18, y=50)

    label_usuario = Label(frame_baixo, text='Nome Usuário *', width=12, height=1, fg=cores['preto'], bg=cores['branco'], font=('Arial 10 bold'))
    label_usuario.place(x=148, y=20)

    entry_usuario = ttk.Entry(frame_baixo, width=12, font=('Arial 12'))
    entry_usuario.place(x=151, y=50)

    label_repetir_senha = Label(frame_baixo, text='Repita sua senha *', width=15, height=1,
                                fg=cores['preto'], bg=cores['branco'], font=('Arial 10 bold'))
    label_repetir_senha.place(x=146, y=80)

    entry_repetir_senha = ttk.Entry(frame_baixo, width=12, font=('Arial 12'), show='*')
    entry_repetir_senha.place(x=151, y=110)

    label_email = Label(frame_baixo, text='E-mail *', width=6, height=1, fg=cores['preto'], bg=cores['branco'], font=('Arial 10 bold'))
    label_email.place(x=18, y=150)

    entry_email = ttk.Entry(frame_baixo, width=27, font=('Arial 12'))
    entry_email.place(x=18, y=180)


    def cadastrar():
        nome = entry_nome_cadastro.get().strip()
        senha = entry_senha.get().strip()
        usuario = entry_usuario.get().strip().capitalize()
        email = entry_email.get().strip()

        try:
            abri_arquivo = open(arq, 'rt')
            dados = abri_arquivo.read().split()


            if nome == '' or senha == '' or usuario == '' or email == '':
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror('Erro de Registro','Não Deixe Nenhum Campo Vazio.\nPreencha Todos os campos.')

            elif len(nome) < 3:
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro de nome", "Quantidade de caracter insuficiente.\nO nome deve ter no mínimo 3 caracteres.")

            elif len(senha) < 8:
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro de senha", "A senha deve ter no mínimo 8 caracteres.")

            elif senha != entry_repetir_senha.get():
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro de senha", "Verifique se você repetiu a senha corretamente.")

            elif nome not in dados and senha not in dados \
                    and usuario not in dados and email not in dados:

                abri_arquivo = open(arq, 'at')
                abri_arquivo.write(f'Nome: {nome.capitalize()}\n'
                                    f'Usuario: {usuario.capitalize()}\n'
                                    f'Senha: {senha}\n'
                                    f'Email: {email}\n'
                                    f'-------------------------\n')

                messagebox.showinfo('Informação de Registro', 'Conta criada com sucesso!')

                objetos = [botao_cadastrar, entry_nome_cadastro, label_email, entry_email, label_usuario,
                           entry_usuario, entry_repetir_senha, label_repetir_senha, botao_voltar]

                for ob in objetos:
                    ob.destroy()

                label_nome['text'] = 'Nome/Email *'
                label_nome['width'] = 10
                entry_nome['width'] = 28
                entry_senha['width'] = 28

                botao_login.place(x=18, y=170)
                botao_cadastre_se.place(x=68, y=220)

                entry_nome.place(x=18, y=50)
                entry_senha.delete(0, END)

            elif nome in dados and senha in dados \
                    and usuario in dados and email in dados:

                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro", "Humm, parece que já existe uma pessoa cadastrada com essas\ninformações. "
                                                         "Por favor, verifique seus dados e tente novamente.")

            elif usuario in dados:
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro", f"Ops! O nome de usuário '{usuario}', já foi registrado.")

            elif email in dados:
                jan.iconphoto(False, PhotoImage(file='imagens/erro.png'))
                messagebox.showerror("Erro de cadastro", f"Ops! O email '{email}', já foi registrado.")

            else:
                messagebox.showinfo("Informação de cadastro", "Conta criada com sucesso!")

        except FileNotFoundError:
            abri_arquivo = open(arq, 'at')
            abri_arquivo.write(f'Nome: {nome.capitalize()}\n'
                               f'Usuario: {usuario.capitalize()}\n'
                               f'Senha: {senha}\n'
                               f'Email: {email}\n'
                               f'-------------------------\n')

            messagebox.showinfo('Informação de Registro', 'Conta criada com sucesso!')

            objetos[botao_cadastrar, entry_nome_cadastro, label_email, entry_email, label_usuario,
            entry_usuario, entry_repetir_senha, label_repetir_senha, botao_voltar]
            for ob in objetos:
                ob.destroy()

            label_nome['text'] = 'Nome/Email *'
            label_nome['width'] = 10
            entry_nome['width'] = 28
            entry_senha['width'] = 28

            botao_login.place(x=18, y=170)
            botao_cadastre_se.place(x=68, y=220)

            entry_nome.place(x=18, y=50)
            entry_senha.delete(0, END)


        jan.iconphoto(False, PhotoImage(file='imagens/login.png'))

    botao_cadastrar = Button(frame_baixo, command=cadastrar, text='Cadastrar', width=18, height=1, overrelief=RIDGE,
                             pady=5, padx=2, bg=cores['azulbb'], fg=cores['branco'], font=('Arial 10 bold'))
    botao_cadastrar.place(x=68, y=220)

botao_cadastre_se = Button(frame_baixo, command=cadastre_se, text='Cadastre-se', width=18, height=1, overrelief=RIDGE,
                           pady=5, padx=2, bg=cores['azulbb'], fg=cores['branco'], font=('Arial 10 bold'))
botao_cadastre_se.place(x=68, y=220)

jan.mainloop()
