from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from src.models import Teacher
from datetime import datetime


class AddTeacherDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.code_label = QLabel('Code:')
        self.code_edit = QLineEdit()

        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()

        self.lastname_label = QLabel('Last Name:')
        self.lastname_edit = QLineEdit()

        self.birthday_label = QLabel('Birthday:')
        self.birthday_edit = QLineEdit()

        self.position_label = QLabel('Position:')
        self.position_edit = QLineEdit()

        self.degree_label = QLabel('Degree:')
        self.degree_combo = QComboBox()
        self.degree_combo.addItems(('PhD', 'MSc', 'BSc'))

        self.add_button = QPushButton('Add Teacher')
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.code_label)
        layout.addWidget(self.code_edit)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)

        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_edit)

        layout.addWidget(self.birthday_label)
        layout.addWidget(self.birthday_edit)

        layout.addWidget(self.position_label)
        layout.addWidget(self.position_edit)

        layout.addWidget(self.degree_label)
        layout.addWidget(self.degree_combo)

        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('Add Teacher')

    def get_teacher_data(self):
        return {
            'code': int(self.code_edit.text()),
            'name': self.name_edit.text(),
            'lastname': self.lastname_edit.text(),
            'birthday': datetime.strptime(self.birthday_edit.text(), "%Y-%m-%d").date(),
            'position': self.position_edit.text(),
            'degree': self.degree_edit.text(),
        }
