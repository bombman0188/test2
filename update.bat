@echo off
if exist requirements.txt (
    python -m pip install -r requirements.txt
)

if exist setup.py (
    python setup.py install
)