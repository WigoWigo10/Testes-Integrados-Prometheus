@echo off
set /p SEGUNDOS=Digite o valor em segundos: 
set APP_PATH=%~dp0app.exe
powershell -Command "Start-Process '%APP_PATH%' -ArgumentList '-m power_hub --action post -c switch -s lid 1 -lid %SEGUNDOS%'"

