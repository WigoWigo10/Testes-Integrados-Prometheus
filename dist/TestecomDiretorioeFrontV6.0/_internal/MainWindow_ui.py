# Form implementation generated from reading ui file 'e:\Executavel Touch\Rotina de Testes Integrada\TestecomDiretorioeFrontV6.0\dist\TestecomDiretorioeFrontV6.0\_internal\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAccessibleName("")
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet("background-color: #343436;\n"
"\n"
"background-color: rgb(36, 36, 46);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.Botao_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Botao_reset.setGeometry(QtCore.QRect(20, 14, 75, 23))
        self.Botao_reset.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #de0341;\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #de0341;\n"
"    background-color:white;\n"
"    color: #de0341;\n"
"    border-radius:10\n"
"}")
        self.Botao_reset.setObjectName("Botao_reset")
        self.Label_Diretorio_Salvamento = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_Diretorio_Salvamento.setGeometry(QtCore.QRect(230, 500, 291, 23))
        self.Label_Diretorio_Salvamento.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.Label_Diretorio_Salvamento.setMouseTracking(False)
        self.Label_Diretorio_Salvamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius:5")
        self.Label_Diretorio_Salvamento.setText("")
        self.Label_Diretorio_Salvamento.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_Diretorio_Salvamento.setIndent(0)
        self.Label_Diretorio_Salvamento.setObjectName("Label_Diretorio_Salvamento")
        self.Texto_Localdesalvamento = QtWidgets.QLabel(parent=self.centralwidget)
        self.Texto_Localdesalvamento.setGeometry(QtCore.QRect(30, 500, 191, 23))
        self.Texto_Localdesalvamento.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Localdesalvamento.setObjectName("Texto_Localdesalvamento")
        self.Botao_DiretorioSalvamento = QtWidgets.QToolButton(parent=self.centralwidget)
        self.Botao_DiretorioSalvamento.setGeometry(QtCore.QRect(530, 500, 25, 19))
        self.Botao_DiretorioSalvamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Botao_DiretorioSalvamento.setObjectName("Botao_DiretorioSalvamento")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 49, 671, 431))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_PowerHub = QtWidgets.QWidget()
        self.tab_PowerHub.setStyleSheet("background-color: #343436;")
        self.tab_PowerHub.setObjectName("tab_PowerHub")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab_PowerHub)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 671, 401))
        self.scrollArea.setStyleSheet("background-color: #343436;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Texto_AC = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_AC.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.Texto_AC.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_AC.setObjectName("Texto_AC")
        self.Botao_Ativar_AC = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.Botao_Ativar_AC.setGeometry(QtCore.QRect(130, 30, 111, 23))
        self.Botao_Ativar_AC.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_Ativar_AC.setObjectName("Botao_Ativar_AC")
        self.spinBox_AC_segundos = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_AC_segundos.setGeometry(QtCore.QRect(400, 30, 51, 22))
        self.spinBox_AC_segundos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_AC_segundos.setSuffix("")
        self.spinBox_AC_segundos.setPrefix("")
        self.spinBox_AC_segundos.setMinimum(5)
        self.spinBox_AC_segundos.setMaximum(100)
        self.spinBox_AC_segundos.setSingleStep(5)
        self.spinBox_AC_segundos.setObjectName("spinBox_AC_segundos")
        self.Texto_AC_por = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_AC_por.setGeometry(QtCore.QRect(310, 30, 21, 16))
        self.Texto_AC_por.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_AC_por.setObjectName("Texto_AC_por")
        self.Texto_AC_segundos = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_AC_segundos.setGeometry(QtCore.QRect(500, 30, 61, 16))
        self.Texto_AC_segundos.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_AC_segundos.setObjectName("Texto_AC_segundos")
        self.spinBox_HDMI_segundos = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_HDMI_segundos.setGeometry(QtCore.QRect(400, 70, 51, 22))
        self.spinBox_HDMI_segundos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_HDMI_segundos.setSuffix("")
        self.spinBox_HDMI_segundos.setPrefix("")
        self.spinBox_HDMI_segundos.setMinimum(5)
        self.spinBox_HDMI_segundos.setMaximum(100)
        self.spinBox_HDMI_segundos.setSingleStep(5)
        self.spinBox_HDMI_segundos.setObjectName("spinBox_HDMI_segundos")
        self.Texto_HDMI_por = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_HDMI_por.setGeometry(QtCore.QRect(310, 70, 21, 16))
        self.Texto_HDMI_por.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_HDMI_por.setObjectName("Texto_HDMI_por")
        self.Botao_Ativar_HDMI = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.Botao_Ativar_HDMI.setGeometry(QtCore.QRect(130, 70, 111, 23))
        self.Botao_Ativar_HDMI.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_Ativar_HDMI.setObjectName("Botao_Ativar_HDMI")
        self.Texto_HDMI = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_HDMI.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.Texto_HDMI.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_HDMI.setObjectName("Texto_HDMI")
        self.Texto_HDMI_segundos = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_HDMI_segundos.setGeometry(QtCore.QRect(500, 70, 61, 16))
        self.Texto_HDMI_segundos.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_HDMI_segundos.setObjectName("Texto_HDMI_segundos")
        self.spinBox_Fan_segundos = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_Fan_segundos.setGeometry(QtCore.QRect(400, 110, 51, 22))
        self.spinBox_Fan_segundos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_Fan_segundos.setSuffix("")
        self.spinBox_Fan_segundos.setPrefix("")
        self.spinBox_Fan_segundos.setMinimum(5)
        self.spinBox_Fan_segundos.setMaximum(100)
        self.spinBox_Fan_segundos.setSingleStep(5)
        self.spinBox_Fan_segundos.setObjectName("spinBox_Fan_segundos")
        self.Texto_Fan_por = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_Fan_por.setGeometry(QtCore.QRect(310, 110, 21, 16))
        self.Texto_Fan_por.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Fan_por.setObjectName("Texto_Fan_por")
        self.Botao_Ativar_Fan = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.Botao_Ativar_Fan.setGeometry(QtCore.QRect(130, 110, 111, 23))
        self.Botao_Ativar_Fan.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_Ativar_Fan.setObjectName("Botao_Ativar_Fan")
        self.Texto_Fan_segundos = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_Fan_segundos.setGeometry(QtCore.QRect(500, 110, 61, 16))
        self.Texto_Fan_segundos.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Fan_segundos.setObjectName("Texto_Fan_segundos")
        self.Texto_Fan = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_Fan.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.Texto_Fan.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Fan.setObjectName("Texto_Fan")
        self.Texto_LID_por = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_LID_por.setGeometry(QtCore.QRect(310, 150, 21, 16))
        self.Texto_LID_por.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_LID_por.setObjectName("Texto_LID_por")
        self.spinBox_LID_segundos = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_LID_segundos.setGeometry(QtCore.QRect(400, 150, 51, 22))
        self.spinBox_LID_segundos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_LID_segundos.setSuffix("")
        self.spinBox_LID_segundos.setPrefix("")
        self.spinBox_LID_segundos.setMinimum(5)
        self.spinBox_LID_segundos.setMaximum(100)
        self.spinBox_LID_segundos.setSingleStep(5)
        self.spinBox_LID_segundos.setObjectName("spinBox_LID_segundos")
        self.Texto_LID = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_LID.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.Texto_LID.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_LID.setObjectName("Texto_LID")
        self.Texto_LID_segundos = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_LID_segundos.setGeometry(QtCore.QRect(500, 150, 61, 16))
        self.Texto_LID_segundos.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_LID_segundos.setObjectName("Texto_LID_segundos")
        self.Botao_Ativar_LID = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.Botao_Ativar_LID.setGeometry(QtCore.QRect(130, 150, 111, 23))
        self.Botao_Ativar_LID.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_Ativar_LID.setObjectName("Botao_Ativar_LID")
        self.Texto_ServoMotor = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_ServoMotor.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.Texto_ServoMotor.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_ServoMotor.setObjectName("Texto_ServoMotor")
        self.Texto_ServoMotor_por = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_ServoMotor_por.setGeometry(QtCore.QRect(320, 280, 21, 16))
        self.Texto_ServoMotor_por.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_ServoMotor_por.setObjectName("Texto_ServoMotor_por")
        self.Botao_Ativar_ServoMotor = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.Botao_Ativar_ServoMotor.setGeometry(QtCore.QRect(130, 210, 111, 23))
        self.Botao_Ativar_ServoMotor.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_Ativar_ServoMotor.setObjectName("Botao_Ativar_ServoMotor")
        self.Texto_ServoMotor_segundos = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_ServoMotor_segundos.setGeometry(QtCore.QRect(500, 280, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Texto_ServoMotor_segundos.sizePolicy().hasHeightForWidth())
        self.Texto_ServoMotor_segundos.setSizePolicy(sizePolicy)
        self.Texto_ServoMotor_segundos.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_ServoMotor_segundos.setObjectName("Texto_ServoMotor_segundos")
        self.spinBox_ServoMotor_segundos = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_ServoMotor_segundos.setGeometry(QtCore.QRect(400, 280, 51, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_ServoMotor_segundos.sizePolicy().hasHeightForWidth())
        self.spinBox_ServoMotor_segundos.setSizePolicy(sizePolicy)
        self.spinBox_ServoMotor_segundos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_ServoMotor_segundos.setSuffix("")
        self.spinBox_ServoMotor_segundos.setPrefix("")
        self.spinBox_ServoMotor_segundos.setMinimum(5)
        self.spinBox_ServoMotor_segundos.setMaximum(100)
        self.spinBox_ServoMotor_segundos.setSingleStep(5)
        self.spinBox_ServoMotor_segundos.setObjectName("spinBox_ServoMotor_segundos")
        self.QComboBox_ServoMotor_ID = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.QComboBox_ServoMotor_ID.setGeometry(QtCore.QRect(20, 280, 111, 22))
        self.QComboBox_ServoMotor_ID.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.QComboBox_ServoMotor_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.QComboBox_ServoMotor_ID.setObjectName("QComboBox_ServoMotor_ID")
        self.QComboBox_ServoMotor_ID.addItem("")
        self.QComboBox_ServoMotor_ID.addItem("")
        self.Texto_ServoMotor_para = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_ServoMotor_para.setGeometry(QtCore.QRect(20, 320, 41, 16))
        self.Texto_ServoMotor_para.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_ServoMotor_para.setObjectName("Texto_ServoMotor_para")
        self.Texto_ServoMotor_Direcao = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Texto_ServoMotor_Direcao.setGeometry(QtCore.QRect(160, 250, 101, 16))
        self.Texto_ServoMotor_Direcao.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_ServoMotor_Direcao.setObjectName("Texto_ServoMotor_Direcao")
        self.QComboBox_ServoMotor_Direcao = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.QComboBox_ServoMotor_Direcao.setGeometry(QtCore.QRect(160, 280, 111, 22))
        self.QComboBox_ServoMotor_Direcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.QComboBox_ServoMotor_Direcao.setObjectName("QComboBox_ServoMotor_Direcao")
        self.QComboBox_ServoMotor_Direcao.addItem("")
        self.QComboBox_ServoMotor_Direcao.addItem("")
        self.spinBox_ServoMotor_AnguloDesejado = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.spinBox_ServoMotor_AnguloDesejado.setGeometry(QtCore.QRect(70, 320, 51, 22))
        self.spinBox_ServoMotor_AnguloDesejado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_ServoMotor_AnguloDesejado.setPrefix("")
        self.spinBox_ServoMotor_AnguloDesejado.setMinimum(-90)
        self.spinBox_ServoMotor_AnguloDesejado.setMaximum(90)
        self.spinBox_ServoMotor_AnguloDesejado.setSingleStep(1)
        self.spinBox_ServoMotor_AnguloDesejado.setProperty("value", 0)
        self.spinBox_ServoMotor_AnguloDesejado.setObjectName("spinBox_ServoMotor_AnguloDesejado")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_PowerHub, "")
        self.tab_Touch = QtWidgets.QWidget()
        self.tab_Touch.setStyleSheet("background-color: #343436;")
        self.tab_Touch.setObjectName("tab_Touch")
        self.Botao_TesteTouch = QtWidgets.QPushButton(parent=self.tab_Touch)
        self.Botao_TesteTouch.setGeometry(QtCore.QRect(30, 40, 111, 23))
        self.Botao_TesteTouch.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_TesteTouch.setText("Teste de Touch")
        self.Botao_TesteTouch.setObjectName("Botao_TesteTouch")
        self.Label_Diretorio_EXE_Touch = QtWidgets.QLabel(parent=self.tab_Touch)
        self.Label_Diretorio_EXE_Touch.setGeometry(QtCore.QRect(190, 40, 291, 23))
        self.Label_Diretorio_EXE_Touch.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.Label_Diretorio_EXE_Touch.setMouseTracking(False)
        self.Label_Diretorio_EXE_Touch.setTabletTracking(False)
        self.Label_Diretorio_EXE_Touch.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Label_Diretorio_EXE_Touch.setAcceptDrops(False)
        self.Label_Diretorio_EXE_Touch.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Label_Diretorio_EXE_Touch.setAutoFillBackground(False)
        self.Label_Diretorio_EXE_Touch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius:5")
        self.Label_Diretorio_EXE_Touch.setText("")
        self.Label_Diretorio_EXE_Touch.setScaledContents(False)
        self.Label_Diretorio_EXE_Touch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_Diretorio_EXE_Touch.setWordWrap(False)
        self.Label_Diretorio_EXE_Touch.setObjectName("Label_Diretorio_EXE_Touch")
        self.Botao_DiretorioTouch = QtWidgets.QToolButton(parent=self.tab_Touch)
        self.Botao_DiretorioTouch.setGeometry(QtCore.QRect(490, 40, 25, 19))
        self.Botao_DiretorioTouch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Botao_DiretorioTouch.setObjectName("Botao_DiretorioTouch")
        self.Box_Valordeloop_Touch = QtWidgets.QSpinBox(parent=self.tab_Touch)
        self.Box_Valordeloop_Touch.setGeometry(QtCore.QRect(560, 40, 61, 23))
        self.Box_Valordeloop_Touch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Box_Valordeloop_Touch.setWrapping(True)
        self.Box_Valordeloop_Touch.setMinimum(1)
        self.Box_Valordeloop_Touch.setMaximum(1000000)
        self.Box_Valordeloop_Touch.setProperty("value", 1)
        self.Box_Valordeloop_Touch.setDisplayIntegerBase(10)
        self.Box_Valordeloop_Touch.setObjectName("Box_Valordeloop_Touch")
        self.Texto_Loop_3 = QtWidgets.QLabel(parent=self.tab_Touch)
        self.Texto_Loop_3.setGeometry(QtCore.QRect(190, 20, 251, 16))
        self.Texto_Loop_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Loop_3.setObjectName("Texto_Loop_3")
        self.Texto_Loop_Touch = QtWidgets.QLabel(parent=self.tab_Touch)
        self.Texto_Loop_Touch.setGeometry(QtCore.QRect(560, 20, 47, 13))
        self.Texto_Loop_Touch.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Loop_Touch.setObjectName("Texto_Loop_Touch")
        self.tabWidget.addTab(self.tab_Touch, "")
        self.tab_Keyboard = QtWidgets.QWidget()
        self.tab_Keyboard.setStyleSheet("background-color: #343436;")
        self.tab_Keyboard.setObjectName("tab_Keyboard")
        self.Botao_TesteTeclado = QtWidgets.QPushButton(parent=self.tab_Keyboard)
        self.Botao_TesteTeclado.setGeometry(QtCore.QRect(30, 40, 111, 23))
        self.Botao_TesteTeclado.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Botao_TesteTeclado.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(87, 90, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 196, 223);\n"
"    color: rgb(34, 36, 43);\n"
"    border-radius:7\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(62, 101, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10\n"
"\n"
"}")
        self.Botao_TesteTeclado.setObjectName("Botao_TesteTeclado")
        self.Label_Diretorio_EXE_Teclado = QtWidgets.QLabel(parent=self.tab_Keyboard)
        self.Label_Diretorio_EXE_Teclado.setGeometry(QtCore.QRect(190, 40, 291, 23))
        self.Label_Diretorio_EXE_Teclado.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.Label_Diretorio_EXE_Teclado.setMouseTracking(True)
        self.Label_Diretorio_EXE_Teclado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-radius:5")
        self.Label_Diretorio_EXE_Teclado.setText("")
        self.Label_Diretorio_EXE_Teclado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_Diretorio_EXE_Teclado.setObjectName("Label_Diretorio_EXE_Teclado")
        self.Botao_DiretorioTeclado = QtWidgets.QToolButton(parent=self.tab_Keyboard)
        self.Botao_DiretorioTeclado.setGeometry(QtCore.QRect(490, 40, 25, 19))
        self.Botao_DiretorioTeclado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Botao_DiretorioTeclado.setObjectName("Botao_DiretorioTeclado")
        self.Box_Valordeloop_Teclado = QtWidgets.QSpinBox(parent=self.tab_Keyboard)
        self.Box_Valordeloop_Teclado.setGeometry(QtCore.QRect(560, 40, 61, 23))
        self.Box_Valordeloop_Teclado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Box_Valordeloop_Teclado.setWrapping(True)
        self.Box_Valordeloop_Teclado.setReadOnly(False)
        self.Box_Valordeloop_Teclado.setMinimum(1)
        self.Box_Valordeloop_Teclado.setMaximum(1000000)
        self.Box_Valordeloop_Teclado.setProperty("value", 1)
        self.Box_Valordeloop_Teclado.setObjectName("Box_Valordeloop_Teclado")
        self.Texto_Loop_Keyboard = QtWidgets.QLabel(parent=self.tab_Keyboard)
        self.Texto_Loop_Keyboard.setGeometry(QtCore.QRect(560, 20, 47, 13))
        self.Texto_Loop_Keyboard.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Loop_Keyboard.setObjectName("Texto_Loop_Keyboard")
        self.Texto_Diretorio_Keyboard = QtWidgets.QLabel(parent=self.tab_Keyboard)
        self.Texto_Diretorio_Keyboard.setGeometry(QtCore.QRect(190, 20, 251, 16))
        self.Texto_Diretorio_Keyboard.setStyleSheet("color: rgb(255, 255, 255);")
        self.Texto_Diretorio_Keyboard.setObjectName("Texto_Diretorio_Keyboard")
        self.tabWidget.addTab(self.tab_Keyboard, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rotina de Teste"))
        self.Botao_reset.setText(_translate("MainWindow", "Reset"))
        self.Texto_Localdesalvamento.setText(_translate("MainWindow", "Local de salvamento do relatório:"))
        self.Botao_DiretorioSalvamento.setText(_translate("MainWindow", "..."))
        self.Texto_AC.setText(_translate("MainWindow", "AC:"))
        self.Botao_Ativar_AC.setText(_translate("MainWindow", "Ativar"))
        self.Texto_AC_por.setText(_translate("MainWindow", "por"))
        self.Texto_AC_segundos.setText(_translate("MainWindow", "segundos"))
        self.Texto_HDMI_por.setText(_translate("MainWindow", "por"))
        self.Botao_Ativar_HDMI.setText(_translate("MainWindow", "Ativar"))
        self.Texto_HDMI.setText(_translate("MainWindow", "HDMI:"))
        self.Texto_HDMI_segundos.setText(_translate("MainWindow", "segundos"))
        self.Texto_Fan_por.setText(_translate("MainWindow", "por"))
        self.Botao_Ativar_Fan.setText(_translate("MainWindow", "Ativar"))
        self.Texto_Fan_segundos.setText(_translate("MainWindow", "segundos"))
        self.Texto_Fan.setText(_translate("MainWindow", "Fan:"))
        self.Texto_LID_por.setText(_translate("MainWindow", "por"))
        self.Texto_LID.setText(_translate("MainWindow", "LID:"))
        self.Texto_LID_segundos.setText(_translate("MainWindow", "segundos"))
        self.Botao_Ativar_LID.setText(_translate("MainWindow", "Ativar"))
        self.Texto_ServoMotor.setText(_translate("MainWindow", "Servo Motor:"))
        self.Texto_ServoMotor_por.setText(_translate("MainWindow", "por"))
        self.Botao_Ativar_ServoMotor.setText(_translate("MainWindow", "Ativar"))
        self.Texto_ServoMotor_segundos.setText(_translate("MainWindow", "segundos"))
        self.QComboBox_ServoMotor_ID.setItemText(0, _translate("MainWindow", "Servo Motor 1"))
        self.QComboBox_ServoMotor_ID.setItemText(1, _translate("MainWindow", "Servo Motor 2"))
        self.Texto_ServoMotor_para.setText(_translate("MainWindow", "para"))
        self.Texto_ServoMotor_Direcao.setText(_translate("MainWindow", "Direção:"))
        self.QComboBox_ServoMotor_Direcao.setItemText(0, _translate("MainWindow", "Positiva"))
        self.QComboBox_ServoMotor_Direcao.setItemText(1, _translate("MainWindow", "Negativa"))
        self.spinBox_ServoMotor_AnguloDesejado.setSuffix(_translate("MainWindow", "°"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_PowerHub), _translate("MainWindow", "Power Hub"))
        self.Botao_DiretorioTouch.setText(_translate("MainWindow", "..."))
        self.Texto_Loop_3.setText(_translate("MainWindow", "Local do Diratório"))
        self.Texto_Loop_Touch.setText(_translate("MainWindow", "Loop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Touch), _translate("MainWindow", "Touch"))
        self.Botao_TesteTeclado.setText(_translate("MainWindow", "Teste de Teclado"))
        self.Botao_DiretorioTeclado.setText(_translate("MainWindow", "..."))
        self.Texto_Loop_Keyboard.setText(_translate("MainWindow", "Loop"))
        self.Texto_Diretorio_Keyboard.setText(_translate("MainWindow", "Local do Diratório"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Keyboard), _translate("MainWindow", "Keyboard"))
