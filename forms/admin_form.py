import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class AdminForm(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.info_label = QLabel('Админ-панель')
        self.info_label.setAlignment(Qt.AlignCenter)

        self.create_connect_button = QPushButton('Создать/Подключиться к БД')
        self.create_connect_button.clicked.connect(self.create_connect_db)

        layout.addWidget(self.info_label, alignment=Qt.AlignRight)
        layout.addWidget(self.create_connect_button, alignment=Qt.AlignRight)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle('Админ-панель')

    def create_connect_db(self):
        # Здесь вы можете добавить код для создания или подключения к базе данных
        print('Создание/Подключение к БД...')

