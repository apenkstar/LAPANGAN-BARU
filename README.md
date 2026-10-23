# Kas Lapangan (APK)

Aplikasi pencatatan kas lapangan. Data tersimpan di HP, tanpa internet.

## Cara mendapat APK
1. Buat repo baru di github.com (gratis), misalnya `kas-lapangan`.
2. Unggah semua isi folder ini ke repo (termasuk folder `.github`), cabang `main`.
3. Buka tab **Actions**. Build jalan otomatis, tunggu sekitar 5-8 menit sampai centang hijau.
4. Buka tab **Releases** di halaman repo, unduh `kas-lapangan.apk`.
5. Buka file itu di HP. Kalau diminta, izinkan "Instal dari sumber ini" untuk browser kamu.

## Memperbarui aplikasi
Ganti isi `www/index.html` di repo. Build baru jalan otomatis dan muncul di Releases.
Pasang APK baru di atas yang lama (jangan dicopot), data kas tetap aman karena kunci tanda tangan sama.

## Cadangan data
Tombol **Cadangan** di pojok atas aplikasi menyalin seluruh data sebagai teks. Simpan teks itu di tempat aman.
Untuk memulihkan di HP baru, tempel teksnya di kotak yang sama lalu ketuk **Pulihkan**.
