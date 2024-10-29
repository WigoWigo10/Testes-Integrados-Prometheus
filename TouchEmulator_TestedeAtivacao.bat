@echo off
setlocal EnableDelayedExpansion

REM Cria o arquivo touch.json com o conteúdo apropriado
echo { > touch.json
echo "cmd": "touch", >> touch.json
echo "touch_interval": 100, >> touch.json
echo "delay":200, >> touch.json
echo "sequence": [ >> touch.json
echo {"touch_type": "single"}, >> touch.json
echo {"touch_type": "double"} >> touch.json
echo ] >> touch.json
echo } >> touch.json

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

REM Verifica se o app.exe existe no mesmo diretório que o arquivo .bat
set APP_PATH=%~dp0app.exe

REM Cria a pasta para relatórios, se não existir
if not exist "%RELATORIO_PATH%\TouchEmulator" (
    mkdir "%RELATORIO_PATH%\TouchEmulator"
)

REM Verifica se o arquivo Relatório de Testes.txt e Relatório de Testes.csv já existem, e incrementa o número se necessário
set RELATORIO_TXT=%RELATORIO_PATH%\TouchEmulator\Relatorio de Testes.txt
set RELATORIO_CSV=%RELATORIO_PATH%\TouchEmulator\Relatorio de Testes.csv
set num=0
:checkfile
if exist "%RELATORIO_TXT%" (
    set /a num+=1
    set RELATORIO_TXT=%RELATORIO_PATH%\TouchEmulator\Relatorio de Testes - !num!.txt
    set RELATORIO_CSV=%RELATORIO_PATH%\TouchEmulator\Relatorio de Testes - !num!.csv
    goto checkfile
)

REM Cria o arquivo debug_touch.txt para registrar informações detalhadas de debug
REM set DEBUG_PATH=%RELATORIO_PATH%\Touch\debug_touch.txt
REM echo Criando arquivo de debug: %DEBUG_PATH%
REM echo Início do script - Data: %date% Hora: %time% > "%DEBUG_PATH%"

REM Verifica se o executável existe
if not exist "%EXECUTAVEL_EXE_PATH%" (
    REM echo O executável não foi encontrado! >> "%DEBUG_PATH%"
    echo * O executavel nao foi encontrado!
    exit /b
)

REM Verifica se o app.exe existe no diretório atual
if not exist "%APP_PATH%" (
    REM echo O arquivo app.exe não foi encontrado! >> "%DEBUG_PATH%"
    echo * O arquivo app.exe não foi encontrado!
    exit /b
)

REM Iniciar o loop para as iterações especificadas
:loop

REM Captura o horário atual
for /F "tokens=1-5 delims=:. " %%A in ("%time%") do set HORARIO=%%A:%%B:%%C

echo Iniciando iteracao !contador! as %date% %HORARIO%
REM echo Iteração !contador! iniciada em %date% %HORARIO% >> "%DEBUG_PATH%"

REM Executa o executável com caminho completo usando PowerShell e Start-Process
powershell -Command "Start-Process '%EXECUTAVEL_EXE_PATH%'"
REM echo Executável iniciado: %EXECUTAVEL_EXE_PATH% >> "%DEBUG_PATH%"

REM Aguarda 2 segundos e inicia o app.exe em segundo plano com argumentos/comando
waitfor /t 2 MySignal4 2>nul
REM echo Timeout de 3 segundos concluído >> "%DEBUG_PATH%"

REM Executa o app.exe com o arquivo JSON gerado, usando Start-Process no PowerShell
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m touch_emulator --device te-001 -c touch.json'"
REM echo app.exe iniciado com touch.json >> "%DEBUG_PATH%"

REM Espera o primeiro executável terminar
waitfor /T 3 MySignal5 2>nul
REM echo Comando waitfor executado >> "%DEBUG_PATH%"

REM Após o término do primeiro executável, aguarda 2 segundos para garantir a geração do log
waitfor /t 2 MySignal6 2>nul
REM echo Timeout de 2 segundos após app.exe concluído >> "%DEBUG_PATH%"

REM Caminho do log baseado no diretório do executável
set LOG_PATH=%~dp2ITPM_TouchpadTest.LOG

REM Verifica se o log foi gerado
if exist "%LOG_PATH%" (
    REM echo Log encontrado: %LOG_PATH% >> "%DEBUG_PATH%"
    echo Verificando o log...

    REM Lê o resultado nas primeiras 2 linhas
    set RESULT=Indeterminado
    for /f "tokens=1 delims=:" %%i in ('findstr /N /C:"PASS" "%LOG_PATH%"') do (
        if %%i LEQ 2 (
            set RESULT=Pass
            set /a passCount+=1
            echo Passou...
            REM echo Resultado da iteração !contador!: PASS >> "%DEBUG_PATH%"
            goto resultado
        )
    )
    for /f "tokens=1 delims=:" %%i in ('findstr /N /C:"FAIL" "%LOG_PATH%"') do (
        if %%i LEQ 2 (
            set RESULT=Fail
            set /a failCount+=1
            echo Falhou...
            REM echo Resultado da iteração !contador!: FAIL >> "%DEBUG_PATH%"
            goto resultado
        )
    )
) else (
    REM echo Log nao encontrado! >> "%DEBUG_PATH%"
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

REM Verifica se já alcançou o número máximo de iterações
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

REM Registra a conclusão no arquivo de debug
REM echo Script concluído com %passCount% PASS e %failCount% FAIL >> "%DEBUG_PATH%"

REM Fim do script
echo Testes concluidos.
REM Criar um arquivo para sinalizar a conclusão do loop
echo Teste concluído > "%RELATORIO_PATH%\TouchEmulator\done.txt"
pause
exit
