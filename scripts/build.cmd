@echo off
call venv\Scripts\activate.bat
py setup.py bdist_wheel

rmdir /S /Q build
rmdir /S /Q dat_terminal.egg-info

cd ..\dat-terminal-test
call venv\Scripts\activate.bat
pip install ..\dat-terminal\dist\dat_terminal-0.1-py3-none-any.whl