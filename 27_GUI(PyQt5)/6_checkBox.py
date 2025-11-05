import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
# Qt import explanation:
# ----------------------
# The 'Qt' class from 'PyQt5.QtCore' provides a collection of built-in constants
# and enumerations that are widely used throughout PyQt.
# These constants define things like alignment, orientation, widget states,
# and other UI behaviors.
#
# Examples:
#   Qt.AlignCenter   → used to center-align layouts or widgets
#   Qt.Checked       → represents a checked state for checkboxes
#   Qt.Horizontal    → used for specifying horizontal orientation
#
# In this program, we import 'Qt' to easily access constants like 'Qt.AlignCenter'
# for setting layout alignment, instead of writing the longer form
# 'PyQt5.QtCore.Qt.AlignCenter'.
#
# So, 'from PyQt5.QtCore import Qt' keeps the code cleaner and more readable.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("CHECK BOX")

        self.checkBox1 = QCheckBox("Do You Love Me?? HEHE ;)")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.checkBox1)
        vbox.setAlignment(Qt.AlignCenter)
        vbox.setContentsMargins(50, 200, 50, 200)
        
        self.checkBox1.setStyleSheet("""
            QCheckBox {
                font-size: 28px;
                color: #555;
            }
            QCheckBox::indicator {
                width: 25px;
                height: 25px;
            }
        """)
        
        self.checkBox1.stateChanged.connect(self.on_checkbox_toggled) # the on_checkbox_toggled gets a parameter state automatically by Qt which is int variable

        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def on_checkbox_toggled(self, state):
        if state: # or we can check condition like state == Qt.Checked
            self.setWindowTitle("Awww, you do! <3")
        else:
            self.setWindowTitle("Oh... okay ToT")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()