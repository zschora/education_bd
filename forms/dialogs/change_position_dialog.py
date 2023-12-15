from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from src.models import Teacher
from datetime import datetime


class AddAssociationMajorSubjectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.scode_label = QLabel('Subject code:')
        self.scode_edit = QLineEdit()

        self.mcode_label = QLabel('Major code:')
        self.mcode_edit = QLineEdit()

        self.add_button = QPushButton('Связать')
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.scode_label)
        layout.addWidget(self.scode_edit)

        layout.addWidget(self.mcode_label)
        layout.addWidget(self.mcode_edit)

        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('Add Association')

    def get_data(self):
        return {
            'major_code': int(self.mcode_edit.text()),
            'subject_code': int(self.scode_edit.text())
        }
