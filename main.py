import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

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
        password = self.password_input.text()

        # Тут можешь добавить проверку введенных данных и переход к другому окну

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    sys.exit(app.exec_())
