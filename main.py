from PyQt5.QtWidgets import QApplication
from forms.main_forms.login_form import LoginForm
from forms.main_forms.admin_form import AdminForm
from forms.main_forms.user_form import UserForm

if __name__ == '__main__':
    app = QApplication([])
    login_form = LoginForm(app)
    admin_form = AdminForm(app)
    user_form = UserForm(app)

    # Подключаем сигналы из LoginForm к слотам в AdminForm, UserForm
    login_form.show_admin_form.connect(admin_form.show)
    login_form.show_user_form.connect(user_form.show)

    login_form.show()
    #admin_form.show()
    #user_form.show()
    app.exec_()
