import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QLineEdit
from PyQt5.QtCore import QFile, QTextStream, Qt

from forms.dialogs.output import OutputDialog
from src.database_manager import DatabaseManager
from forms.dialogs.change_position_dialog import ChangePositionDialog
from src.models import Teacher


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

        self.change_position_button = QPushButton('Изменить должность')
        self.change_position_button.clicked.connect(self.change_teacher_position)
        layout.addWidget(self.change_position_button, alignment=Qt.AlignRight)

        self.qq = QPushButton('Запрос')
        self.qq.clicked.connect(self.query)
        layout.addWidget(self.qq, alignment=Qt.AlignRight)

        self.year_label = QLabel('Birth year:')
        self.year_edit = QLineEdit()
        layout.addWidget(self.year_label, alignment=Qt.AlignRight)
        layout.addWidget(self.year_edit, alignment=Qt.AlignRight)



        self.setLayout(layout)
        self.setWindowTitle('Пользователь-панель')
        self.setGeometry(300, 300, 400, 200)  # размеры окна

        style = QFile('forms\\styles\\form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

    def print_teachers(self):
        teachers = self.db_manager.get_teachers()
        output_dialog = OutputDialog('Teachers', teachers)
        output_dialog.exec_()

    def print_subjects(self):
        subjects = self.db_manager.get_subjects()
        output_dialog = OutputDialog('Subjects', subjects)
        output_dialog.exec_()

    def print_majors(self):
        majors = self.db_manager.get_majors()
        output_dialog = OutputDialog('Majors', majors)
        output_dialog.exec_()

    def change_teacher_position(self):
        dialog = ChangePositionDialog()
        result = dialog.exec_()

        if result == QDialog.Accepted:
            data = dialog.get_data()
            self.db_manager.change_teacher_position(**data)

    def query(self):
        res = self.db_manager.get_courses_by_birth_year(int(self.year_edit.text()))
        output_dialog = OutputDialog('Result', res)
        output_dialog.exec_()


