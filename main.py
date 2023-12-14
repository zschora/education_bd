from PyQt5.QtWidgets import QApplication
from forms.login_form import LoginForm
from forms.admin_form import AdminForm

if __name__ == '__main__':
    app = QApplication([])
    login_form = LoginForm(app)
    admin_form = AdminForm(app)

    # Подключаем сигнал из LoginForm к слоту в AdminForm
    login_form.show_admin_form.connect(admin_form.show)

    login_form.show()
    app.exec_()
