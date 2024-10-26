@echo off
setlocal EnableDelayedExpansion

REM Cria o arquivo keyboard.json com o conteúdo apropriado
echo { > keyboard.json
echo "cmd": "all_keys", >> keyboard.json
echo "keyboard_matrix": [ >> keyboard.json
echo {"ksi": 0, "kso": 3, "fn": 1}, >> keyboard.json
echo {"ksi": 0, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 1, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 0, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 0, "kso": 12, "fn": 0}, >> keyboard.json
echo {"ksi": 0, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 14, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 14, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 12, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 12, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 11, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 10, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 10, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 11, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 9, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 1, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 14, "fn": 0}, >> keyboard.json
echo {"ksi": 5, "kso": 13, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 13, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 12, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 8, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 10, "fn": 0}, >> keyboard.json
echo {"ksi": 6, "kso": 4, "fn": 0}, >> keyboard.json
echo {"ksi": 6, "kso": 9, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 1, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 14, "fn": 0}, >> keyboard.json
echo {"ksi": 2, "kso": 13, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 13, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 6, "kso": 12, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 10, "fn": 0}, >> keyboard.json
echo {"ksi": 3, "kso": 4, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 11, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 11, "fn": 0}, >> keyboard.json
echo {"ksi": 1, "kso": 1, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 3, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 1, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 2, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 0, "kso": 0, "fn": 0}, >> keyboard.json
echo {"ksi": 0, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 16, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 15, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 14, "fn": 0}, >> keyboard.json
echo {"ksi": 4, "kso": 13, "fn": 0}, >> keyboard.json
echo ] >> keyboard.json
echo } >> keyboard.json

REM Variável para contar as iterações
set contador=1

REM Variáveis para contar o número de "PASS" e "FAIL"
set passCount=0
set failCount=0

REM Caminhos para salvar o relatório na Área de Trabalho do usuário
set USERPROFILE=%USERPROFILE%
REM Caminho passado como argumento
set RELATORIO_PATH=%~1  
REM Remove espaços em branco
set RELATORIO_PATH=%RELATORIO_PATH: =%
REM Caminho do executável passado como argumento
set EXECUTAVEL_EXE_PATH=%~2  
REM Número de loops passado como argumento
set LOOP_COUNT=%~3  

REM Verifica se o app.py existe no mesmo diretório que o arquivo .bat
set APP_PATH=%~dp0app.py

REM Cria a pasta para relatórios, se não existir
if not exist "%RELATORIO_PATH%\Teclado" (
    mkdir "%RELATORIO_PATH%\Teclado"
)

REM Verifica se o arquivo Relatório de Testes.txt e Relatório de Testes.csv já existem, e incrementa o número se necessário
set RELATORIO_TXT=%RELATORIO_PATH%\Teclado\Relatorio de Testes.txt
set RELATORIO_CSV=%RELATORIO_PATH%\Teclado\Relatorio de Testes.csv
set num=0
:checkfile
if exist "%RELATORIO_TXT%" (
    set /a num+=1
    set RELATORIO_TXT=%RELATORIO_PATH%\Teclado\Relatorio de Testes - !num!.txt
    set RELATORIO_CSV=%RELATORIO_PATH%\Teclado\Relatorio de Testes - !num!.csv
    goto checkfile
)

REM Verifica se o executável existe
if not exist "%EXECUTAVEL_EXE_PATH%" (
    MSG * O executável não foi encontrado!
    exit /b
)

REM Verifica se o app.py existe no diretório atual
if not exist "%APP_PATH%" (
    MSG * O arquivo app.py não foi encontrado!
    exit /b
)

REM Iniciar o loop para as iterações especificadas
:loop

REM Captura o horário atual
for /F "tokens=1-5 delims=:. " %%A in ("%time%") do set HORARIO=%%A:%%B:%%C

echo Iniciando iteracao !contador! as %date% %HORARIO%

REM Executa o executável com caminho completo usando PowerShell e Start-Process
REM Executa o executável com prioridade máxima e força o primeiro plano
powershell -Command "Start-Process '%EXECUTAVEL_EXE_PATH%'"

REM Aguarda 3 segundos e inicia o app.py em segundo plano e envia o argumento/comando
waitfor /t 3 MySignal 2>nul

REM Executa o app.exe com o arquivo JSON gerado, usando Start-Process no PowerShell
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m touch_emulator --device te-001 -c touch.json'"

REM Espera o primeiro executável terminar
waitfor /T 15 MySignal 2>nul

REM Após o término do primeiro executável, aguarda 2 segundos para garantir a geração do log
waitfor /t 2 MySignal 2>nul

REM Caminho do log baseado no diretório do executável
set LOG_PATH=%~dp2ITPM_KeyboardTest.LOG

REM Verifica se o log foi gerado
if exist "%LOG_PATH%" (
    echo Verificando o log...

    REM Lê o resultado nas primeiras 2 linhas
    set RESULT=Indeterminado
    for /f "tokens=1 delims=:" %%i in ('findstr /N /C:"PASS" "%LOG_PATH%"') do (
        if %%i LEQ 2 (
            set RESULT=Pass
            set /a passCount+=1
            echo Passou...
            goto resultado
        )
    )
    for /f "tokens=1 delims=:" %%i in ('findstr /N /C:"FAIL" "%LOG_PATH%"') do (
        if %%i LEQ 2 (
            set RESULT=Fail
            set /a failCount+=1
            echo Falhou...
            goto resultado
        )
    )
) else (
    echo Log nao encontrado! 
    echo Falhou...
    set RESULT=Fail
    set /a failCount+=1
)

:resultado
REM Registra o número da iteração, o horário e o resultado no Relatório de Testes.txt
echo Iteração !contador! - Data: %date% - Horário: %HORARIO% - Resultado: !RESULT! >> "%RELATORIO_TXT%"

REM Adiciona a iteração, horário e resultado ao arquivo CSV
if not exist "%RELATORIO_CSV%" (
    REM Cria o cabeçalho do arquivo CSV
    echo Iteracao,Horario,Resultado > "%RELATORIO_CSV%"
)
echo !contador!,!HORARIO!,!RESULT! >> "%RELATORIO_CSV%"

REM Fecha o processo se houver falha usando taskkill via PowerShell
if "!RESULT!"=="Fail" (
    powershell -Command "Stop-Process -Name '%~n2' -Force"
    REM echo Processo terminado devido a falha >> "%DEBUG_PATH%"
)

REM Incrementa o contador
set /a contador+=1

REM Verifica se já alcançou 1000 iterações
if !contador! LEQ %LOOP_COUNT% goto loop

REM Exibe e registra a contagem de "PASS" e "FAIL" ao final do loop
echo. >> "%RELATORIO_TXT%"
echo Total de PASS: !passCount! >> "%RELATORIO_TXT%"
echo Total de FAIL: !failCount! >> "%RELATORIO_TXT%"
echo. >> "%RELATORIO_CSV%"
echo Total de PASS,!passCount! >> "%RELATORIO_CSV%"
echo Total de FAIL,!failCount! >> "%RELATORIO_CSV%"

REM Exibe as contagens no prompt
echo Total de PASS: !passCount!
echo Total de FAIL: !failCount!

REM Fim do script
echo Testes concluidos.
REM Criar um arquivo para sinalizar a conclusão do loop
echo Teste concluído > "%RELATORIO_PATH%\Teclado\done.txt"
pause
exit