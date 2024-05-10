@echo off
for %%* in (.) do set "CURRENT_FOLDER=%%~n*"
title %CURRENT_FOLDER%
color a
call .venv\Scripts\activate
python main.py
