import sqlite3
from tkinter import messagebox

class SistemaAcademico:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            picture TEXT NOT NULL);''')
    def register_student(self, estudante):
        self.c.execute("INSERT INTO estudantes (nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (estudante))
        self.conn.commit()

        # mostrando msg de sucesso
        messagebox.showinfo('Sucesso', 'Registro realizado com sucesso')
    def view_all_students(self, order):
        self.c.execute(f"SELECT * FROM estudantes ORDER BY {order}")
        dados = self.c.fetchall()
        return dados


    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados 
    
    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, novos_valores)
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', f'Estudante com ID:{novos_valores[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi excluido!')
    def get_all_courses(self):
        self.c.execute("SELECT curso FROM estudantes")
        dados = self.c.fetchall()
        valores = set()
        for tupla in dados:
            valores.add(tupla[0]) 
        return tuple(valores)

# Instanciando a classe Sistema de registro

sistema_academico = SistemaAcademico()

#estudante = ('Elena', 'elena@gmail.com', '28247287', 'F', '01/05/2007', 'SP, Brasil', 'Medicina', 'imagem2.png')
#sistema_de_registro.register_student(estudante)

#sistema_de_registro.view_all_students()
#sistema_de_registro.get_all_courses()

# TRATAR O ERRO QUANDO ID INEXISTENTE
#aluno = sistema_de_registro.search_student(3)

#estudante = ('Elenaaaaaaaaa', 'elena@gmail.com', '28378179', 'F', '01/05/2007', 'SP, Brasil', 'Medicina2', 'imagem2.png', 2)
#aluno = sistema_de_registro.update_student(estudante)
#sistema_de_registro.search_student(2)

#sistema_de_registro.delete_student(2)
#sistema_de_registro.view_all_students()

