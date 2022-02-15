import sys
from PySide2 import QtWidgets
from client.gui.ui import messenger_ui
from client.grpc import client_grpc
from client.gui.auth import Auth
from client.db.db_connector import db


class Messenger(QtWidgets.QMainWindow, messenger_ui.Ui_MainWindow):
    def __init__(self):
        super(Messenger, self).__init__()
        self.setupUi(self)
        self.auth_window = Auth()
        self.auth_window.auth_signal.connect(self.auth_completed)
        self.token = db.get_token()
        self.show()
        if not self.token:
            self.auth_window.show()

    def auth_completed(self, token: str):
        self.token = token


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Messenger()

    sys.exit(app.exec_())