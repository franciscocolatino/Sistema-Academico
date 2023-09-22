import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
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
    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Nome: {i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')
    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        print(f'ID: {dados[0]} | Nome: {dados[1]} | email: {dados[2]} | Tel: {dados[3]} | Sexo: {dados[4]} | Data de nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]}')
    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, novos_valores)
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', f'Estudante com ID:{novos_valores[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi excluido!')


# Instanciando a classe Sistema de registro

sistema_de_registro = SistemaDeRegistro()

#estudante = ('Elena', 'elena@gmail.com', '28247287', 'F', '01/05/2007', 'SP, Brasil', 'Medicina', 'imagem2.png')
#sistema_de_registro.register_student(estudante)

#sistema_de_registro.view_all_students()

# TRATAR O ERRO QUANDO ID INEXISTENTE
#aluno = sistema_de_registro.search_student(3)

#estudante = ('Elenaaaaaaaaa', 'elena@gmail.com', '28378179', 'F', '01/05/2007', 'SP, Brasil', 'Medicina2', 'imagem2.png', 2)
#aluno = sistema_de_registro.update_student(estudante)
#sistema_de_registro.search_student(2)

#sistema_de_registro.delete_student(2)
#sistema_de_registro.view_all_students()

