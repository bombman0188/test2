@echo off

FOR /L %%y IN (0, 0, 1) DO (
	ping 127.0.0.1 -w 1000 -n 2 > NUL
    call update.bat %1%
	python main.py %1%
)

