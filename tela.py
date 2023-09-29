from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date

from main import *

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# criando janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam") 

def sobre():
    Help=Tk()
    Help.title("Sobre o projeto:")
    Help.geometry("450x300")
    Help.configure(background=co1)
    #Help.resizable(width=FALSE, height=FALSE)
    
    texto="Universidade Federal de Alagoas-UFAL\n\nProjeto AB2\n\nDisciplina: Algoritmos de Programaçção (APC)\n\n\n\n\n\n\nEquipe:\nAnderson da Silva Passos\nFrancisco Colatino de Lima"
    frame_help=Frame(Help,width=400, height=250, bg=co1,relief=RAISED)
    frame_help.place(relx=0.09, rely=0.05)
    h_nome=Label(frame_help, text=texto, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co0, compound=LEFT,justify="center")
    h_nome.place(x=0,y=0)
    Help.mainloop()



barrademenus=Menu(janela)


#menu geral opcoes
menuopcoes=Menu(barrademenus, tearoff=0)
menuopcoes.add_command(label="Sobre",command=sobre)
janela.config(menu=menuopcoes)



# Criando Frames

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5) #

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED) #
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW) #

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID) #
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW) #

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID) #
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5) #

# Trabalhando no frame logo

global imagem, imagem_string, l_imagem

#varivael imagem
imagem_string=''  #corrigir bugs


app_lg = Image.open('logo.png').resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)


imagem = Image.open('logo.png').resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=410, y=10)

# SALVANDO ARQUIVOS


#função logo
def imagem_logo():  #corrigir bugs--------------------------------
    global imagem, l_imagem
    imagem=Image.open("logo.png")
    imagem=imagem.resize((130,130))
    imagem=ImageTk.PhotoImage(imagem)

    l_imagem=Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=410,y=10)
#--------------------------------------------------------
# CRUD
# create

def adicionar():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get_date()
    endereco = e_endereco.get()
    img = imagem_string
    curso=c_curso.get().capitalize()

    lista=[nome,email,tel,sexo,data,endereco,curso,img]

    for item in lista:
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    sistema_de_registro.register_student(lista)

    limpando_inputs()

    imagem_logo()
    mostrar_alunos()

# search

def procurar(id=None):
    global imagem, imagem_string, l_imagem
    if (id == None):
        id = int(e_procurar.get())
    else:
        e_procurar.delete(0, END)
        id = id[0]
        e_procurar.insert(END, id)
    dados = sistema_de_registro.search_student(id)
    
    limpando_inputs()

    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem).resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=410, y=10)


def atualizar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get_date()
    endereco = e_endereco.get()
    img = imagem_string
    curso=c_curso.get().capitalize()

    #adicionando o curso na lista


    lista=[nome,email,tel,sexo,data,endereco,curso,img,id_aluno]

    for item in lista:
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    sistema_de_registro.update_student(lista)

    limpando_inputs() 
    imagem_logo()

    mostrar_alunos()
# Criando os campos de entrada

def deletar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())
    
    sistema_de_registro.delete_student(id_aluno)

    limpando_inputs()

    imagem_logo()
    mostrar_alunos()

def limpando_inputs():
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=25, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=25, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=137, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=140, y=160)

l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=227, y=10)
data_nascimento = DateEntry(frame_detalhes, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
data_nascimento.place(x=230, y=40)

l_endereco = Label(frame_detalhes, text="Endereco *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=227, y=70)
e_endereco = Entry(frame_detalhes, width=20, justify='left', relief='solid')
e_endereco.place(x=230, y=100)

l_curso = Label(frame_detalhes, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=227, y=130)

cursos=sistema_de_registro.get_all_courses()
c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = cursos
c_curso.place(x=230, y=160)

def atualizar_cursos():
    cursos = sistema_de_registro.get_all_courses()
    c_curso['values'] = cursos
# funcao para escolher imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    if (imagem == () or imagem == ''):
        imagem_logo()
    else:
        imagem_string = imagem
        imagem = Image.open(imagem).resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=410, y=10)

        botao_carregar['text'] = 'Trocar de foto'

botao_carregar = Button(frame_detalhes, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=410, y=160)

# Tabela alunos
def mostrar_alunos(order='id'): #

    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    df_list = sistema_de_registro.view_all_students(order)

    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=list_header, show='headings')
    
    # Scrollbar vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview) #
    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky=NSEW)
    vsb.grid(column=1, row=1, sticky=NS)
    hsb.grid(column=0, row=2, sticky=EW)
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'center', 'center', 'center', 'center', 'center', 'center']
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_aluno.heading(col, command=lambda c=col: atualizando_ordem(c), text=col.title(), anchor=NW)

        tree_aluno.column(col, width=h[n], anchor=hd[n])
        n+=1
    for item in df_list:
        tree_aluno.insert('', 'end', values=item)
    def on_click(event):
        if (tree_aluno.selection() != ()):
            procurar(tree_aluno.item(tree_aluno.selection()[0], 'values'))
    tree_aluno.bind('<Return>', on_click)
    atualizar_cursos()

def atualizando_ordem(coluna):
    infos = {
        'id': 'id', 
        'Nome': 'nome', 
        'email': 'email', 
        'Telefone': 'tel', 
        'sexo': 'sexo', 
        'Data': 'data_nascimento', 
        'Endereço': 'endereco', 
        'Curso': 'curso'
    }
    mostrar_alunos(infos[coluna])
    

# Procurar aluno

frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno pelo ID", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes

app_img_add = Image.open('mais.png').resize((25,25))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_botoes, command=adicionar, image=app_img_add, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('atualizar.png').resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('botao-apagar.png').resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, relief=GROOVE, text=' Excluir', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# LINHA

l_linha = Label(frame_botoes, relief=GROOVE, text='', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co2, fg=co1)
l_linha.place(x=245, y=15)

mostrar_alunos()
janela.mainloop()
