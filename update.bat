@echo on

if "%1"=="" (
    echo main branch
    git reset --hard origin/main
) else (
    echo %1% branch
    git reset --hard origin/%1%
)

if exist requirements.txt (
    python -m pip install -r requirements.txt
)

if exist setup.py (
    python setup.py install
)