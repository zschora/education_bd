import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QFile, QTextStream, Qt
from src.database_manager import DatabaseManager


class UserForm(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()
        print('Создание/Подключение к БД...')
        self.db_manager = DatabaseManager()

    def init_ui(self):
        layout = QVBoxLayout()

        self.print_teachers_button = QPushButton('Вывести учителей')
        self.print_teachers_button.clicked.connect(self.print_teachers)
        layout.addWidget(self.print_teachers_button, alignment=Qt.AlignRight)

        self.print_subjects_button = QPushButton('Вывести предметы')
        self.print_subjects_button.clicked.connect(self.print_subjects)
        layout.addWidget(self.print_subjects_button, alignment=Qt.AlignRight)

        self.print_majors_button = QPushButton('Вывести направления')
        self.print_majors_button.clicked.connect(self.print_majors)
        layout.addWidget(self.print_majors_button, alignment=Qt.AlignRight)

        self.setLayout(layout)
        self.setWindowTitle('Пользователь-панель')
        self.setGeometry(300, 300, 400, 200)  # размеры окна

        style = QFile('forms\\styles\\user_form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

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
