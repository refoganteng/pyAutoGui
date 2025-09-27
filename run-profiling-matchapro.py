import pyautogui
import time

DELAY = 1.5 
JEDA_AWAL = 5  
ULANG = 50  # jumlah pengulangan per batch
BATCH = 2  # jumlah looping luar

def klik(x, y):
    
    pyautogui.click(x, y)
    time.sleep(DELAY)

def ketik(teks):
    pyautogui.write(teks, interval=0.05)
    time.sleep(DELAY)

def scroll_ke_bawah():
    pyautogui.scroll(-9999)
    time.sleep(DELAY)

def scroll_ke_atas():
    pyautogui.scroll(9999)
    time.sleep(DELAY)

print(f"Script mulai dalam {JEDA_AWAL} detik... Pindah ke layar target dulu!")
time.sleep(JEDA_AWAL)

for batch in range(BATCH):  # looping luar
    print(f"=== Mulai batch ke-{batch+1} ===")

    for i in range(ULANG):  # looping dalam
        time.sleep(DELAY-1)
        pyautogui.press('tab')
        pyautogui.press('tab')      
        pyautogui.press('enter')  
        time.sleep(DELAY)

        pyautogui.press('enter')
        time.sleep(DELAY)
        klik(970, 875)
        time.sleep(DELAY)
        klik(970, 875)  # centang email

        scroll_ke_bawah()
        klik(1044, 855) 
        ketik("-")
        pyautogui.press('tab')
        pyautogui.hotkey('command', 'v')

        scroll_ke_atas()    
        
        klik(1815, 215) #tombol submit
        pyautogui.press('enter') 
        
        time.sleep(DELAY-1)
        pyautogui.press('enter') 
        pyautogui.hotkey('command', 'w')

        print(f"✅ Profilling ke-{i+1} selesai (batch {batch+1})")

    # Aksi tambahan setelah selesai 50 kali (setiap batch)
    scroll_ke_atas()
    klik(1783, 692) #tombol filter
    print(f"🔄 Batch {batch+1} selesai, aksi tambahan sudah dilakukan")
    time.sleep(DELAY+10) 
    



    #   tidak mengubah informasi apapun karena tidak diketahui informasi lanjutan terkait usaha ini
