# IMPORTAR qt_core
from qt_core import *

# IMPORTAR PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton


# JANELA PRINCIPAL
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # PARAMETROS INICIAIS
        parent.resize(960, 580)
        parent.setMinimumSize(720, 480)

        # CRIAR UM CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # CRIAR LAYOUT PRINCIPAL
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        # Todo Layout é bom zerar os espaçamentos

       # ///////////////////////////////////////////////
       # MENU LATERAL

        # MENU ESQUERDA
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LAYOUT DO MENU ESQUERDO
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU TOGGLE
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        # cor de fundo
        '''self.left_menu_top_frame.setStyleSheet(
            "#left_menu_top_frame { background-color: red; }")'''

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # ////////////////////////////////////////////
        # BOTOES
        # TOP BUTTONS
        self.toggle_button = PyPushButton(
            text="Menu",
            icon_path="icon_menu.svg"
        )
        self.btn_1 = PyPushButton(
            text="Página Inicial",
            is_active=True,
            icon_path="icon_home.svg"
        )
        self.btn_2 = PyPushButton(
            text="Página 2",
            icon_path="icon_widgets.svg"
        )

        # ADD BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # MENU SPACER
        self.left_menu_space = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        # cor de fundo
        '''self.left_menu_bottom_frame.setStyleSheet(
            "#left_menu_bottom_frame { background-color: red; }")'''

        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BUTTONS
        self.settings_btn = PyPushButton(
            text="Configurações",
            icon_path="icon_settings.svg"
        )

        # ADD BOTTOM BUTTON TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_space)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)

        # ////////////////////////////////////////////
        # CONTEUDO E PÁGINAS

        # CONTEUDO
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # BARRA TOPO
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet(
            "background-color: #21232d; color: #6272a4 ")

        # LAYOUT CONTEUDO
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)  # Espaço margem

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Label esquerda
        self.top_label_left = QLabel("Primeira aplicação PySide6!")
        # top spacer
        self.top_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Label direita
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # ADICIONAR LABEL AO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        # tem que adicionar que item pq o top_spacer é qspacerITEM
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # ////////////////////////////////////////////////////////////

        # PAGINAS DE APLICAÇÃO
        self.pages = QStackedWidget()
        self.pages.setStyleSheet(
            "font-size: 12px; color: #f8f8f2;")

        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        # deixando a página atual
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # BARRA FINAL
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet(
            "background-color: #21232d; color: #6272a4 ")

        # layout bottom
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Label esquerda
        self.bottom_label_left = QLabel("Criado por: Tailon")
        # top spacer
        self.bottom_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Label direita
        self.bottom_label_right = QLabel("2021")

        # ADICIONAR LABEL AO LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        # tem que adicionar qual item
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # ADICIONAR ELEMENTOS NO LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADICIONAR OS WIDGETS A APLICAÇÃO
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL FRAME
        parent.setCentralWidget(self.central_frame)
