from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal, Qt
import subprocess
import os
import sys
import time
import threading
from MainWindow import Ui_MainWindow

class MonitorThread(QThread):
    loop_concluido = pyqtSignal(str)

    def __init__(self, relatorio_path, tipo_teste):
        super().__init__()
        self.relatorio_path = relatorio_path
        self.tipo_teste = tipo_teste

    def run(self):
        while True:
            time.sleep(10)  # Aumenta o tempo de espera para 10 segundos
            done_file = os.path.join(self.relatorio_path, self.tipo_teste, "done.txt")
            print(f"Verificando a existência de: {done_file}")  # Debug
            if os.path.exists(done_file):
                print(f"{done_file} encontrado.")  # Debug
                self.loop_concluido.emit(self.tipo_teste)
                os.remove(done_file)
                break
            else:
                print(f"{done_file} não encontrado.")  # Debug

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(690, 355)
        self.setupUi(self)

        self.RELATORIO_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "RotinadeTestes")
        self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)

        self.Botao_reset.clicked.connect(self.Resetar)
        self.Botao_TesteTouch.clicked.connect(self.Executar_TesteTouch_bat)
        self.Botao_DiretorioTouch.clicked.connect(self.SelecionarArquivo_Executavel_Touch)
        self.Botao_TesteTeclado.clicked.connect(self.Executar_TesteTeclado_bat)
        self.Botao_DiretorioTeclado.clicked.connect(self.SelecionarArquivo_Executavel_Teclado)
        self.Botao_Ativar_AC.clicked.connect(self.Executar_TesteAC_bat)

        self.Botao_DiretorioSalvamento.clicked.connect(self.MudarDiretorio_da_Saida)

    def Executar_TesteAC_bat(self):
        segundos_ac = self.spinBox_AC_segundos.value()
        threading.Thread(target=self.executar_ac_emulator, args=(segundos_ac,)).start()
        self.monitor_thread_ac = MonitorThread(self.RELATORIO_PATH, "AC")
        self.monitor_thread_ac.loop_concluido.connect(lambda: self.exibir_mensagem("conclusão", "AC"))
        self.monitor_thread_ac.start()

    def executar_ac_emulator(self, segundos):
        comando = f'AC_TestedeAtivacao.bat "{self.RELATORIO_PATH}" "{segundos}"'
        try:
            print(f"Executando comando: {comando}")  # Debug
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"Saída: {resultado.stdout}")
        except subprocess.CalledProcessError as e:
            self.exibir_mensagem("erro", f"Erro ao executar o teste AC: {e}\nSaída de erro: {e.stderr}")

    def Executar_TesteTouch_bat(self):
        Diretorio_Executavel_Touch = self.Label_Diretorio_EXE_Touch.text()
        if not Diretorio_Executavel_Touch:
            self.exibir_mensagem("erro", "Diretório de executável do Touch está vazio.")
            return
        loop_Touch = self.Box_Valordeloop_Touch.value()
        threading.Thread(target=self.executar_touch_emulator, args=(Diretorio_Executavel_Touch, loop_Touch)).start()
        self.monitor_thread_touch = MonitorThread(self.RELATORIO_PATH, "TouchEmulator")
        self.monitor_thread_touch.loop_concluido.connect(lambda: self.exibir_mensagem("conclusão", "TouchEmulator"))
        self.monitor_thread_touch.start()

    def executar_touch_emulator(self, executavel, loop):
        comando = f'TouchEmulator_TestenoDiretorio.bat "{self.RELATORIO_PATH}" "{executavel}" "{loop}"'
        try:
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"Saída: {resultado.stdout}")
        except subprocess.CalledProcessError as e:
            self.exibir_mensagem("erro", f"Erro ao executar o teste Touch: {e}\nSaída de erro: {e.stderr}")

    def exibir_mensagem(self, tipo, mensagem):
        msg_box = QMessageBox(self)
        if tipo == "conclusão":
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Concluído")
            msg_box.setInformativeText(f"O loop de testes de(a) {mensagem} foi concluído.")
        elif tipo == "erro":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Erro")
            msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Mensagem")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def MudarDiretorio_da_Saida(self):
        novo_diretorio = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Salvamento", os.path.expanduser("~"))
        if novo_diretorio:
            caminho_completo = os.path.join(novo_diretorio, "RotinadeTestes")
            self.RELATORIO_PATH = caminho_completo
            if not os.path.exists(caminho_completo):
                os.makedirs(caminho_completo)
            self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)

    def Resetar(self):
        self.Label_Diretorio_EXE_Touch.setText("")
        self.Box_Valordeloop_Touch.setValue(1)
        self.Label_Diretorio_EXE_Teclado.setText("")
        self.Box_Valordeloop_Teclado.setValue(1)
        self.RELATORIO_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "RotinadeTestes")
        self.Label_Diretorio_Salvamento.setText(self.RELATORIO_PATH)

    def Executar_TesteTeclado_bat(self):
        Diretorio_Executavel_Teclado = self.Label_Diretorio_EXE_Teclado.text()
        if not Diretorio_Executavel_Teclado:
            self.exibir_mensagem("erro", "Diretório de executável do Teclado está vazio.")
            return
        loop_Teclado = self.Box_Valordeloop_Teclado.value()
        threading.Thread(target=self.executar_teclado_emulator, args=(Diretorio_Executavel_Teclado, loop_Teclado)).start()
        self.monitor_thread_teclado = MonitorThread(self.RELATORIO_PATH, "Teclado")
        self.monitor_thread_teclado.loop_concluido.connect(lambda: self.exibir_mensagem("conclusão", "Teclado"))
        self.monitor_thread_teclado.start()

    def executar_teclado_emulator(self, executavel, loop):
        comando = f'Keyboard_TestenoDiretorio.bat "{self.RELATORIO_PATH}" "{executavel}" "{loop}"'
        try:
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"Saída: {resultado.stdout}")
        except subprocess.CalledProcessError as e:
            self.exibir_mensagem("erro", f"Erro ao executar o teste Teclado: {e}\nSaída de erro: {e.stderr}")

    def SelecionarArquivo_Executavel_Touch(self):
        diretorio_inicial = os.path.expanduser("~")
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar executável", diretorio_inicial, "Executáveis (*.exe)")
        if arquivo:
            self.Label_Diretorio_EXE_Touch.setText(arquivo)

    def SelecionarArquivo_Executavel_Teclado(self):
        diretorio_inicial = os.path.expanduser("~")
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar executável", diretorio_inicial, "Executáveis (*.exe)")
        if arquivo:
            self.Label_Diretorio_EXE_Teclado.setText(arquivo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
