from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from src.models import Teacher
from datetime import datetime


class AddSubjectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.code_label = QLabel('Code:')
        self.code_edit = QLineEdit()

        self.title_label = QLabel('Title:')
        self.title_edit = QLineEdit()

        self.hours_label = QLabel('Hours:')
        self.hours_edit = QLineEdit()

        self.add_button = QPushButton('Add Subject')
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.code_label)
        layout.addWidget(self.code_edit)

        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)

        layout.addWidget(self.hours_label)
        layout.addWidget(self.hours_edit)


        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('Add Subject')

    def get_subject_data(self):
        return {
            'code': int(self.code_edit.text()),
            'title': self.title_edit.text(),
            'hours': int(self.hours_edit.text())
        }
