@echo off
cd /d %~dp0
set PYTHONPATH=%PYTHONPATH%;%CD%
python -c "from py_scripts.math_ops import square_number; print(f'The square of 5 is: {square_number(5)}')"
