# keyboard_test.py
import subprocess
import threading
import os
from PyQt6.QtWidgets import QMessageBox

class KeyboardScanTest:
    def __init__(self, relatorio_path, executavel_keyboardscan, loop_keyboardscan):
        self.relatorio_path = relatorio_path
        self.executavel_keyboardscan = executavel_keyboardscan
        self.loop_keyboardscan = loop_keyboardscan
        print(f"DEBUG: Inicializando KeyboardScanTest com relatorio_path={relatorio_path}, executavel_keyboardscan={executavel_keyboardscan}, loop_keyboardscan={loop_keyboardscan}")

    def executar_tecladoscan_emulator(self):
        comando = f'Keyboard_TestedeAtivacao.bat "{self.relatorio_path}" "{self.executavel_keyboardscan}" "{self.loop_keyboardscan}"'
        print(f"DEBUG: Executando comando: {comando}")
        try:
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"DEBUG: Comando executado com sucesso. Saída: {resultado.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"DEBUG: Erro ao executar o comando. Código de retorno: {e.returncode}, Saída de erro: {e.stderr}")
            self.exibir_mensagem("erro", f"Erro ao executar o teste Teclado: {e}\nSaída de erro: {e.stderr}")

    def exibir_mensagem(self, tipo, mensagem):
        print(f"DEBUG: Exibindo mensagem do tipo {tipo}: {mensagem}")
        msg_box = QMessageBox()
        if tipo == "conclusão":
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Concluído")
            msg_box.setInformativeText(f"O teste de KeyboardScan foi concluído.")
        elif tipo == "erro":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Erro")
            msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Mensagem")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
        print(f"DEBUG: Mensagem exibida.")
