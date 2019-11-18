#####################################
#       Trabalho Pratico            #
# --------------------------------- #
# Luiz Gustavo Braganca dos Santos  #
# 524507                            #
#####################################

# imports
import sys, os, math
from PyQt5.QtGui import (QIcon, QPainter, QPen)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QToolButton, QPushButton, QInputDialog, QLineEdit)
from implementacoes import bezier


class ComputacaoGrafica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.BezCur = []
        self.comando = '' 
        self.initUI()  

        self.BezierPtsControle = -1
        self.BezierVarControle = 0
    # fim construtor()

    def ClearScreen(self):
        self.BezCur = []
        self.BezierPtsControle = -1
        self.BezierVarControle = 0
        self.update()
    # fim ClearScreen()

    def Bezier(self):
        self.comando = 'bezier'
        valorA, ok = QInputDialog.getText(self, 'Input Dialog', 'Digite a quantidade de pontos de controle')
        self.BezierPtsControle = int(valorA)
    # fim Bezier()

    def initUI(self):
        self.setGeometry(300, 300, 1024, 738)
        self.setWindowTitle('Trabalho Prático - Computação Gráfica')
        self.setWindowIcon(QIcon('img/logo.png'))

        menubar = self.menuBar()

        # Menu Bezier
        BezierMenu = menubar.addMenu('&Bezier')

        BezierAction = BezierMenu.addAction('Curva Bezier')
        BezierAction.triggered.connect(self.Bezier)

        # Menu Limpar Tela
        clearMenu = menubar.addMenu('&Clear')

        clearAction = clearMenu.addAction('Limpar tela')
        clearAction.triggered.connect(self.ClearScreen)
        self.show()
    # fim initUI()

    '''
        Clicou em algum ponto do grafico
    '''
    def mousePressEvent(self, event): 
        # BEZIER
        if event.button() == Qt.LeftButton:
            if self.comando == 'bezier':                
                x = event.pos().x()
                y = event.pos().y()
                if self.BezierVarControle < self.BezierPtsControle:
                    self.BezierVarControle += 1
                    self.BezCur.append([x, y])
                # fim if
            # fim if
        # fim if
    # fim mousePressEvent()

    def paintEvent(self, e):
        cor = Qt.black    
        pen = QPen(cor, 3, Qt.SolidLine)                    
        painter = QPainter(self)

        if self.comando == 'bezier':
            for p in self.BezCur:
                painter.drawPoint(p[0], p[1])
            # fim for

            if self.BezierVarControle < self.BezierPtsControle:
                pen = QPen(Qt.darkBlue, 8, Qt.SolidLine)
                painter.setPen(pen) 
                aux = bezier(1200, self.BezCur)

                for pontos in aux:
                    painter.drawPoint(pontos['x'], pontos['y'])
                # fim for
            else:
                pen = QPen(cor, 3, Qt.SolidLine)
                painter.setPen(pen) 
                aux = bezier(1200, self.BezCur)
                for pontos in aux:
                    painter.drawPoint(pontos['x'], pontos['y'])
                # fim for
            # fim if

            self.update()
        # fim if
    # fim paintEvent()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputacaoGrafica()
    sys.exit(app.exec_())
# fim main
