from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ====== KONFIGURASI ======
DELAY = 1.0       # jeda antar aksi
JEDA_AWAL = 3     # jeda awal sebelum mulai
ULANG = 5         # jumlah usaha per batch
BATCH = 2         # jumlah batch

SUMBER = "PL-KUMKM 2023"
CATATAN = (
    "tidak mengubah informasi apapun karena tidak diketahui informasi lanjutan terkait usaha ini, sumber datanya juga dari PL-KUMKM 2023"
)

# ====== ATTACH KE BRAVE ======
options = Options()
options.debugger_address = "127.0.0.1:9222"  # Attach ke Brave yang dibuka dengan remote debugging
driver = webdriver.Chrome(options=options)

print(f"✅ Selenium attach ke Brave yang sudah dibuka")
print(f"Script mulai dalam {JEDA_AWAL} detik... Pastikan halaman direktori sudah fokus!")
time.sleep(JEDA_AWAL)

main_tab = driver.current_window_handle  # simpan tab utama

for batch in range(BATCH):
    print(f"=== Mulai batch ke-{batch+1} ===")
    for i in range(ULANG):
        body = driver.find_element(By.TAG_NAME, "body")

        # TAB TAB ENTER ENTER → buka tab baru
        body.send_keys(Keys.TAB)
        body.send_keys(Keys.TAB)
        body.send_keys(Keys.ENTER)
        time.sleep(DELAY)
        body.send_keys(Keys.ENTER)
        time.sleep(DELAY)

        # Tunggu sampai tab baru muncul
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        tabs = driver.window_handles
        new_tab = [h for h in tabs if h != main_tab][0]
        driver.switch_to.window(new_tab)

        # ===== CEK EMAIL =====
        try:
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_value = email_input.get_attribute("value").strip()
            checkbox = driver.find_element(By.ID, "check-email")

            if email_value == "":
                if checkbox.is_selected():
                    checkbox.click()
                    print("❌ Email kosong → checkbox di-uncheck")
                else:
                    print("✅ Email kosong → checkbox sudah kosong")
            else:
                if not checkbox.is_selected():
                    checkbox.click()
                    print(f"☑️ Email terisi ({email_value}) → checkbox dicentang")
                else:
                    print(f"✅ Email terisi ({email_value}) → checkbox sudah dicentang")
        except:
            print("⚠️ Tidak menemukan input email — skip langkah email.")

        # ===== ISI SUMBER & CATATAN =====
        driver.find_element(By.ID, "sumber_profiling").send_keys(SUMBER)
        driver.find_element(By.ID, "catatan_profiling").send_keys(CATATAN)

        # ===== SUBMIT =====
        driver.find_element(By.ID, "submit-final").click()
        time.sleep(DELAY)

        # ENTER untuk konfirmasi (jika ada popup sukses)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ENTER)
        time.sleep(DELAY)

        # ===== TUTUP TAB & KEMBALI KE MAIN =====
        driver.close()
        driver.switch_to.window(main_tab)

        print(f"✅ Profiling ke-{i+1} selesai (batch {batch+1})")
        time.sleep(DELAY)

    print(f"🔄 Batch {batch+1} selesai")
    time.sleep(DELAY + 3)

print("🎉 Semua batch selesai!")
