# keyboard_test.py
import subprocess
import threading
import os
from PyQt6.QtWidgets import QMessageBox

class KeyboardTest:
    def __init__(self, relatorio_path, executavel_teclado, loop_teclado):
        self.relatorio_path = relatorio_path
        self.executavel_teclado = executavel_teclado
        self.loop_teclado = loop_teclado

    def executar_teclado_emulator(self):
        comando = f'Keyboard_TestenoDiretorio.bat "{self.relatorio_path}" "{self.executavel_teclado}" "{self.loop_teclado}"'
        try:
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print(f"Saída: {resultado.stdout}")
        except subprocess.CalledProcessError as e:
            self.exibir_mensagem("erro", f"Erro ao executar o teste Teclado: {e}\nSaída de erro: {e.stderr}")

    def exibir_mensagem(self, tipo, mensagem):
        msg_box = QMessageBox()
        if tipo == "conclusão":
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Concluído")
            msg_box.setInformativeText(f"O teste de Teclado foi concluído.")
        elif tipo == "erro":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Erro")
            msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Mensagem")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
