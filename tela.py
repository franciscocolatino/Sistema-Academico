from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import DateEntry

from db.main import *

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
  
co7 = "#ef5350"   # vermelha
co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 = "#003452" # azul
#criando janela
janela=Tk()
janela.title("Sistema Acadêmico")
janela.geometry("810x545")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

janelatabs=ttk.Notebook(janela)
janelatabs.place(x=0,y=0,width=810,height=545)
tb1=Frame(janelatabs)
tb2=Frame(janelatabs)

janelatabs.add(tb1, text="Registro")
janelatabs.add(tb2, text="Disciplinas")

def sobre():
    Help=Tk()
    Help.title("Sobre o projeto:")
    Help.geometry("450x300")
    Help.configure(background=co1)
    Help.resizable(width=FALSE, height=FALSE)
    
    texto="Universidade Federal de Alagoas-UFAL\n\nProjeto AB2\n\nDisciplina: Algoritmos de Programaçção (APC)\n\n\n\n\n\n\nEquipe:\nAnderson da Silva Passos\nFrancisco Colatino de Lima"
    frame_help=Frame(Help,width=400, height=250, bg=co1,relief=RAISED)
    frame_help.place(relx=0.09, rely=0.05)
    h_nome=Label(frame_help, text=texto, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co0, compound=LEFT,justify="center")
    h_nome.place(x=0,y=0)
    Help.mainloop()


def tela_alunos_disciplinas(disciplina, periodo, curso_name):
    global frame_tabela_aluno
    aluno=Tk()
    aluno.title(curso_name)
    aluno.geometry("600x450")
    aluno.configure(background=co1)
    aluno.resizable(width=FALSE, height=FALSE)
    frame_nome_aluno=Frame(aluno,width=600, height=50, bg=co1,relief=RAISED)
    frame_nome_aluno.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)
    frame_tabela_aluno=Frame(aluno,width=600, height=450, bg=co1,relief=RAISED)
    frame_tabela_aluno.grid(row=1, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

    l_disciplina_aluno=Label(frame_nome_aluno, text=f"Disciplina: {disciplina}", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
    l_disciplina_aluno.place(x=50,y=7)

    l_periodo_aluno=Label(frame_nome_aluno, text=f"Período: {periodo}", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
    l_periodo_aluno.place(x=370,y=7)
    mostrar_disciplina(curso_name, periodo)
    aluno.mainloop()
    

#MENU
barrademenus=Menu(janela)
#menu geral opcoes
menuopcoes=Menu(barrademenus, tearoff=0)
menuopcoes.add_command(label="Sobre",command=sobre)
janela.config(menu=menuopcoes)

# Criando Frames

#Aba1
frame_logo=Frame(tb1,width=850, height=52, bg=co1)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes=Frame(tb1,width=100, height=200, bg=co1,relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details=Frame(tb1,width=700, height=100, bg=co1,relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela=Frame(tb1,width=800, height=100, bg=co1,relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW,columnspan=5)

#Aba 2
frame_logo2=Frame(tb2,width=850, height=52, bg=co1)
frame_logo2.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes2=Frame(tb2,width=100, height=200, bg=co1,relief=RAISED)
frame_botoes2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details2=Frame(tb2,width=700, height=100, bg=co1,relief=SOLID)
frame_details2.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela2=Frame(tb2,width=800, height=100, bg=co1,relief=SOLID)
frame_tabela2.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW,columnspan=5)


# Trabalhando no frame logo

global imagem, imagem_string, l_imagem

imagem_string=''  #corrigir bugs

app_lg = Image.open('images/logo.png').resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema Acadêmico", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co10, fg=co1)
app_logo.place(x=5, y=0)

app_logo2=Label(frame_logo2, image=app_lg, text=" Sistema Acadêmico", width=850, compound=LEFT, anchor=NW, font=("Verdana 15"), bg=co10, fg=co1)
app_logo2.place(x=5,y=0)

imagem = Image.open('images/logo.png').resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=410, y=10)

#função logo
def imagem_logo():
    global imagem, l_imagem
    imagem=Image.open("images/logo.png")
    imagem=imagem.resize((130,130))
    imagem=ImageTk.PhotoImage(imagem)

    l_imagem=Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=410,y=10)

# CRUD

def criar():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get_date()
    endereco = e_endereco.get()
    img = imagem_string
    periodo = c_periodo.get()
    curso_name=c_curso.get().capitalize()
    course_id = cursos_db.check_course_exists(curso_name)

    lista=[nome,email,tel,sexo,data,endereco,img,periodo,course_id]
    for item in lista:
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    if (not(course_id)):
        course_id = cursos_db.create_course(curso_name)
    lista=[nome,email,tel,sexo,data,endereco,img,periodo,course_id]

    alunos_db.register_student(lista)

    limpando_inputs()
    imagem_logo()
    mostrar_alunos()

def procurar(id=None):
    global imagem, imagem_string, l_imagem
    if (id == None):
        id = int(e_procurar.get())
    else:
        e_procurar.delete(0, END)
        id = id[0]
        e_procurar.insert(END, id)
    dados = alunos_db.search_student(id)

    if dados==None:
        messagebox.showerror("Erro", "Esse aluno não existe!")
    else:
        limpando_inputs()
        e_nome.insert(END, dados[1])
        e_email.insert(END, dados[2])
        e_tel.insert(END, dados[3])
        c_sexo.insert(END, dados[4])
        data_nascimento.insert(END, dados[5])
        e_endereco.insert(END, dados[6])
        c_periodo.insert(END, dados[-4])
        c_curso.insert(END, dados[-1])

        imagem = dados[7]
        imagem_string = imagem

        imagem = Image.open(imagem).resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)

        l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
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
    periodo = c_periodo.get()
    curso_name = c_curso.get().capitalize()
    curso_id = cursos_db.check_course_exists(curso_name)
    if (not(curso_id)):
        curso_id = cursos_db.create_course(curso_name)
    lista=[nome,email,tel,sexo,data,endereco,img,periodo,curso_id ,id_aluno]

    for item in lista:
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    alunos_db.update_student(lista)

    limpando_inputs() 
    imagem_logo()
    mostrar_alunos()

def deletar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())
    aluno = alunos_db.search_student(id_aluno)
    curso_id = int(aluno[-2])

    alunos_db.delete_student(id_aluno)
    countOne = cursoDisciplina_db.count_discipline_has_one_course(curso_id)
    countTwo = alunos_db.count_students_has_one_course(curso_id)

    if (countOne == 0 and countTwo == 0):
        cursos_db.delete_course(curso_id)
        atualizar_cursos()
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
    c_periodo.delete(0, END)
    c_curso2.delete(0, END)
    e_periodo2.delete(0, END)
    c_disciplina2.delete(0, END)

