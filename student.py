class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}  # Словарь для хранения оценок {предмет: [оценки]}

    def add_grade(self, subject, grade):
        if subject in self.grades.keys() :
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def get_subjects(self):
        print(self.grades)
    def get_average_grade(self, subject):
        sum = 0
        sub_grades = self.grades[subject]
        for i in range(len(sub_grades)):
            sum += sub_grades[i]
        print(subject, sum/len(sub_grades))


    def get_all_average_grade(self):
        for k in self.grades.keys():
            sum = 0
            sub_grades = self.grades[k]
            for i in range(len(sub_grades)):
                sum += sub_grades[i]
            print(k, sum / len(sub_grades))


def show_moves(moves): #показывает список комманд
    print("-" * 20)
    for k, v in moves.items():
        print(f"{k}. {v}")
    print("-" * 20)


if __name__ == "__main__":
    Name = input("Введите имя студента: ")
    Age = int(input("Введите возраст студента: "))
    loh = Student(Name, Age)
    moves = {
        1: "Добавление оценки за определенный предмет.",
        2: "Получение списка всех предметов, по которым есть оценки у студента.",
        3: "Получение средней оценки по определенному предмету.",
        4: "Получение средней оценки по всем предметам.",
        5: "Показать список команд ещё раз",
        6: "Выйти"
    }
    show_moves(moves)
    while True:
        a = int(input("Введите номер пункта, в который хотите перейти: "))
        while a not in moves.keys():
            a = int(input("Такой команды не существует, попробуйте ещё раз: "))
        if a == 1:
            Sub = input("Введите название предмета: ")
            Grade = int(input("Введите оценку: "))
            loh.add_grade(Sub, Grade)
        if a == 2:
            loh.get_subjects()
        if a == 3:
            Sub = input("Введите название предмета: ")
            loh.get_average_grade(Sub)
        if a == 4:
            loh.get_all_average_grade()
        if a == 5:
            show_moves(moves)
        if a == 6:
            print("Программа завершена!")
            break
