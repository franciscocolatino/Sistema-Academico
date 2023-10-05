import sqlite3
from tkinter import messagebox

class Disciplina:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS disciplinas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            periodo INTEGER NOT NULL
                            );''')
    def create_discipline(self, disciplina):
        self.c.execute("INSERT INTO disciplinas (nome, periodo) VALUES (?, ?)", (disciplina))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Disciplina cadastrado com sucesso')
        discipline_id = self.c.lastrowid
        return discipline_id
    def get_all_discipline(self):
        self.c.execute("SELECT * FROM disciplinas")
        dados = self.c.fetchall()
        return dados
    def update_discipline(self, novos_valores):
        self.c.execute("UPDATE disciplinas SET nome=?, periodo=? WHERE id=?", novos_valores)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Disciplina com ID:{novos_valores[2]} foi atualizado!')
    def delete_discipline(self, id):
        self.c.execute("DELETE FROM disciplinas WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Disciplina com ID:{id} foi excluida!')

disciplina_db = Disciplina()