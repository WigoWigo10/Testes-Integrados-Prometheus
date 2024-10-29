# main.py
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal
import os
import sys
import time
import threading
import signal
from MainWindow import Ui_MainWindow
from touch_test import TouchTest
from keyboardscan_test import KeyboardScanTest
from ac_test import ACTest
from hdmi_test import HDMITest
from fan_test import FANTest
from lid_test import LIDTest

class MonitorThread(QThread):
    loop_concluido = pyqtSignal(str)

    def __init__(self, relatorio_path, tipo_teste):
        super().__init__()
        self.relatorio_path = relatorio_path
        self.tipo_teste = tipo_teste
        self._is_running = True

    def run(self):
        while self._is_running:
            time.sleep(5)
            done_file = os.path.join(self.relatorio_path, self.tipo_teste, "done.txt")
            if os.path.exists(done_file):
                self.loop_concluido.emit(self.tipo_teste)
                os.remove(done_file)
                self._is_running = False

    def stop(self):
        self._is_running = False


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(690, 540)
        self.setupUi(self)

        self.RELATORIO_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "RotinadeTestes")
        self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)

        self.Botao_reset.clicked.connect(self.Resetar)
        self.Botao_TesteTouch.clicked.connect(self.Executar_TesteTouch_bat)
        self.Botao_DiretorioTouch.clicked.connect(self.SelecionarArquivo_Executavel_Touch)
        self.Botao_TesteTecladoScan.clicked.connect(self.Executar_TesteTecladoScan_bat)
        self.Botao_DiretorioTecladoScan.clicked.connect(self.SelecionarArquivo_Executavel_KeyboardScan)
        
        #Testes da Power Hub
        #self.Botao_Ativar_AC.clicked.connect(self.Executar_TesteAC_bat)
        self.Botao_Ativar_HDMI.clicked.connect(self.Executar_TesteHDMI_bat)
        self.Botao_Ativar_Fan.clicked.connect(self.Executar_TesteFAN_bat)
        self.Botao_Ativar_LID.clicked.connect(self.Executar_TesteLID_bat)
        
        self.Botao_DiretorioSalvamento.clicked.connect(self.MudarDiretorio_da_Saida)

    def closeEvent(self, event):
        # Encerra todos os processos em execução antes de fechar a janela
        print("Fechando o programa...")

        # Pode-se iterar sobre os threads e parar qualquer um que ainda esteja em execução
        for thread in threading.enumerate():
            if thread is not threading.main_thread():
                print(f"Encerrando thread: {thread.name}")
                if isinstance(thread, MonitorThread):
                    thread.stop()

        # Encerra o aplicativo
        os._exit(0)
        
    def Executar_TesteLID_bat(self):
        segundos_lid = self.spinBox_LID_segundos.value()
        segundos_lid = int(segundos_lid)
        self.lid_test = LIDTest(self.RELATORIO_PATH, segundos_lid)
        threading.Thread(target=self.lid_test.executar_lid).start()
        self.monitor_thread_lid = MonitorThread(self.RELATORIO_PATH, "PowerHub/LID")
        self.monitor_thread_lid.loop_concluido.connect(lambda: self.lid_test.exibir_mensagem("conclusão", "LID"))
        self.monitor_thread_lid.start()
        
    def Executar_TesteFAN_bat(self):
        segundos_fan = self.spinBox_Fan_segundos.value()
        self.fan_test = FANTest(self.RELATORIO_PATH, segundos_fan)
        threading.Thread(target=self.fan_test.executar_fan).start()
        self.monitor_thread_fan = MonitorThread(self.RELATORIO_PATH, "PowerHub/FAN")
        self.monitor_thread_fan.loop_concluido.connect(lambda: self.fan_test.exibir_mensagem("conclusão", "FAN"))
        self.monitor_thread_fan.start()

    def Executar_TesteHDMI_bat(self):
        segundos_hdmi = self.spinBox_HDMI_segundos.value()
        self.hdmi_test = HDMITest(self.RELATORIO_PATH, segundos_hdmi)
        threading.Thread(target=self.hdmi_test.executar_hdmi).start()
        self.monitor_thread_hdmi = MonitorThread(self.RELATORIO_PATH, "PowerHub/HDMI")
        self.monitor_thread_hdmi.loop_concluido.connect(lambda: self.hdmi_test.exibir_mensagem("conclusão", "HDMI"))
        self.monitor_thread_hdmi.start()

    '''def Executar_TesteAC_bat(self):
        segundos_ac = self.spinBox_AC_segundos.value()
        self.ac_test = ACTest(self.RELATORIO_PATH, segundos_ac)
        threading.Thread(target=self.ac_test.executar_ac).start()
        self.monitor_thread_ac = MonitorThread(self.RELATORIO_PATH, "PowerHub/AC")
        self.monitor_thread_ac.loop_concluido.connect(lambda: self.ac_test.exibir_mensagem("conclusão", "AC"))
        self.monitor_thread_ac.start()'''


    def Executar_TesteTouch_bat(self):
        Diretorio_Executavel_Touch = self.Label_Diretorio_EXE_Touch.text()
        if not Diretorio_Executavel_Touch:
            self.exibir_mensagem("erro", "Diretório de executável do Touch está vazio.")
            return
        loop_Touch = self.Box_Valordeloop_Touch.value()
        self.touch_test = TouchTest(self.RELATORIO_PATH, Diretorio_Executavel_Touch, loop_Touch)
        threading.Thread(target=self.touch_test.executar_touch_emulator).start()
        self.monitor_thread_touch = MonitorThread(self.RELATORIO_PATH, "TouchEmulator")
        self.monitor_thread_touch.loop_concluido.connect(lambda: self.touch_test.exibir_mensagem("conclusão", "TouchEmulator"))
        self.monitor_thread_touch.start()

    def Executar_TesteTecladoScan_bat(self):
        Diretorio_Executavel_TecladoScan = self.Label_Diretorio_EXE_TecladoScan.text()
        if not Diretorio_Executavel_TecladoScan:
            self.exibir_mensagem("erro", "Diretório de executável do KeyboardScan está vazio.")
            return
        loop_TecladoScan = self.Box_Valordeloop_TecladoScan.value()
        self.keyboardscan_test = KeyboardScanTest(self.RELATORIO_PATH, Diretorio_Executavel_TecladoScan, loop_TecladoScan)
        threading.Thread(target=self.keyboardscan_test.executar_tecladoscan_emulator).start()
        self.monitor_thread_teclado = MonitorThread(self.RELATORIO_PATH, "KeyboardScan")
        self.monitor_thread_teclado.loop_concluido.connect(lambda: self.keyboardscan_test.exibir_mensagem("conclusão", "KeyboardScan"))
        self.monitor_thread_teclado.start()

    def MudarDiretorio_da_Saida(self):
        diretorio = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída")
        if diretorio:
            # Define o novo caminho de saída, incluindo a pasta "RotinadeTestes"
            self.RELATORIO_PATH = os.path.join(diretorio, "RotinadeTestes")
            
            # Cria a pasta "RotinadeTestes" se ela não existir
            if not os.path.exists(self.RELATORIO_PATH):
                os.makedirs(self.RELATORIO_PATH)
            
            # Atualiza o texto do Label para refletir o novo caminho
            self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)


    def SelecionarArquivo_Executavel_Touch(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Executável do Touch", "", "Executáveis (*.exe);;Todos os Arquivos (*)")
        if arquivo:
            self.Label_Diretorio_EXE_Touch.setText(arquivo)

    def SelecionarArquivo_Executavel_KeyboardScan(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Executável do Teclado", "", "Executáveis (*.exe);;Todos os Arquivos (*)")
        if arquivo:
            self.Label_Diretorio_EXE_TecladoScan.setText(arquivo)

    def Resetar(self):
        # Limpar diretórios selecionados
        self.Label_Diretorio_EXE_Touch.clear()
        self.Label_Diretorio_EXE_TecladoScan.clear()
        
        # Resetar valores dos spinBoxes
        #self.spinBox_AC_segundos.setValue(5)
        self.spinBox_HDMI_segundos.setValue(5)
        self.spinBox_Fan_segundos.setValue(5)
        self.spinBox_LID_segundos.setValue(5)
        self.spinBox_ServoMotor_AnguloDesejado.setValue(0)
        self.spinBox_ServoMotor_segundos.setValue(5)
        
        # Resetar índices dos comboBoxes
        self.QComboBox_ServoMotor_ID.setCurrentIndex(0)
        self.QComboBox_ServoMotor_Direcao.setCurrentIndex(0)
        
        # Limpar campos de texto
        self.Box_Valordeloop_Touch.setValue(1)
        self.Box_Valordeloop_TecladoScan.setValue(1)
        
        # Setar diretório padrão de salvamento
        self.RELATORIO_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "RotinadeTestes")
        self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)


    def exibir_mensagem(self, tipo, mensagem):
        msg = QMessageBox()
        if tipo == "erro":
            msg.setIcon(QMessageBox.Icon.Critical)
        elif tipo == "info":
            msg.setIcon(QMessageBox.Icon.Information)
        elif tipo == "aviso":
            msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(mensagem)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
