@echo off
setlocal EnableDelayedExpansion

REM Caminhos para salvar o relatório na Área de Trabalho do usuário
set USERPROFILE=%USERPROFILE%

REM Caminho passado como argumento (o diretório de saída)
set RELATORIO_PATH=%~1  

REM Remove espaços em branco do caminho
set RELATORIO_PATH=%RELATORIO_PATH: =%

REM Verifica se o app.exe existe no mesmo diretório que o arquivo .bat
set APP_PATH=%~dp0app.exe

REM Verifica se o app.exe existe no diretório atual
if not exist "%APP_PATH%" (
    echo O arquivo app.exe não foi encontrado no caminho: %APP_PATH%
    MSG * O arquivo app.exe não foi encontrado!
    exit /b
)

REM Cria a pasta para relatórios, se não existir
if not exist "%RELATORIO_PATH%\PowerHub\FAN" (
    mkdir "%RELATORIO_PATH%\PowerHub\FAN"
    echo Pasta FAN criada em "%RELATORIO_PATH%\PowerHub\FAN".
) else (
    echo A pasta FAN já existe.
)

REM Verifica se os arquivos Relatório de Testes.txt e Relatório de Testes.csv já existem, e incrementa o número se necessário
set RELATORIO_TXT=%RELATORIO_PATH%\PowerHub\FAN\Relatorio de Testes.txt
set RELATORIO_CSV=%RELATORIO_PATH%\PowerHub\FAN\Relatorio de Testes.csv
set num=0

:checkfile
if exist "%RELATORIO_TXT%" (
    set /a num+=1
    set RELATORIO_TXT=%RELATORIO_PATH%\PowerHub\FAN\Relatorio de Testes - !num!.txt
    set RELATORIO_CSV=%RELATORIO_PATH%\PowerHub\FAN\Relatorio de Testes - !num!.csv
    goto checkfile
)

REM Captura o horário atual
for /F "tokens=1-5 delims=:. " %%A in ("%time%") do set HORARIO=%%A:%%B:%%C

REM Inicializa contador
set /a contador=1

echo Iniciando iteracao !contador! as %date% %HORARIO% >> "%RELATORIO_TXT%"
echo Iniciando iteracao !contador! as %date% %HORARIO% >> "%RELATORIO_CSV%"
echo Data,Hora,Status,Duração >> "%RELATORIO_CSV%"  REM Cabeçalho do CSV

REM Verifica se o usuário passou o argumento de quantos segundos o Switch AC ficará ativado
set SEGUNDOS=%~2

REM Executa o app.exe com o comando para ativar o Switch de Energia AC
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m power_hub --action post -c switch -s fan 1'"

REM Aguarda o número de segundos fornecido (ou o padrão)
echo Switch FAN ativado por %SEGUNDOS% segundos... >> "%RELATORIO_TXT%"
echo Switch FAN ativado por %SEGUNDOS% segundos... >> "%RELATORIO_CSV%"
waitfor /t %SEGUNDOS% MySignal 2>nul

REM Comando para desligar o Switch de Energia AC
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m power_hub --action post -c switch -s fan 0'"
echo Switch FAN desativado após %SEGUNDOS% segundos. >> "%RELATORIO_TXT%"
echo Switch FAN desativado após %SEGUNDOS% segundos. >> "%RELATORIO_CSV%"
echo %date%,%HORARIO%,Desativado,%SEGUNDOS% >> "%RELATORIO_CSV%"  REM Registro no CSV

REM Fim do script
echo Testes concluídos. >> "%RELATORIO_TXT%"
echo Criando done.txt em "%RELATORIO_PATH%\PowerHub\FAN".
echo Teste concluído > "%RELATORIO_PATH%\PowerHub\FAN\done.txt"

if exist "%RELATORIO_PATH%\PowerHub\FAN\done.txt" (
    echo Arquivo done.txt criado com sucesso.
) else (
    echo Erro: Arquivo done.txt não foi criado.
)

pause
exit