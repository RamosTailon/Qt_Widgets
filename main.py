import sys
import os

# IMPORTAR qt_core
from qt_core import *
# IMPORTAR MAIN WINDOW

from gui.windows.main_window.ui_main_window import *


class MainWindow (QMainWindow):  # classe responsavel por exibir a janela
    def __init__(self):
        super().__init__()

        # Adicionar o titulo na janela
        self.setWindowTitle("Aprendizado Janela")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        self.show()

    # FUNÇÕES BOTÕES
    # ///////////////////////////////////////////////

    def reset_selection(self):
        # findChildren procura uma classe especifica
        # neste caso deve se usar a classe pai = QPushButton
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def toggle_button(self):
        # GET MENU WIDTH
        menu_width = self.ui.left_menu.width()
        width = 50

        if menu_width == 50:
            width = 200

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # ///////////////////////////////////////////////


if __name__ == "__main__":  # definir a classe para iniciar no momento da execução do programa
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
