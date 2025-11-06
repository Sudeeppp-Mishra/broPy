# Python PyQt5 Stopwatch

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0) # hr, min, sec, ms
        self.time_label = QLabel("00:00:00:00", self)
        
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           QPushButton, QLabel{
                               padding: 20px;
                               margin: 10px;
                               font-family: Times New Roman;
                               font-weight: bold;
                           }
                           
                           QPushButton{
                               background-color: lightgrey;
                               font-size: 20px;
                           }
                           
                           QLabel{
                               font-size: 40px;
                               background-color: lightgreen;
                           }
                           """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
    
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
    
    def format_time(self, time):
        hrs = time.hour()
        mins = time.minute()
        sec = time.second()
        ms = time.msec() // 10 # 3 digits to 2
        
        return f"{hrs:02}:{mins:02}:{sec:02}.{ms:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
                
if __name__=="__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    
    stopwatch.show()
    sys.exit(app.exec_())