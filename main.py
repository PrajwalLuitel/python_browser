from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('   <       ', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(' >          ' , self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload     ', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home   ', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.Url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://duckduckgo.com'))


    def navigate_to_url(self):
        url = self.Url_bar.text()
        if url[:7] != "http://" and url[:8] != "https://":
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.Url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("My Python Browser")
window = MainWindow()
app.exec_()