import sqlite3
from tkinter import messagebox

class Alunos:
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
                            picture TEXT NOT NULL,
                            periodo INTEGER NOT NULL,
                            curso_id INTEGER NOT NULL,
                            FOREIGN KEY (curso_id) REFERENCES cursos (id)
                       );''')
    def register_student(self, estudante):
        self.c.execute("INSERT INTO estudantes (nome, email, tel, sexo, data_nascimento, endereco, picture, periodo, curso_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (estudante))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registro realizado com sucesso')
    def view_all_students(self, order):
        self.c.execute(f"SELECT estudantes.id AS id, estudantes.nome AS nome, estudantes.email, estudantes.tel, estudantes.sexo, estudantes.data_nascimento, estudantes.endereco, estudantes.periodo, cursos.nome AS nome_curso "
               f"FROM estudantes "
               f"JOIN cursos ON estudantes.curso_id = cursos.id "
               f"ORDER BY {order}")
        dados = self.c.fetchall()
        return dados

    def search_student(self, id):
        self.c.execute(f"SELECT * FROM estudantes LEFT JOIN cursos ON estudantes.curso_id = cursos.id WHERE estudantes.id=?", (id,))
        dados = self.c.fetchone()
        return dados 
    
    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, picture=?, periodo=?, curso_id=? WHERE id=?"
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
    def count_students_has_one_course(self, curso_id):
        self.c.execute("SELECT COUNT(*) FROM estudantes WHERE curso_id=?", (curso_id,))
        dados = self.c.fetchone()
        return dados[0]
    def get_students_one_discipline(self, curso_id, periodo):
        self.c.execute("SELECT nome FROM estudantes WHERE curso_id=? AND periodo=?", (curso_id, periodo))
        dados = self.c.fetchall()
        return dados