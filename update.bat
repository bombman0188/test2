@echo off

if "%~1"=="" (
    git reset --hard origin/main
) else (
    git reset --hard origin/%1%
)

if exist requirements.txt (
    python -m pip install -r requirements.txt
)

if exist setup.py (
    python setup.py install
)