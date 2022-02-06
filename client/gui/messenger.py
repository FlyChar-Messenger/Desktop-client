from PySide2 import QtWidgets
from client.gui.ui import first_ui
from client.grpc import client_grpc


class Messenger(QtWidgets.QMainWindow, first_ui.Ui_MainWindow):
    def __init__(self):
        super(Messenger, self).__init__()
        self.setupUi(self)
