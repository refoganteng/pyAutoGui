# pyAutoGui
PyAutoGUI adalah modul Python yang digunakan untuk mengotomatiskan tugas-tugas pada komputer dengan mengontrol mouse dan keyboard secara terprogram. Library ini memungkinkan skrip Python untuk memindahkan kursor mouse, melakukan klik, mengetik teks, menekan tombol, mengambil tangkapan layar, dan bahkan menemukan gambar di layar.

Cara implementasi pada pekerjaan di BPS (contoh: profilling SBR dan approve admin di fasih-sm)

#Step0 - install python dan pip di laptop/PC

#Step1 - Cek Pointer
Lakukan tugas secara manual (kontrol manusia) sambil catat setiap koordinat tombol x dan y nya, run file cekpointer.py di terminal.
Kemudian ubah koordinat2nya di file run-profiling-matchapro.py (ini dilakukan karena resolusi setiap PC/Laptop berbeda2)

#Step2 - Filter di matchapro menu Direktori Usaha (filter yang belum profilling)

#Step3 - Coba run file run-profiling-matchapro.py
Kemudian arahkan mouse ke filter
Cek apakah pointer sudah presisi dan profiling berhasil sampai submit dan tutup tab browser. Kalau belum pas, run cekpointer.py lagi, perbaiki koordinatnya. Lalu coba run lagi.

#Step4 - Pantau proses jalannya skrip di terminal
(Pastikan server BPS sedang sehat dan jaringan internet lancar)

