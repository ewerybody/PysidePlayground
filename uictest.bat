@echo off
set file_arg=%1%
@REM  set uic=C:\Python38\Lib\site-packages\PySide2\uic.exe
set uic=./.venv/Lib/site-packages/PySide6/uic.exe

echo file_arg: %file_arg%

if not exist %file_arg% (
    echo no input file!!!
    pause
    exit
)

%uic% -g python %file_arg% -o uictest_compiled.py
pause
