@echo off
setlocal EnableDelayedExpansion

REM Cria o arquivo touch.json com o conteúdo apropriado
echo { > touch.json
echo "cmd": "touch", >> touch.json
echo "touch_interval": 250, >> touch.json
echo "delay":750, >> touch.json
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
if not exist "%RELATORIO_PATH%\Touch" (
    mkdir "%RELATORIO_PATH%\Touch"
)

REM Verifica se o arquivo Relatório de Testes.txt e Relatório de Testes.csv já existem, e incrementa o número se necessário
set RELATORIO_TXT=%RELATORIO_PATH%\Touch\Relatorio de Testes.txt
set RELATORIO_CSV=%RELATORIO_PATH%\Touch\Relatorio de Testes.csv
set num=0
:checkfile
if exist "%RELATORIO_TXT%" (
    set /a num+=1
    set RELATORIO_TXT=%RELATORIO_PATH%\Touch\Relatorio de Testes - !num!.txt
    set RELATORIO_CSV=%RELATORIO_PATH%\Touch\Relatorio de Testes - !num!.csv
    goto checkfile
)

REM Verifica se o executável existe
if not exist "%EXECUTAVEL_EXE_PATH%" (
    MSG * O executável não foi encontrado!
    exit /b
)

REM Verifica se o app.exe existe no diretório atual
if not exist "%APP_PATH%" (
    MSG * O arquivo app.exe não foi encontrado!
    exit /b
)

REM Iniciar o loop para as iterações especificadas
:loop

REM Captura o horário atual
for /F "tokens=1-5 delims=:. " %%A in ("%time%") do set HORARIO=%%A:%%B:%%C

echo Iniciando iteracao !contador! as %date% %HORARIO%

REM Executa o executável com caminho completo
start "" "%EXECUTAVEL_EXE_PATH%"

REM Aguarda 3 segundos e inicia o app.exe em segundo plano e envia o argumento/comando
timeout /t 3 /nobreak >nul

REM Executa o app.exe com o arquivo JSON gerado
start "" "%APP_PATH%" -m touch_emulator --device te-001 -c touch.json

REM Espera o primeiro executável terminar
waitfor /T 5 MySignal 2>nul

REM Após o término do primeiro executável, aguarda 2 segundos para garantir a geração do log
timeout /t 2 /nobreak >nul

REM Caminho do log baseado no diretório do executável
set LOG_PATH=%~dp2ITPM_TouchpadTest.LOG

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

REM Fecha o processo se houver falha
if "!RESULT!"=="Fail" (
    taskkill /IM "%~nx2" /F
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

REM Fim do script
echo Testes concluidos.
REM Criar um arquivo para sinalizar a conclusão do loop
echo Teste concluído > "%RELATORIO_PATH%\Touch\done.txt"
pause
exit
