import sys
from client.db.db_connector import DB
from PySide2 import QtWidgets
from gui.auth import Auth
from gui.messenger import Messenger
app = QtWidgets.QApplication([])

db = DB()
token = db.get_token()

widget = Auth()

if token:
    widget = Messenger()

widget.show()

sys.exit(app.exec_())