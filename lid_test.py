import subprocess
import threading
import os
from PyQt6.QtWidgets import QMessageBox

class LIDTest:
    def __init__(self, relatorio_path, segundos):
        self.relatorio_path = relatorio_path
        self.segundos = int(segundos)

    def executar_lid(self):
        comando = f'LID_TestedeAtivacao.bat "{self.relatorio_path}" "{self.segundos}"'
        try:
            print(f"Executando comando: {comando}")  # Debug
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"Saída: {resultado.stdout}")
            self.exibir_mensagem()
        #except subprocess.CalledProcessError as e:
            #self.exibir_mensagem("erro", f"Erro ao executar o teste FAN: {e}\nSaída de erro: {e.stderr}")
        except:
            pass

    def exibir_mensagem(self, tipo, mensagem):
        msg_box = QMessageBox()
        #if tipo == "conclusão":
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Concluído")
        msg_box.setInformativeText(f"O teste de LID foi concluído.")
        '''
        elif tipo == "erro":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Erro")
            msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Mensagem")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
        '''
