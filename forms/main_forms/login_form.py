from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal, QFile, QTextStream
import bcrypt

admin_pswd = "$2b$12$UYjTYM29BBEUt3iDekI5kOR9PQTnhbd6ZHe2NmPbtmKs5wf6SxPB."
user_pswd = "$2b$12$xEzieiJijrAiSSzez0pmbuYmSLplTcgWomRly5FL/vOwVSIU5YL6u"

class LoginForm(QWidget):
    show_admin_form = pyqtSignal()
    show_user_form = pyqtSignal()

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

        style = QFile('forms\\styles\\form.css')  # стили формы
        if style.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style)
            self.setStyleSheet(stream.readAll())

        self.setGeometry(300, 300, 400, 200)  # размеры окна
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
                self.show_user_form.emit()
                self.hide()

