'''import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QVBoxLayout, QFrame, QLabel, QMessageBox, QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()

        # Set up background image
        self.background_image_path = "splash.jpg"  # Change to your image path
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Antier and Delfin Game')
        self.setGeometry(200, 200, 800, 800)  # Set your desired window size

        # Set up main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set zero margins
        main_layout.setSpacing(0)  # Set zero spacing

        # Background image
        background_label = QLabel(self)
        self.set_background_image(background_label)

        # Container widget for buttons
        buttons_container = QFrame(self)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout(buttons_container)
        button_layout.setContentsMargins(0, 200, 50, 50)

        # How to Play button
        how_to_play_button = QPushButton('How to Play', buttons_container)
        self.set_button_style(how_to_play_button)
        how_to_play_button.clicked.connect(self.instructions)

        # Start Game button
        start_game_button = QPushButton('Start Game', buttons_container)
        self.set_button_style(start_game_button)
        start_game_button.clicked.connect(self.start)

        # Add buttons to the horizontal layout
        button_layout.addWidget(start_game_button)
        button_layout.addWidget(how_to_play_button)

        # Set the stylesheet for the main widget to cover the entire window
        self.setStyleSheet(f"background-image: url({self.background_image_path}); background-repeat: no-repeat; background-position: center; background-size: cover;")

        # Add the buttons container to the main layout
        main_layout.addWidget(buttons_container)

        self.center_on_screen()

        self.show()

    def set_background_image(self, label):
        # Set up background image
        pixmap = QPixmap(self.background_image_path)
        aspect_ratio = pixmap.width() / pixmap.height()
        new_width = min(self.width(), pixmap.width())
        new_height = int(new_width / aspect_ratio)
        pixmap = pixmap.scaled(new_width, new_height)
        label.setGeometry(0, 0, new_width, new_height)

    def center_on_screen(self):
        screen_geo = QDesktopWidget().screenGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def set_button_style(self, button):
        button.setFont(QFont("Verdana", 15))
        button.setMinimumSize(300, 80)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button.setStyleSheet("font-size: 20px; background-color: rgba(0, 0, 0, 0); border: none; border-radius: 20px;")

    def instructions(self):
        QMessageBox.information(self, 'How to Play', 'Use the W, A, S, D keys to move the character. Right-click to SPRINT, Left-click to ATTACK.')

    def start(self):
        print("Game starting...")

if __name__ == '__main__':
    app = QApplication([])
    launcher = GameLauncher()
    app.exec_()'''
    
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bryan + Matt's Game")
        self.setGeometry(200, 200, 800, 800)  # Set your desired window size

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
        layout.addStretch()  # Add flexible space to push buttons to the bottom
        layout.addWidget(button1, alignment=Qt.AlignCenter)
        layout.addWidget(button2, alignment=Qt.AlignCenter)

        self.show()

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
