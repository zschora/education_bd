import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QDialog
from PyQt5.QtCore import QFile, QTextStream, Qt
from src.database_manager import DatabaseManager
from forms.dialogs.add_teacher_dialog import AddTeacherDialog
from forms.dialogs.add_subject_dialog import AddSubjectDialog
from forms.dialogs.add_major_dialog import AddMajorDialog
from forms.dialogs.output import OutputDialog
from forms.dialogs.add_ass_ts_dialog import AddAssociationTeacherSubjectDialog
from forms.dialogs.add_ass_ms_dialog import AddAssociationMajorSubjectDialog
from src.models import Teacher, Subject, Major, AssociationMajorSubject, AssociationTeacherSubject


class AdminForm(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()
        print('Создание/Подключение к БД...')
        self.db_manager = DatabaseManager()

    def init_ui(self):
        main_layout = QHBoxLayout()

        options_layout = QVBoxLayout()
        options_layout.setAlignment(Qt.AlignTop)

        self.print_teachers_button = QPushButton('Вывести учителей')
        self.print_teachers_button.clicked.connect(self.print_teachers)
        options_layout.addWidget(self.print_teachers_button)

        self.print_subjects_button = QPushButton('Вывести предметы')
        self.print_subjects_button.clicked.connect(self.print_subjects)
        options_layout.addWidget(self.print_subjects_button)

        self.print_majors_button = QPushButton('Вывести направления')
        self.print_majors_button.clicked.connect(self.print_majors)
        options_layout.addWidget(self.print_majors_button)

        main_layout.addLayout(options_layout)

        modify_layout = QVBoxLayout()
        modify_layout.setAlignment(Qt.AlignTop)

        self.random_fill_button = QPushButton('Заполнить рандомно бд')
        self.random_fill_button.clicked.connect(self.random_fill)
        modify_layout.addWidget(self.random_fill_button)

        self.add_teacher_button = QPushButton('Добавить учителя')
        self.add_teacher_button.clicked.connect(self.add_teacher)
        modify_layout.addWidget(self.add_teacher_button)

        self.add_subject_button = QPushButton('Добавить предмет')
        self.add_subject_button.clicked.connect(self.add_subject)
        modify_layout.addWidget(self.add_subject_button)

        self.add_major_button = QPushButton('Добавить направление')
        self.add_major_button.clicked.connect(self.add_major)
        modify_layout.addWidget(self.add_major_button)

        self.add_ass_ts_button = QPushButton('Связать учителя и предмет')
        self.add_ass_ts_button.clicked.connect(self.add_association_teacher_subject)
        modify_layout.addWidget(self.add_ass_ts_button)

        self.add_ass_ms_button = QPushButton('Связать направление и предмет')
        self.add_ass_ms_button.clicked.connect(self.add_association_major_subject)
        modify_layout.addWidget(self.add_ass_ms_button)

        main_layout.addLayout(modify_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Админ-панель')
        self.setGeometry(300, 300, 400, 200)  # размеры окна

        style = QFile('forms\\styles\\form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

    def random_fill(self):
        self.db_manager.add_random_data()

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

    def add_teacher(self):
        dialog = AddTeacherDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            teacher_data = dialog.get_teacher_data()
            self.db_manager.add_teacher(**teacher_data)
            print(f"Teacher added: {Teacher(**teacher_data)}")

    def add_subject(self):
        dialog = AddSubjectDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            subject_data = dialog.get_subject_data()
            self.db_manager.add_subject(**subject_data)
            print(f"Subject added: {Subject(**subject_data)}")

    def add_major(self):
        dialog = AddMajorDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            major_data = dialog.get_major_data()
            self.db_manager.add_major(**major_data)
            print(f"Major added: {Major(**major_data)}")

    def add_association_teacher_subject(self):
        dialog = AddAssociationTeacherSubjectDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            data = dialog.get_data()
            self.db_manager.add_association_teacher_subject(**data)
            print(f"Association added: Teacher{data['teacher_code']}->Subject{data['subject_code']}")

    def add_association_major_subject(self):
        dialog = AddAssociationMajorSubjectDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            data = dialog.get_data()
            self.db_manager.add_association_major_subject(**data)
            print(f"Association added: Major{data['major_code']}->Subject{data['subject_code']}")
