# Это программа на python показывает расписание на ближайший учебный день

def schedule():

    print("Введите настоящий день недели (в нижнем регистре)")
    day = input()

    bells = ["Урок безопасности: 8.25 - 8.40", "1 урок: 8.45 - 9.25", "2 урок: 9.35 - 10.15", "3 урок: 10.25 - 11.05", "4 урок: 11.15 - 11.55", "5 урок: 12.10 - 12.50", "6 урок: 13.05 - 13.45", "7 урок: 13.55 - 14.35", "8 урок: 14.45 - 15.25"]

    while 1:
        if day == "пятница" or day == "суббота" or day == "воскресенье":
            print("Ближайший учебный день недели - понедельник")
            print(" ")
            print("В понедельник 8 уроков")
            print(" ")
            monday = ["1 - Разговор о неважном", "2 - Английский язык", "3 - Химия", "4 - История", "5 - Математика", "6 - Русский язык", "7 - Статистика и вероятность", "8 - Физическая культура"]
            print("Расписание уроков на понедельник")
            print(" ")
            for i in monday:
                print(i)
            print(" ")
            print("Расписание звонков в понедельник")
            print(" ")
            for i in bells:
                print(i)
            break
        elif day == "понедельник":
            print("Ближайший учебный день недели - вторник")
            tuesday = ["1 - Информатика", "2 - Математика", "3 - Обществознание", "4 - Физика", "5 - Литература", "6 - Иностранный язык", "7 - Физическая культура"]
            print("Расписание уроков на вторник")
            for i in tuesday:
                print(i)
            print("Расписание звонков на вторник")
            print(" ")
            for i in bells:
                print(i)
            break
        elif day == "вторник":
            print("Ближайший учебный день недели - среда")
            print("Расписание уроков на среду")
            wednesday = ["1 - Русский язык", "2 - Обществознание", "3 - Информатика", "4 - Математика", "5 - Литература", "6 - Алгоритмика", "7 - Математика"]
            for i in wednesday:
                print(i)
            print("Расписание звонков на среду")
            print(" ")
            for i in bells:
                print(i)
            break
        elif day == "среда":
            print("Ближайший учебный день недели - четверг")
            thursday = ["1 - Россия - мои горизонты", "2 - География", "3 - Математика", "4 - Английский язык", "5 - История", "6 - Информатика", "7 - Физическая культура"]
            print("Расписание звонковна четверг")
            for i in bells:
                print(i)
            break
        elif day == "четверг":
            print("Ближайший учебный день недели - пятница")
            friday = ["1 - Математика", "2 - Литература", "3 - Информатика", "4 - ОБЗР", "5 - Биология", "6 - Математика", "7 - Физика"]
            for i in bells:
                print(i)
            break
        else:
            print("Сообщение не распознано, попробуйте снова")
            day = input()

schedule()
