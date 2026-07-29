@echo off
setlocal
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
  echo Virtual environment not found at .\venv
  echo Create one with: python -m venv venv
  exit /b 1
)

call "venv\Scripts\activate.bat"
python -m pip install -q -r backend\requirements.txt

echo.
echo ========================================
echo  Pearl Mccaffrey - Personal Shopper
echo  Web server starting...
echo  Local:   http://127.0.0.1:8000
echo  Network: http://%COMPUTERNAME%:8000
echo ========================================
echo.

start "" http://127.0.0.1:8000

cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

endlocal
