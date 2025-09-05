import requests
import gspread
from google.oauth2.service_account import Credentials

# --- Konfigurasi Google Sheets ---
SERVICE_ACCOUNT_FILE = "credentials.json"  # ganti sesuai file service account
SPREADSHEET_ID = "16ffHn4H-KDV5m1VvupPh8nHg2Ye7Ft471Tx6cHTWfg4"    # ganti dengan ID Google Sheet
SHEET_NAME = "Config"

# --- Ambil URL ngrok aktif ---
def get_ngrok_url():
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        tunnels = res.get("tunnels", [])
        for t in tunnels:
            if "https" in t["public_url"]:
                return t["public_url"]
    except Exception as e:
        print("❌ Gagal ambil ngrok URL:", e)
    return None

def update_sheet(url):
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

    # Update cell B1
    sheet.update("B1", url)
    print("✅ URL ngrok terbaru disimpan:", url)

if __name__ == "__main__":
    url = get_ngrok_url()
    if url:
        update_sheet(url)
