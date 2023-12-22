import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtCore import Qt

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bryan + Matt's Game")
        self.setGeometry(200, 200, 800, 800)  # Set your desired window size

        # Set up the background image for the central widget
        self.background_image_path = "splash.jpg"  # Change to your image path
        self.set_background_image()

        # Create title label
        title_label = QLabel("Wala pay final title", self)
        self.set_title_style(title_label)

        # Create buttons
        button1 = QPushButton('Start', self)
        button1.clicked.connect(self.start)
        button2 = QPushButton('How to Play', self)
        button2.clicked.connect(self.instructions)

        # Set button styles
        self.set_button_style(button1)
        self.set_button_style(button2)

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(title_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        layout.addStretch()  # Add flexible space to push buttons to the bottom
        layout.addWidget(button1, alignment=Qt.AlignCenter)
        layout.addWidget(button2, alignment=Qt.AlignCenter)

        self.show()

    def set_background_image(self):
        pixmap = QPixmap(self.background_image_path)
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QBrush(pixmap))
        self.setPalette(palette)

    def set_title_style(self, label):
        label.setStyleSheet("font-size: 80px; color: white;")

    def set_button_style(self, button):
        button.setMinimumSize(300, 80)
        button.setStyleSheet("font-size: 20px; background-color: #d4d4d4; border: 4px solid black; border-radius: 20px;")
    
    def start(self):
        print("Game starting...")
    
    def instructions(self):
        QMessageBox.information(self, 'How to Play', 'Use the W, A, S, D keys to move the character. Right-click to SPRINT, Left-click to ATTACK.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonApp()
    sys.exit(app.exec_())

