import sqlite3
from tkinter import messagebox

class CursoDisciplina:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS cursos_disciplinas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            curso_id INTEGER NOT NULL,
                            disciplina_id INTEGER NOT NULL,
                            FOREIGN KEY (curso_id) REFERENCES cursos (id),
                            FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id)
                            );''')
    def create_course_disciplina(self, curso_disciplina):
        self.c.execute("INSERT INTO cursos_disciplinas (curso_id, disciplina_id) VALUES (?, ?)", (curso_disciplina))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Curso relacionado com disciplina com sucesso')
    def get_all_courses_disciplinas(self):
        self.c.execute("SELECT cursos_disciplinas.id,cursos.nome AS curso, disciplinas.nome AS disciplina, disciplinas.periodo FROM cursos_disciplinas \
                    JOIN cursos ON cursos.id = cursos_disciplinas.curso_id \
                    JOIN disciplinas ON disciplinas.id = cursos_disciplinas.disciplina_id")
        dados = self.c.fetchall()
        return dados
    def get_all_disciplines_one_course(self, course_id):
        self.c.execute("SELECT disciplinas.nome FROM cursos_disciplinas \
                    JOIN disciplinas ON cursos_disciplinas.disciplina_id = disciplinas.id \
                    WHERE cursos_disciplinas.curso_id = ?", (course_id,))
        dados = self.c.fetchall()
        return dados
    def get_discipline_with_course(self, courseDisciplineId):
        self.c.execute("SELECT cursos_disciplinas.id, cursos.nome, disciplinas.nome, disciplinas.periodo "
                   "FROM cursos_disciplinas "
                   "JOIN cursos ON cursos.id = cursos_disciplinas.curso_id "
                   "JOIN disciplinas ON disciplinas.id = cursos_disciplinas.disciplina_id " 
                   "WHERE cursos_disciplinas.id=?", (courseDisciplineId,))
        dados = self.c.fetchone()
        return dados
    def count_discipline_has_one_course(self, course_id):
        self.c.execute("SELECT COUNT(*) FROM cursos_disciplinas WHERE curso_id=?", (course_id,))
        dados = self.c.fetchone()
        return dados[0]
    def get_discipline_id(self, courseDisciplineId):
        self.c.execute("SELECT disciplina_id FROM cursos_disciplinas WHERE id=?", (courseDisciplineId,))
        dados = self.c.fetchone()
        return dados
    def delete_course_discipline(self, id):
        self.c.execute("DELETE FROM cursos_disciplinas WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Relacionamento de cursos com disciplinas com ID:{id} foi excluido!')
    def update_course_discipline(self, novos_valores):
        self.c.execute("UPDATE cursos_disciplinas SET curso_id=?, disciplina_id=? WHERE id=?", novos_valores)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Relacionamento de cursos com disciplinas com ID:{novos_valores[2]} foi atualizado!')

CursoDisciplina_db = CursoDisciplina()