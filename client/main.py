import sys
from PySide2 import QtWidgets
from gui.messenger import Messenger

app = QtWidgets.QApplication([])

widget = Messenger()

sys.exit(app.exec_())