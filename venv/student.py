class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}  # Словарь для хранения оценок {предмет: [оценки]}

    def add_grade(self, subject, grade):
        # Метод для добавления оценки за предмет
        pass

    def get_subjects(self):
        # Метод для получения списка предметов
        pass

    def get_average_grade(self, subject=None):
        # Метод для получения средней оценки
        pass