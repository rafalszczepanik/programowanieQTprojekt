import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainmenu import FirstSite


class MyMainWindow(QMainWindow, FirstSite):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
