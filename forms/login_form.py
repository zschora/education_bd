from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal
import bcrypt
from forms.admin_form import AdminForm

admin_pswd = "$2b$12$UYjTYM29BBEUt3iDekI5kOR9PQTnhbd6ZHe2NmPbtmKs5wf6SxPB."
user_pswd = "$2b$12$xEzieiJijrAiSSzez0pmbuYmSLplTcgWomRly5FL/vOwVSIU5YL6u"

class LoginForm(QWidget):
    # Создаем сигнал как классовый атрибут
    show_admin_form = pyqtSignal()

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        hbox_username = QHBoxLayout()
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        hbox_username.addWidget(self.username_label, alignment=Qt.AlignRight)
        hbox_username.addWidget(self.username_input, alignment=Qt.AlignLeft)

        hbox_password = QHBoxLayout()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        hbox_password.addWidget(self.password_label, alignment=Qt.AlignRight)
        hbox_password.addWidget(self.password_input, alignment=Qt.AlignLeft)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        layout.addLayout(hbox_username)
        layout.addLayout(hbox_password)
        layout.addWidget(self.login_button)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle('Login Form')

        # Устанавливаем фоновый цвет
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5dc;
            }

            QLabel {
                color: #964B00;
                font-size: 18px;
            }

            QLineEdit {
                padding: 8px;
                font-size: 16px;
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #964B00;
                color: #ffffff;
                font-size: 18px;
                border: none;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #7B3F00;
            }
            QPushButton:pressed {
                background-color: #522C00;  
            }

        """)

        self.setGeometry(300, 300, 400, 200)  # Задаем размеры окна
        self.show()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text().encode('utf-8')

        if username == 'admin':
            if bcrypt.checkpw(password, admin_pswd.encode('utf-8')):
                print('OK')
                self.show_admin_form.emit()
                self.hide()
        if username == 'user':
            if bcrypt.checkpw(password, user_pswd.encode('utf-8')):
                print('OK')

