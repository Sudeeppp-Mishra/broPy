import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Buttons")
        self.setGeometry(700, 300, 500, 500)
        
        self.label1 = QLabel("Payment Type:", self)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("Gift Card", self)
        
        self.buttongrp1 = QButtonGroup(self)
        
        self.label2 = QLabel("Payment Method", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        
        self.buttongrp2 = QButtonGroup(self)
        
        self.initUI()
        
    def initUI(self):
        self.label1.setGeometry(0, 0, 300, 100)
        self.radio1.setGeometry(0, 60, 300, 100)
        self.radio2.setGeometry(0, 120, 300, 100)
        self.radio3.setGeometry(0, 180, 300, 100)
        
        self.buttongrp1.addButton(self.radio1)
        self.buttongrp1.addButton(self.radio2)
        self.buttongrp1.addButton(self.radio3)
        
        
        self.label2.setGeometry(0, 300, 300, 100)
        self.radio4.setGeometry(0, 360, 300, 100)
        self.radio5.setGeometry(0, 420, 300, 100)
        
        self.buttongrp2.addButton(self.radio4)
        self.buttongrp2.addButton(self.radio5)
        
        self.setStyleSheet("QRadioButton{"
            "font-size: 40px;"
            "font-family: Times New Roman;"
            "padding: 10px;"
            "}"
            "QLabel{"
            "font-size: 40px;"
            "font-family: Times New Roman;"
            "padding: 10px;"
            "}")
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    def radio_button_changed(self):
        radio_button = self.sender() # which radio button sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected!")
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()