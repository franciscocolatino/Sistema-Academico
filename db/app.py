from db.Curso import *
from db.CursoDisciplina import *
from db.Disciplina import *

cursos_db = Curso()
# curso1 = cursos_db.create_course("Ciencia da computação")
# curso2 = cursos_db.create_course("Medicina")

disciplina_db = Disciplina()
# disciplina1 = disciplina.create_disciplina(['APC', 1])
# disciplina2 = disciplina.create_disciplina(['POO', 3])
# disciplina3 = disciplina.create_disciplina(['ANATOMIA 1', 1])
# disciplina4 = disciplina.create_disciplina(['ANATOMIA 2', 2])
# disciplina5 = disciplina.create_disciplina(['ENGENHARIA DE SOFTWARE', 5])

cursoDisciplina_db = CursoDisciplina()
# cursoDisciplina.create_course_disciplina([1, 1])
# cursoDisciplina.create_course_disciplina([1, 2])
# cursoDisciplina.create_course_disciplina([2, 3])
# cursoDisciplina.create_course_disciplina([2, 4])
# cursoDisciplina.create_course_disciplina([1, 5])
# cursoDisciplina.get_all_courses_disciplinas()
cursoDisciplina_db.get_all_disciplines_one_course(1)
# cursos_db.check_course_exists('Ciencia da computação')
