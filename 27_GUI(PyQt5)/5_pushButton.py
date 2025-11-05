import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("CLICK HERE", self) # the self means the window so we are adding to window
        # it is better practice to initialize things here and do the UI work in next function
        
        self.label = QLabel("Hello", self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150, 150, 200, 100)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_click) # when clicked we connect it to some event "clicked" is a signal(or event) and "self.on_click" is a slot where we are connecting
        
        self.label.setGeometry(250, 250, 100, 200)
        self.label.setStyleSheet("font-size:20px;")
        
    def on_click(self):
        # print("Button Clicked!")
        # self.button.setText("CLICKED")
        # self.button.setDisabled(True)
        
        self.label.setText("GoodBye!")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()