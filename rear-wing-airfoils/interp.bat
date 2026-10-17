@echo off
set PYTHON_EXECUTABLE=python
set SCRIPT_PATH=%~dp0interp.py

REM Check if a file was drag-and-dropped onto the batch file
if "%~1"=="" (
    REM No file provided, so run the script and ask for input
    %PYTHON_EXECUTABLE% "%SCRIPT_PATH%"
) else (
    REM Use the drag-and-dropped file as input
    %PYTHON_EXECUTABLE% "%SCRIPT_PATH%" "%~1"
)
