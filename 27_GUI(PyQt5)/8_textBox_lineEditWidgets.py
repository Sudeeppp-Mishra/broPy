# PyQt5 LineEdit

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        
        self.line_edit_txtBox = QLineEdit(self) # TextBox
        
        self.pushButton = QPushButton("Submit", self)
        
        self.initUI()
        
    def initUI(self):
        self.line_edit_txtBox.setGeometry(10, 10, 200, 40)
        self.line_edit_txtBox.setStyleSheet("font-size: 20px; font-family: Times New Roman;")
        self.line_edit_txtBox.setPlaceholderText("Enter your name")
        
        self.pushButton.setGeometry(10, 50, 200, 40)
        self.pushButton.setStyleSheet("font-size: 20px; font-family: Times New Roman;")
        self.pushButton.clicked.connect(self.submit)
                
    def submit(self):
        txt = self.line_edit_txtBox.text()
        self.setWindowTitle(f"Hello, {txt}")
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()