@echo off
title Simulador de Examenes Escolares
cd /d "%~dp0"
echo ==================================================================
echo   SIMULADOR DE EXAMENES ESCOLARES (ESTADISTICA Y NUEVAS MATERIAS)
echo ==================================================================
echo.
echo Iniciando servidor web en http://127.0.0.1:8000 ...
echo Puedes abrir tu navegador en: http://127.0.0.1:8000
echo Presiona Ctrl+C para detener el servidor.
echo.
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause