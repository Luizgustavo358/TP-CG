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


class Ui_Dialog(object):
    def __init__(self):
        super().__init__()

        self.Dialog = QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.show()
    # fim construtor

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 353)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QRect(20, 310, 331, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setGeometry(QRect(10, 20, 341, 281))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 321, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.y3_edit = QLineEdit(self.gridLayoutWidget)
        self.y3_edit.setObjectName("y3_edit")
        self.gridLayout.addWidget(self.y3_edit, 2, 3, 1, 1)
        self.y2_edit = QLineEdit(self.gridLayoutWidget)
        self.y2_edit.setObjectName("y2_edit")
        self.gridLayout.addWidget(self.y2_edit, 1, 3, 1, 1)
        self.y1_edit = QLineEdit(self.gridLayoutWidget)
        self.y1_edit.setObjectName("y1_edit")
        self.gridLayout.addWidget(self.y1_edit, 0, 3, 1, 1)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.x3_edit = QLineEdit(self.gridLayoutWidget)
        self.x3_edit.setObjectName("x3_edit")
        self.gridLayout.addWidget(self.x3_edit, 2, 1, 1, 1)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.x2_edit = QLineEdit(self.gridLayoutWidget)
        self.x2_edit.setObjectName("x2_edit")
        self.gridLayout.addWidget(self.x2_edit, 1, 1, 1, 1)
        self.x1_edit = QLineEdit(self.gridLayoutWidget)
        self.x1_edit.setObjectName("x1_edit")
        self.gridLayout.addWidget(self.x1_edit, 0, 1, 1, 1)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.x4_edit = QLineEdit(self.gridLayoutWidget)
        self.x4_edit.setObjectName("x4_edit")
        self.gridLayout.addWidget(self.x4_edit, 3, 1, 1, 1)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.y4_edit = QLineEdit(self.gridLayoutWidget)
        self.y4_edit.setObjectName("y4_edit")
        self.gridLayout.addWidget(self.y4_edit, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)
    # fim setupUi()

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Alterar"))
        self.groupBox.setTitle(_translate("Dialog", "Alterar Coordenadas:"))
        self.label_4.setText(_translate("Dialog", "y2"))
        self.label_6.setText(_translate("Dialog", "y3"))
        self.label.setText(_translate("Dialog", "x1"))
        self.label_2.setText(_translate("Dialog", "y1"))
        self.label_5.setText(_translate("Dialog", "x3"))
        self.label_3.setText(_translate("Dialog", "x2"))
        self.label_7.setText(_translate("Dialog", "x4"))
        self.label_8.setText(_translate("Dialog", "y4"))
    # fim retranslateUi()

    def set_elements(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1_edit.setText(x1)
        self.x2_edit.setText(x2)
        self.x3_edit.setText(x3)
        self.x4_edit.setText(x4)

        self.y1_edit.setText(y1)
        self.y2_edit.setText(y2)
        self.y3_edit.setText(y3)
        self.y4_edit.setText(y4)
    # fim set_elements()

    def get_elements(self):
        self.pontos = []
        self.pontos.append([str(self.x1_edit), str(self.y1_edit)])
        self.pontos.append([str(self.x2_edit), str(self.y2_edit)])
        self.pontos.append([str(self.x3_edit), str(self.y3_edit)])
        self.pontos.append([str(self.x4_edit), str(self.y4_edit)])

        return self.pontos
    # fim get_elementos()
# fim class


class ComputacaoGrafica(QMainWindow):
    '''
        Metodo construtor - inicializa todas as variaveis 
                            e a tela.
    '''
    def __init__(self):
        super().__init__()

        # variaveis
        self.BezCur = []
        self.comando = '' 
        self.BezierPtsControle = -1
        self.BezierVarControle = 0

        # inicializa a tela
        self.initUI()        
    # fim construtor()


    '''
        Metodo ClearScreen() - limpa todos os dados.
    '''
    def ClearScreen(self):
        self.BezCur = []
        self.BezierPtsControle = -1
        self.BezierVarControle = 0
        self.update()
    # fim ClearScreen()


    '''
        Metodo Bezier() - cria um dialog para escolha da quantidade de
                          pontos de controle.
    '''
    def Bezier(self):
        self.comando = 'bezier'
        valorA, ok = QInputDialog.getText(self, 'Curva de Bézier', 'Digite a quantidade de pontos de controle:')
        self.BezierPtsControle = int(valorA)
    # fim Bezier()


    '''
        Metodo mudar_valores() - muda os valores das coordenadas.
    '''
    def mudar_valores(self):
        ui = Ui_Dialog()
    # fim mudar_valores()


    '''
        Metodo initUI() - inicializa a interface grafica.
    '''
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
        clearMenu = menubar.addMenu('&Limpar')

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
