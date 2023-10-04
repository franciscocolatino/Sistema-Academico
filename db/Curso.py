import sqlite3
from tkinter import messagebox

class Curso:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS cursos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL UNIQUE
                            );''')
    def create_course(self, curso):
        self.c.execute("INSERT INTO cursos (nome) VALUES (?)", (curso,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Curso cadastrado com sucesso')
        course_id = self.c.lastrowid
        return course_id
    def get_all_courses(self):
        self.c.execute("SELECT nome FROM cursos")
        dados = self.c.fetchall()
        valores = set()
        for tupla in dados:
            valores.add(tupla[0]) 
        print(tuple(valores))
        return tuple(valores)
    def check_course_exists(self, name):
        self.c.execute("SELECT id FROM cursos WHERE nome=?", (name,))
        curso_id = self.c.fetchone()
        if curso_id:
            print(curso_id[0])
            return curso_id[0]
        else:
            return False
    def get_course_id(self, name):
        self.c.execute("SELECT id FROM cursos WHERE nome=?", (name,))
        dados = self.c.fetchone()
        return dados
    def delete_course(self, id):
        self.c.execute("DELETE FROM cursos WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Curso com ID:{id} foi excluido!')