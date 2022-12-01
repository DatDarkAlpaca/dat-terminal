@echo off
py setup.py bdist_wheel
rmdir /S /Q dat_terminal.egg-info
rmdir /S /Q build

cd ..\dat-terminal-test
.\venv\Scripts\activate.bat
pip install ..\dat-terminal\dist\dat_terminal-0.1-py3-none-any.whl