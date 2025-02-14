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

REM Cria o arquivo de debug
set DEBUG_FILE=%RELATORIO_PATH%\PowerHub\LID\debug.txt
echo --- Início do Log de Debug --- > "%DEBUG_FILE%"
echo Caminho do relatório: %RELATORIO_PATH% >> "%DEBUG_FILE%"
echo Caminho do app: %APP_PATH% >> "%DEBUG_FILE%"

REM Verifica se o app.exe existe no diretório atual
if not exist "%APP_PATH%" (
    echo O arquivo app.exe não foi encontrado no caminho: %APP_PATH% >> "%DEBUG_FILE%"
    exit /b
) else (
    echo O arquivo app.exe foi encontrado. >> "%DEBUG_FILE%"
)

REM Cria a pasta para relatórios, se não existir
if not exist "%RELATORIO_PATH%\PowerHub\LID" (
    mkdir "%RELATORIO_PATH%\PowerHub\LID"
    echo Pasta LID criada em "%RELATORIO_PATH%\PowerHub\LID". >> "%DEBUG_FILE%"
) else (
    echo A pasta LID já existe. >> "%DEBUG_FILE%"
)

REM Verifica se os arquivos Relatório de Testes.txt e Relatório de Testes.csv já existem, e incrementa o número se necessário
set RELATORIO_TXT=%RELATORIO_PATH%\PowerHub\LID\Relatorio de Testes.txt
set RELATORIO_CSV=%RELATORIO_PATH%\PowerHub\LID\Relatorio de Testes.csv
set num=0

:checkfile
if exist "%RELATORIO_TXT%" (
    set /a num+=1
    set RELATORIO_TXT=%RELATORIO_PATH%\PowerHub\LID\Relatorio de Testes - !num!.txt
    set RELATORIO_CSV=%RELATORIO_PATH%\PowerHub\LID\Relatorio de Testes - !num!.csv
    goto checkfile
)

REM Captura o horário atual
for /F "tokens=1-5 delims=:. " %%A in ("%time%") do set HORARIO=%%A:%%B:%%C

REM Inicializa contador
set /a contador=1

echo Iniciando iteracao !contador! as %date% %HORARIO% >> "%RELATORIO_TXT%"
echo Iniciando iteracao !contador! as %date% %HORARIO% >> "%RELATORIO_CSV%"
echo Data,Hora,Status,Duracao >> "%RELATORIO_CSV%"  REM Cabeçalho do CSV

REM Verifica se o usuário passou o argumento de quantos segundos o Switch LID ficará ativado
set SEGUNDOS=%~2

REM Verifica se SEGUNDOS é um número inteiro
echo Verificando o valor de SEGUNDOS: %SEGUNDOS% >> "%DEBUG_FILE%"
set "VAR_TYPE=Desconhecido"
set /a test=%SEGUNDOS% 2>nul
if "!test!"=="%SEGUNDOS%" (
    set "VAR_TYPE=Inteiro"
) else (
    set "VAR_TYPE=Não é um número inteiro"
)
echo Tipo da variável SEGUNDOS: %VAR_TYPE% >> "%DEBUG_FILE%"

set /a SEGUNDOS=%SEGUNDOS%*1000

REM Executa o app.exe com o comando para ativar o Switch de Energia LID
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m power_hub --action post -c switch -s lid 1 -lid %SEGUNDOS%'"
echo Executando o comando para ativar o Switch LID... >> "%DEBUG_FILE%"

REM Aguarda o número de segundos fornecido (ou o padrão)
echo Switch LID ativado por %SEGUNDOS% segundos... >> "%RELATORIO_TXT%"
echo Switch LID ativado por %SEGUNDOS% segundos... >> "%RELATORIO_CSV%"
waitfor /t %SEGUNDOS% MySignal10 2>nul

REM Comando para desligar o Switch de Energia LID
echo Switch LID desativado após %SEGUNDOS% segundos. >> "%RELATORIO_TXT%"
echo Switch LID desativado após %SEGUNDOS% segundos. >> "%RELATORIO_CSV%"
echo %date%,%HORARIO%,Desativado,%SEGUNDOS% >> "%RELATORIO_CSV%"  REM Registro no CSV

REM Fim do script
echo Testes concluidos. >> "%DEBUG_FILE%"
echo Criando done.txt em "%RELATORIO_PATH%\PowerHub\LID". >> "%DEBUG_FILE%"
echo Teste concluído > "%RELATORIO_PATH%\PowerHub\LID\done.txt"

if exist "%RELATORIO_PATH%\PowerHub\LID\done.txt" (
    echo Arquivo done.txt criado com sucesso. >> "%DEBUG_FILE%"
) else (
    echo Erro: Arquivo done.txt não foi criado. >> "%DEBUG_FILE%"
)

pause
exit
