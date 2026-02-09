@echo off
IF NOT EXIST venv (
c:\python310\python -m venv venv
) ELSE (
echo venv folder already exists, skipping creation...
)
call .\venv\Scripts\activate.bat
set PIP="venv\Scripts\pip.exe"
set PYTHON="venv\Scripts\Python.exe"
echo venv %PYTHON%
python cek_file.py
pause
