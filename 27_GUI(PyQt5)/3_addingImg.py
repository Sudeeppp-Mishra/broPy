import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adding Image")
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 200, 200)
        
        pixmap_obj = QPixmap("img/test.jpg")
        label.setPixmap(pixmap_obj)
        
        label.setScaledContents(True) # image will now scale to size of label 
        
        label.setGeometry((self.width() - label.width()) // 2, # divide by 2 for centering
                           (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()