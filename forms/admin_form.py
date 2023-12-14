import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QFile, QTextStream, Qt
from src.database_manager import DatabaseManager


class AdminForm(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()
        print('Создание/Подключение к БД...')
        self.db_manager = DatabaseManager()

    def init_ui(self):
        layout = QVBoxLayout()

        self.random_fill_button = QPushButton('Заполнить рандомно бд')
        self.random_fill_button.clicked.connect(self.random_fill)

        layout.addWidget(self.random_fill_button, alignment=Qt.AlignRight)
        layout.setAlignment(Qt.AlignCenter)

        self.print_teachers_button = QPushButton('Вывести учителей')
        self.print_teachers_button.clicked.connect(self.print_teachers)

        layout.addWidget(self.print_teachers_button, alignment=Qt.AlignRight)

        self.add_teacher_button = QPushButton('Добавить учителя')
        self.add_teacher_button.clicked.connect(self.add_teacher)

        layout.addWidget(self.add_teacher_button, alignment=Qt.AlignRight)

        self.print_subjects_button = QPushButton('Вывести предметы')
        self.print_subjects_button.clicked.connect(self.print_subjects)

        layout.addWidget(self.print_subjects_button, alignment=Qt.AlignRight)

        self.add_subject_button = QPushButton('Добавить предмет')
        self.add_subject_button.clicked.connect(self.add_subject)

        layout.addWidget(self.add_subject_button, alignment=Qt.AlignRight)

        self.print_majors_button = QPushButton('Вывести направления')
        self.print_majors_button.clicked.connect(self.print_majors)

        layout.addWidget(self.print_majors_button, alignment=Qt.AlignRight)

        self.add_major_button = QPushButton('Добавить направление')
        self.add_major_button.clicked.connect(self.add_major)

        layout.addWidget(self.add_major_button, alignment=Qt.AlignRight)

        self.setLayout(layout)
        self.setWindowTitle('Админ-панель')
        self.setGeometry(300, 300, 400, 200)  # размеры окна

        style = QFile('forms\\styles\\admin_form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

    def random_fill(self):
        self.db_manager.add_random_data()

    def print_teachers(self):
        teachers = self.db_manager.get_teachers()
        for teacher in teachers:
            print(teacher)

    def print_subjects(self):
        subjects = self.db_manager.get_subjects()
        for subject in subjects:
            print(subject)

    def print_majors(self):
        majors = self.db_manager.get_majors()
        for major in majors:
            print(major)

    def add_teacher(self):
        pass

    def add_subject(self):
        pass

    def add_major(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_form = AdminForm(app)
    admin_form.show()
    sys.exit(app.exec_())
