import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")
        self.setGeometry(500, 300, 350, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c2f33;
                color: #ffffff;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14pt;
                color: #ffffff;
                margin-bottom: 20px;
            }
            QPushButton {
                padding: 12px;
                border-radius: 5px;
                background-color: #7289da;
                color: #ffffff;
                font-weight: bold;
                font-size: 12pt;
                margin: 5px 0;
            }
            QPushButton:hover {
                background-color: #5b6ea5;
            }
            QPushButton:pressed {
                background-color: #4b5b85;
            }
        """)

        # Title Label
        self.title_label = QLabel("Main Menu")
        self.title_label.setAlignment(Qt.AlignCenter)

        # Menu Buttons
        self.button1 = QPushButton("Option 1")
        self.button2 = QPushButton("Option 2")
        self.button3 = QPushButton("Option 3")
        self.button4 = QPushButton("Logout")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())
