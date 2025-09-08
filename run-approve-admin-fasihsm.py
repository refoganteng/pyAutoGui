import pyautogui
import time

DELAY = 3  # delay antar langkah (detik)
JEDA_AWAL = 5  # waktu buat kamu siap2 sebelum script mulai
ULANG = 12  # jumlah pengulangan

def klik(x, y):
    pyautogui.click(x, y)
    time.sleep(DELAY)

def ketik(teks):
    pyautogui.write(teks, interval=0.05)
    time.sleep(DELAY)

def scroll_ke_bawah():
    pyautogui.scroll(-9999)

def scroll_ke_atas():
    pyautogui.scroll(9999)
    time.sleep(DELAY)

print(f"Script mulai dalam {JEDA_AWAL} detik... Pindah ke layar target dulu!")
time.sleep(JEDA_AWAL)

for i in range(ULANG):
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.press('enter')
    time.sleep(DELAY)
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    ketik("}")


    scroll_ke_bawah()
    klik(1268, 1000)  # review
    time.sleep(DELAY)

    klik(1811, 211)  # approve
    # time.sleep(DELAY - 2)

    pyautogui.press('enter')
    pyautogui.press('enter')

    pyautogui.hotkey('command', 'w')
    time.sleep(DELAY - 2)

    print(f"✅ Approve ke-{i + 1} selesai")

# Setelah semua selesai
# print("🎉 Semua approve selesai. Menunggu 10 detik sebelum sleep...")f
# time.sleep(10)

# Sleep Mac
# os.system('osascript -e \'tell application "System Events" to sleep\'')       