def atualizar_cursos():
    cursos = cursos_db.get_all_courses()
    c_curso['values'] = cursos
    c_curso2['values'] = cursos

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    if (imagem == () or imagem == ''):
        imagem_logo()
    else:
        imagem_string = imagem
        imagem = Image.open(imagem).resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=410, y=10)

        botao_carregar['text'] = 'Trocar de foto'

def atualizando_ordem(coluna):
    infos = {
        'id': 'id', 
        'Nome': 'nome', 
        'email': 'email', 
        'Telefone': 'tel', 
        'sexo': 'sexo', 
        'Data': 'data_nascimento', 
        'Endereço': 'endereco', 
        'Curso': 'nome_curso',
        'P': 'periodo'
    }
    mostrar_alunos(infos[coluna])
    
# Tabela alunos
def mostrar_alunos(order='id'): #

    lista_cabecalho = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'P', 'Curso']

    dados_lista = alunos_db.view_all_students(order)

    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=lista_cabecalho, show='headings')
    
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
    h = [40, 150, 150, 70, 70, 70, 120, 10, 100]
    n = 0

    for col in lista_cabecalho:
        tree_aluno.heading(col, command=lambda c=col: atualizando_ordem(c), text=col.title(), anchor=NW)

        tree_aluno.column(col, width=h[n], anchor=hd[n])
        n+=1
    for item in dados_lista:
        tree_aluno.insert('', 'end', values=item)
    def on_click_procurar(event):
        if (tree_aluno.selection() != ()):
            procurar(tree_aluno.item(tree_aluno.selection()[0], 'values'))
    tree_aluno.bind('<Button-1>', on_click_procurar)
    
    atualizar_cursos()


def criar_disciplinas():

    # creating a treeview with dual scrollbars
    list_header = ["ID","Curso","Disciplina","Período"]

    tree_aluno = ttk.Treeview(frame_tabela2, selectmode="extended",columns=list_header, show="headings",height=9)
    
    # view all students
    df_list = cursoDisciplina_db.get_all_courses_disciplinas()

    

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela2, orient="vertical", command=tree_aluno.yview)   
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela2, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center"]
    h=[45,400,200,125]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        
        tree_aluno.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)
    def on_click_procurar(event):
        if (tree_aluno.selection() != ()):
            procurar_disciplina(tree_aluno.item(tree_aluno.selection()[0], 'values'))
    def on_click_tela(event):
        if (tree_aluno.selection() != ()):
            dados = tree_aluno.item(tree_aluno.selection()[0], 'values')

            periodo = dados[3]
            disciplina_name = dados[2]
            curso_name = dados[1]
            tela_alunos_disciplinas(disciplina_name, periodo, curso_name)
    tree_aluno.bind('<Button-1>', on_click_procurar)
    tree_aluno.bind('<Return>', on_click_tela)

