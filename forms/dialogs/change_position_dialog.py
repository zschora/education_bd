from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from src.models import Teacher
from datetime import datetime


class ChangePositionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.teacher_code_label = QLabel('Teacher CODE:')
        self.teacher_code_edit = QLineEdit()

        self.new_position_label = QLabel('New Position:')
        self.new_position_edit = QLineEdit()

        self.change_button = QPushButton('Change Position')
        self.change_button.clicked.connect(self.accept)

        layout.addWidget(self.teacher_code_label)
        layout.addWidget(self.teacher_code_edit)

        layout.addWidget(self.new_position_label)
        layout.addWidget(self.new_position_edit)

        layout.addWidget(self.change_button)

        self.setLayout(layout)
        self.setWindowTitle('Change Position')

        style = QFile('forms\\styles\\form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

    def get_data(self):
        return {
            'teacher_code': int(self.teacher_code_edit.text()),
            'new_position': self.new_position_edit.text(),
        }
