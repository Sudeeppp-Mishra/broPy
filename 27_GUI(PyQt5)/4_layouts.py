# PyQt5 layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        
    def initUI(self): # for better organization we are using this function
        central_widget = QWidget() # generic widget then we will add layout to it then finally we will add this widget to main-window
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: purple;")
        label5.setStyleSheet("background-color: yellow;")
        
        # vbox = QVBoxLayout() # For horizontal just call the QHBoxLayout() constructor
        
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        
        # central_widget.setLayout(vbox)
        
        grid = QGridLayout()
        
        grid.addWidget(label1, 0, 0) # (x, y) grid are passed
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)
        
        central_widget.setLayout(grid)
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()