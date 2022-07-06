import os
from qt_core import *


class PyPushButton(QPushButton):
    def __init__(
        self,
        text='',
        heigth=40,
        minimum_width=50,
        text_padding=55,  # afastar o texto do alinhamento da direita
        text_color='#c3ccdf',
        icon_path="",
        icon_color="#c3ccdf",
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False
    ):
        super().__init__()

        # SET DEFAULT PARAMETERS
        self.setText(text)
        self.setMinimumHeight(heigth)
        self.setMaximumHeight(heigth)
        # quando o mouse passar em cima
        self.setCursor(Qt.PointingHandCursor)

        # CUSTOM PARAMETERS
        # ////////////////////////////////////////////////////
        self.minimum_width = minimum_width  # deixar o parametro global
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        # ///////////////////////////////////////////////////

        # set style
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active



        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )

    def set_style(
        self,
        text_padding=55,  # afastar o texto do alinhamento da direita
        text_color='#c3ccdf',
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False

    ):
        # style é uma variavel do tipo string
        style = f""" 
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """
        active_style = f"""
        QPushButton{{
            background-color: {btn_hover};
            border-right: 5px solid #282a36;

        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
    # sobre-escreve todo o estilo

    def paintEvent(self, event):
        # é necessário criar um função que recupera as informações da classe = default style
        QPushButton.paintEvent(self, event)

        # quadro de desenho
        # ///////////////////////////////////////////////////
        qp = QPainter()
        qp.begin(self)  # para começar a pintura
        qp.setRenderHint(QPainter.Antialiasing)  # seta antialiasing = vetor
        qp.setPen(Qt.NoPen)  # sem bordas

        #retangulo, container
        rect = QRect(0, 0, self.minimum_width, self.height())
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        # sempre que abrir o qpainter deve fechar
        qp.end()
        # ///////////////////////////////////////////////////

    def draw_icon(self, qp, image, rect, color):
        # pegar a pasta pelo caminho absoluto = path = abspath
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        # normalizando o caminho = pra rodar independente do sistema Operacional
        icon_path = os.path.normpath(os.path.join(path, image))

        # desenhar o icone
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        # mascara para vetores
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        # pega informações de posicionamento e tamanho
        painter.fillRect(icon.rect(), color)

        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
