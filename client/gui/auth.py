import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from client.gui.ui import auth_ui
from client.grpc import client_grpc
from client.db.db_connector import db


class Auth(QtWidgets.QMainWindow, auth_ui.Ui_MainWindow):
    auth_signal = Signal(str)

    def __init__(self):
        super(Auth, self).__init__()
        self.setupUi(self)
        self.auth_button.clicked.connect(self.auth_action)
        self.client = client_grpc.Client()
        self.regestation_buttion.clicked.connect(self.reg_action)

    def auth_action(self):
        login = self.login_text_filed.text()
        password = self.pass_text_filed.text()
        token = self.client.auth(login, password)
        db.update_user_data(token, login, password)
        self.auth_signal.emit(token)
        self.close()

    def reg_action(self):
        login = self.login_text_filed.text()
        password = self.pass_text_filed.text()
        token = self.client.register(login, password)
        db.update_user_data(token, login, password)
        self.auth_signal.emit(token)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Auth()
    widget.show()

    sys.exit(app.exec_())
