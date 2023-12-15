from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QFile, QTextStream


class OutputDialog(QDialog):
    def __init__(self, title, data):
        super().__init__()

        layout = QVBoxLayout()

        for unit in data:
            label = QLabel(str(unit))
            layout.addWidget(label)

        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)
        self.setWindowTitle(title)

        style = QFile('forms\\styles\\admin_form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())
