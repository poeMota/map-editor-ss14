@echo off

where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not installed
    exit /b 1
)

where pip >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: pip not installed
    exit /b 1
)

git submodule init
git submodule update
pip install -r requirements.txt

