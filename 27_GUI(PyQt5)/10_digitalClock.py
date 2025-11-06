import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget): # QWidget is base class and we are going to make the digital clock as our own widget now a window
    def __init__(self):
        super().__init__()
        
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(700, 300, 400, 150)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 100px;
            color: hsl(181, 4%, 81%);
        """)
        self.setStyleSheet("background-color: black;")

        # Try loading custom font
        # Build the full path to the font file based on the script's location 
        # (so it works even if you run this program from a different folder)
        font_path = os.path.join(os.path.dirname(__file__), "fonts/DS-DIGIB.TTF")
        font_id = QFontDatabase.addApplicationFont(font_path)
        families = QFontDatabase.applicationFontFamilies(font_id)
        
        if families:
            font_family = families[0] # we will need 1st index of font family
            print(f"✅ Loaded custom font: {font_family}")
        else:
            font_family = "Times New Roman"
            print("⚠️ Font not found — using Times New Roman")

        self.time_label.setFont(QFont(font_family, 100))

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # sends signal every second so that update_time() is called every second
        self.update_time() # we are manually calling it so that at first as well it will show the time if we don't call this manually then only after a second the window will so the time else it will be empty for a second
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # AP after format specifier adds am or pm (AP - Anti-meridian and Post-meridian)
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
