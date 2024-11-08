import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(500, 300, 350, 250)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c2f33;
                color: #ffffff;
                border-radius: 10px;
            }
            QLabel {
                font-size: 12pt;
                color: #ffffff;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #424549;
                border-radius: 5px;
                background-color: #1e2227;
                color: #ffffff;
            }
            QPushButton {
                padding: 10px;
                border-radius: 5px;
                background-color: #7289da;
                color: #ffffff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5b6ea5;
            }
            QPushButton:pressed {
                background-color: #4b5b85;
            }
        """)

        # Username Label and Input Field
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        # Password Label and Input Field
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Success", "Welcome!")
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")

# Main Application Start
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
