import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QFont # for fonts
from PyQt5.QtCore import Qt # for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel("Helloooooo", self) # self will represent the window object we created in main() and window will be a parent widget
        label.setFont(QFont("Courier New", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: grey;"
                            "background-color: #bfa19f;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # we can use just like CSS
        # label.setAlignment(Qt.AlignTop) # Vertically Top -> for Vertically bottom use Qt.AlignBottom, similarly AlignCenter
        # For Horizontal alignments use AlignRight, AlignHCenter, AlignLeft
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # combining both horizontal and vertical alignments -> CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        # label .setAlignment(AT.AlignCenter) # it also aligns CENTER & CENTER
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()