from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from src.models import Teacher
from datetime import datetime


class AddAssociationTeacherSubjectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.scode_label = QLabel('Subject code:')
        self.scode_edit = QLineEdit()

        self.tcode_label = QLabel('Teacher code:')
        self.tcode_edit = QLineEdit()

        self.add_button = QPushButton('Связать')
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.scode_label)
        layout.addWidget(self.scode_edit)

        layout.addWidget(self.tcode_label)
        layout.addWidget(self.tcode_edit)

        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('Add Association')

    def get_data(self):
        return {
            'teacher_code': int(self.tcode_edit.text()),
            'subject_code': int(self.scode_edit.text())
        }
