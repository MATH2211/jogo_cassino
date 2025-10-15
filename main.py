# main.py

from PyQt6.QtWidgets import QApplication
import sys

# Importa a classe da janela definida no outro arquivo
from game_window import JanelaPrincipal 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())