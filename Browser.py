import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import *
#my browser setting
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation bar
        navbar=QToolBar()
        self.addToolBar(navbar)
            #back button
        back_btn=QAction('↶',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
            #forward button
        fwd_btn=QAction('↷',self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)
            #Reload/Refresh Button
        re_btn=QAction('⟳',self)
        re_btn.triggered.connect(self.browser.reload)
        navbar.addAction(re_btn)
            #home button
        h_btn=QAction('Home',self)
        h_btn.triggered.connect(self.navigate_home)
        navbar.addAction(h_btn)
            #url bar/ Url serch
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
            #url bar
        self.browser.urlChanged.connect(self.update_url)


        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
app=QApplication(sys.argv)
QApplication.setApplicationName('VBrowser')
window=MainWindow()
app.exec_()
