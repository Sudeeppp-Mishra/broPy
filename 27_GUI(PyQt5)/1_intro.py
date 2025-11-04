# PyQt5 Introduction

import sys # This module provides access to some variables used to maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon # for Window ICON
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WINDOW")
        self.setGeometry(0, 0, 500, 500) # setGeometry(x, y, width, height) -> (x,y) is the co-ordinate where the window's intial placement will be
        self.setWindowIcon(QIcon("img/test.jpg"))
        
def main():
    app = QApplication(sys.argv)
    # sys.argv -> it allows PyQt to process any command line arguments intended for it
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()