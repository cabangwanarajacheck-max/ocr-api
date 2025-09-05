@echo off
echo 🚀 Starting OCR API...

REM masuk ke folder project
cd /d C:\Users\someo\ocr-api

REM aktifkan virtualenv
call venv\Scripts\activate

REM buka Flask API di jendela terpisah
start cmd /k "python app.py"

REM tunggu sebentar biar Flask jalan dulu
timeout /t 5 >nul

REM buka ngrok di jendela terpisah
start cmd /k "ngrok http 5000"

echo ✅ OCR API and ngrok started!
pause