def mostrar_disciplina(curso_name, periodo):
    # creating a treeview with dual scrollbars
    list_header = ["Alunos"]

    tree_aluno = ttk.Treeview(frame_tabela_aluno, selectmode="extended",columns=list_header, show="headings",height=18)
    curso_id = cursos_db.check_course_exists(curso_name)
    # view all students
    df_list = alunos_db.get_students_one_discipline(curso_id, periodo)
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela_aluno, orient="vertical", command=tree_aluno.yview)   
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela_aluno, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["center"]
    h=[570]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        
        tree_aluno.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

botao_carregar = Button(frame_details, command=escolher_imagem, text='CARREGAR FOTO', width=17, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=410, y=160)

# Criando os campos de entrada

#Aba1
l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=25, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=25, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=137, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=140, y=160)

l_data_nascimento = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=227, y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
data_nascimento.place(x=230, y=40)

l_endereco = Label(frame_details, text="Endereco *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=227, y=70)
e_endereco = Entry(frame_details, width=20, justify='left', relief='solid')
e_endereco.place(x=230, y=100)

l_curso = Label(frame_details, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=227, y=130)

cursos = cursos_db.get_all_courses()
c_curso = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = cursos
c_curso.place(x=230, y=160)

l_periodo = Label(frame_details, text="Período *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_periodo.place(x=227, y=190)


periodos = ('1','2','3','4','5','6','7','8')
c_periodo = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_periodo['values'] = periodos
c_periodo.place(x=230, y=210)

#--------------------------------------------------------------------
#aba2
l_curso2=Label(frame_details2, text="Curso*", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_curso2.place(x=40,y=3)
c_curso2=ttk.Combobox(frame_details2,width=20,font=("Ivy 8 bold"), justify="center")
c_curso2['values']=(cursos)
c_curso2.place(x=40,y=40)

periodos=('1','2','3','4','5','6','7','8')
l_periodo2=Label(frame_details2, text="Período*", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_periodo2.place(x=300,y=3)
e_periodo2=ttk.Combobox(frame_details2,width=20,font=("Ivy 8 bold"), justify="center")
e_periodo2['values']=(periodos) 
e_periodo2.place(x=300,y=40)

l_disciplina2=Label(frame_details2, text="Disciplina*", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_disciplina2.place(x=40,y=100)
c_disciplina2=Entry(frame_details2, width=20, justify="left", relief="solid")
c_disciplina2.place(x=40,y=140)

imagem2=Image.open("images/logo.png")
imagem2=imagem2.resize((150,150))
imagem2=ImageTk.PhotoImage(imagem2)

l_imagem2=Label(frame_details2, image=imagem2, bg=co1, fg=co4)
l_imagem2.place(x=290,y=70)


#Procurar aluno aba1
frame_procurar=Frame(frame_botoes,width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome=Label(frame_procurar, text="Procurar Aluno [Entra ID]", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

e_procurar=Entry(frame_procurar, width=5, justify="center", relief="solid", font=("Ivy 10"))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar=Button(frame_procurar,command=procurar,text="Procurar",width=6, anchor=CENTER, overrelief=RIDGE,
                      font=('Ivy 7 bold'), bg=co1,fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)


def adicionar_disciplina():
    nome = c_disciplina2.get()
    periodo = e_periodo2.get()
    curso_name=c_curso2.get().capitalize()

    course_id = cursos_db.check_course_exists(curso_name)
    disciplina =[nome,periodo, course_id]

    for item in disciplina :
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    if (not(course_id)):
        course_id = cursos_db.create_course(curso_name)
        atualizar_cursos()
    disciplina =[nome,periodo]
    disciplina_id = disciplina_db.create_discipline(disciplina)
    cursoDisciplina_db.create_course_disciplina([course_id, disciplina_id])


    limpando_inputs()
    criar_disciplinas()

def deletar_disciplina():
    curso_disciplina_id = int(e_procurar2.get())
    if (curso_disciplina_id == ''):
            messagebox.showerror('Erro', 'Preencha o campo "Procurar disciplina" informando o id')
            return
    disciplina_id, curso_id = cursoDisciplina_db.get_discipline_and_course_id(curso_disciplina_id) 

    cursoDisciplina_db.delete_course_discipline(curso_disciplina_id)
    disciplina_db.delete_discipline(disciplina_id)
    countOne = cursoDisciplina_db.count_discipline_has_one_course(curso_id)
    countTwo = alunos_db.count_students_has_one_course(curso_id)

    if (countOne == 0 and countTwo == 0):
        cursos_db.delete_course(curso_id)
        atualizar_cursos()
    limpando_inputs()
    criar_disciplinas()

def procurar_disciplina(id=None): #
    if (id == None):
        id = int(e_procurar2.get())
    else:
        e_procurar2.delete(0, END)
        id = id[0]
        e_procurar2.insert(END, id)
    dados = cursoDisciplina_db.get_discipline_with_course(id)
    if dados==None:
        messagebox.showerror("Erro", "Esse disciplina não existe")
    else:
        limpando_inputs()
        c_curso2.insert(END, dados[1])
        c_disciplina2.insert(END, dados[2])
        e_periodo2.insert(END, dados[3])

def atualizar_disciplina():

    cursoDisciplina_id = int(e_procurar2.get())

    nome = c_disciplina2.get()
    periodo = int(e_periodo2.get())
    curso_name=c_curso2.get().capitalize()
    lista=[nome,periodo,curso_name]

    course_id = cursos_db.check_course_exists(curso_name)

    for item in lista:
        if (item == ''):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    if (not(course_id)):
        course_id = cursos_db.create_course(curso_name)

    dados = cursoDisciplina_db.get_discipline_and_course_id(cursoDisciplina_id)
    disciplina_id = dados[0]

    disciplina_db.update_discipline([nome, periodo, disciplina_id])
    cursoDisciplina_db.update_course_discipline([course_id, disciplina_id, cursoDisciplina_id])

    limpando_inputs() 
    criar_disciplinas()

#Procurar disciplina aba2
frame_procurar2=Frame(frame_botoes2,width=40, height=55, bg=co1, relief=RAISED)
frame_procurar2.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome2=Label(frame_procurar2, text="Procurar Disciplina [Entra ID]", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome2.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

e_procurar2=Entry(frame_procurar2, width=5, justify="center", relief="solid", font=("Ivy 10"))
e_procurar2.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar2=Button(frame_procurar2,command=procurar_disciplina,text="Procurar",width=9, anchor=CENTER, overrelief=RIDGE,
                      font=('Ivy 7 bold'), bg=co1,fg=co0)
botao_procurar2.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)
#--------------------------------------------------------------------

#botoes aba1
app_img_adicionar=Image.open("images/mais.png")
app_img_adicionar=app_img_adicionar.resize((25,25))
app_img_adicionar=ImageTk.PhotoImage(app_img_adicionar)
app_adicionar=Button(frame_botoes, command=criar,image=app_img_adicionar,relief=GROOVE, text=" Adicionar",width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1,fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)


app_img_atualizar=Image.open("images/atualizar.png")
app_img_atualizar=app_img_atualizar.resize((25,25))
app_img_atualizar=ImageTk.PhotoImage(app_img_atualizar)
app_aualizar=Button(frame_botoes,command=atualizar,image=app_img_atualizar,relief=GROOVE, text=" Atualizar",width=100,compound=LEFT, overrelief=RIDGE,font=('Ivy 11'), bg=co1,fg=co0)
app_aualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)


app_img_deletar=Image.open("images/botao-apagar.png")
app_img_deletar=app_img_deletar.resize((25,25))
app_img_deletar=ImageTk.PhotoImage(app_img_deletar)
app_deletar=Button(frame_botoes,command=deletar,image=app_img_deletar,relief=GROOVE, text=" Deletar",width=100,compound=LEFT, overrelief=RIDGE,font=('Ivy 11'), bg=co1,fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)


#botoes aba2
app_adicionar2=Button(frame_botoes2, command=adicionar_disciplina,image=app_img_adicionar,relief=GROOVE, text=" Adicionar",width=100,compound=LEFT, overrelief=RIDGE,font=('Ivy 11'), bg=co1,fg=co0)
app_adicionar2.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)


app_atualizar2=Button(frame_botoes2,command=atualizar_disciplina,image=app_img_atualizar,relief=GROOVE, text=" Atualizar",width=100,compound=LEFT, overrelief=RIDGE,font=('Ivy 11'), bg=co1,fg=co0)
app_atualizar2.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)


app_deletar2=Button(frame_botoes2,command=deletar_disciplina,image=app_img_deletar,relief=GROOVE, text=" Deletar",width=100,compound=LEFT, overrelief=RIDGE,font=('Ivy 11'), bg=co1,fg=co0)
app_deletar2.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Iniciando aplicação
mostrar_alunos()
criar_disciplinas()
janela.mainloop()
