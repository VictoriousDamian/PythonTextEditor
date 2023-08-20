import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QWebView


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.resize(800, 600)

        # Create the address bar and Go button
        self.address_bar = QLineEdit()
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.load_url)

        # Create the web view
        self.web_view = QWebView()

        # Create a layout for the address bar and web view
        layout = QVBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.go_button)
        layout.addWidget(self.web_view)

        # Create a main widget and set the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

    def load_url(self):
        url = self.address_bar.text()
        if url.startswith('http://') or url.startswith('https://'):
            self.web_view.load(QUrl(url))
        else:
            self.web_view.load(QUrl('http://' + url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
