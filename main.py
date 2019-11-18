#####################################
#       Trabalho Pratico            #
# --------------------------------- #
# Luiz Gustavo Braganca dos Santos  #
# 524507                            #
#####################################

# imports
import sys, os, math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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
        valorA, ok = QInputDialog.getText(self, 'Curva de Bézier', 'Digite a quantidade de pontos de controle:')
        self.BezierPtsControle = int(valorA)
    # fim Bezier()

    def mudar_valores(self):
        self.formGroupBox = QGroupBox('Alterar Valores')

        layout = QFormLayout()

        # Dialog de mudar valores
        x1 = QLabel("x1")
        x1_edit = QLineEdit()
        y1 = QLabel("y1")
        y1_edit = QLineEdit()

        layout.addRow(x1, x1_edit)
        layout.addRow(y1, y1_edit)
        self.formGroupBox.setLayout(layout)
    # fim mudar_valores()


    def initUI(self):
        self.setGeometry(300, 300, 1024, 738)
        self.setWindowTitle('Trabalho Prático - Computação Gráfica')
        self.setWindowIcon(QIcon('img/logo.png'))

        menubar = self.menuBar()

        # Menu Bezier
        BezierMenu = menubar.addMenu('&Bezier')

        BezierAction = BezierMenu.addAction('Curva Bezier')
        BezierAction.triggered.connect(self.Bezier)

        MudarValores = BezierMenu.addAction('Mudar Valores')
        MudarValores.triggered.connect(self.mudar_valores)

        # Menu Limpar Tela
        clearMenu = menubar.addMenu('&Clear')

        clearAction = clearMenu.addAction('Limpar tela')
        clearAction.triggered.connect(self.ClearScreen)
        self.show()
    # fim initUI()

    '''
        Metodo mousePressEvent() - Clicou em algum ponto do canvas.
    '''
    def mousePressEvent(self, event):
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

    '''
        Metodo paintEvent() - desenha no canvas. 
    '''
    def paintEvent(self, e):
        cor = Qt.black    
        pen = QPen(cor, 2, Qt.SolidLine)
        painter = QPainter(self)

        if self.comando == 'bezier':
            for p in self.BezCur:
                painter.drawPoint(p[0], p[1])
            # fim for

            if self.BezierVarControle < self.BezierPtsControle:
                pen = QPen(Qt.darkBlue, 3, Qt.SolidLine)
                painter.setPen(pen) 
                aux = bezier(1200, self.BezCur)

                for pontos in aux:
                    painter.drawPoint(pontos['x'], pontos['y'])
                # fim for
            else:
                pen = QPen(cor, 2, Qt.SolidLine)
                painter.setPen(pen) 
                aux = bezier(1200, self.BezCur)
                for pontos in aux:
                    painter.drawPoint(pontos['x'], pontos['y'])
                # fim for
            # fim if

            self.update()
        # fim if
    # fim paintEvent()
# fim class


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputacaoGrafica()
    sys.exit(app.exec_())
# fim main
