import sys


from files import *


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


user = ''
name = 'Anihub App'

home = 'https://anihub.tv'
profile = 'https://anihub.tv/perfil/[]'
anime_list = 'https://anihub.tv/perfil/[]/minha-lista'
vip = 'https://anihub.tv/perfil/[]/editar/vip'

developer = 'https://anihub.tv/perfil/kaueguimaraes'

if exist('user.txt'):
    user = read('user.txt')
else:
    write('user.txt', '')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(home))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        # Definindo itens
        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)

        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(self.browser.forward)

        reload_btn = QAction('Recarregar', self)
        reload_btn.triggered.connect(self.browser.reload)

        home_btn = QAction('Início', self)
        home_btn.triggered.connect(self.navigate_home)

        self.user = QLineEdit()
        self.user.setText(user)

        set_user_btn = QAction('Adicionar usuário', self)
        set_user_btn.triggered.connect(self.set_user)

        profile_btn = QAction('Perfil', self)
        profile_btn.triggered.connect(self.go_to_profile)

        anime_list_btn = QAction('Anime', self)
        anime_list_btn.triggered.connect(self.go_to_anime_list)

        developer_btn = QAction('Developer', self)
        developer_btn.triggered.connect(self.go_to_developer)

        vip_btn = QAction('VIP', self)
        vip_btn.triggered.connect(self.go_to_vip)

        # Adicionando a navbar
        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(reload_btn)
        navbar.addAction(home_btn)
        navbar.addWidget(self.user)
        navbar.addAction(set_user_btn)
        navbar.addAction(profile_btn)
        navbar.addAction(anime_list_btn)
        navbar.addAction(developer_btn)
        navbar.addAction(vip_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl(home))
    
    # Atalhos
    def go_to_profile(self):
        new_url = profile.replace('[]', user)
        print(new_url)
        self.browser.setUrl(QUrl(new_url))
    
    def go_to_anime_list(self):
        new_url = anime_list.replace('[]', user)
        print(new_url)
        self.browser.setUrl(QUrl(new_url))
    
    def go_to_vip(self):
        new_url = vip.replace('[]', user)
        print(new_url)
        self.browser.setUrl(QUrl(new_url))
    #Atalhos

    def go_to_developer(self):
        self.browser.setUrl(QUrl(developer))

    def set_user(self):
        global user

        user = self.user.text()
        delete('user.txt')
        write('user.txt', user)
        print(user)

        return user

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName(name)
window = MainWindow()
app.exec_()


