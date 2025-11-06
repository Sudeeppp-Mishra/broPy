# PyQt5 setStyleSheet()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.btn1 = QPushButton("#1") # since we are using a Layout we don't need to add it to the window by passing self here
        self.btn2 = QPushButton("#2")
        self.btn3 = QPushButton("#3")
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        
        central_widget.setLayout(hbox)
        
        self.btn1.setObjectName("btn1") # if we want to apply style sheet to all buttons differently we need to set object name for them
        self.btn2.setObjectName("btn2") # if we want to apply style sheet to all buttons differently we need to set object name for them
        self.btn3.setObjectName("btn3") 
        
        self.setStyleSheet("""
                           QPushButton{
                               font-size: 20px;
                               font-family: Times New Roman;
                               font-style: bold;
                               padding: 15px 75px;
                               margin: 25px;
                               border: 3px solid;
                           }
                           
                           QPushButton#btn1{
                               background-color: hsl(0, 82%, 26%);
                           }
                           QPushButton#btn2{
                               background-color: hsl(146, 78%, 23%);
                           }
                           QPushButton#btn3{
                               background-color: hsl(181, 72%, 27%);
                           }
                           
                           QPushButton#btn1:hover{
                               background-color: hsl(0, 82%, 66%);
                           }
                           QPushButton#btn2:hover{
                               background-color: hsl(146, 78%, 73%);
                           }
                           QPushButton#btn3:hover{
                               background-color: hsl(181, 72%, 67%);
                           }
                           """)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()