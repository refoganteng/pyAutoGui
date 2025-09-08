import pyautogui
import time

DELAY = 2  # delay antar langkah
JEDA_AWAL = 5  # waktu buat kamu siap2 sebelum script mulai
ULANG = 81  # jumlah pengulangan per batch

def klik(x, y):
    pyautogui.click(x, y)
    time.sleep(DELAY)

print(f"Script mulai dalam {JEDA_AWAL} detik... Pindah ke layar target dulu!")
time.sleep(JEDA_AWAL)


for i in range(ULANG):  # looping dalam
        time.sleep(DELAY-1)
        klik(1802, 347)
        pyautogui.press('enter')
        time.sleep(DELAY)
        pyautogui.press('enter')

        print(f"✅ Hapus open ke-{i+1} selesai")
    

