Aplikasi Prediksi Kelulusan Sederhana Menggunakan Algoritma KNN

Project ini dibuat degan menggunakan Docker Container Manager untuk menjalankan aplikasi Flask.

Pra-syarat:
- Pastikan sistem Anda telah memiliki Docker terpasang sebelum melanjutkan. Anda dapat mengunduh dan menginstal Docker dari situs resmi mereka: https://www.docker.com/

Langkah-langkah:

1. Klon repositori ini:
   - Gunakan perintah `git clone <URL repositori>` untuk mengklon repositori.

2. Pindah ke direktori proyek:
   - Gunakan perintah `cd docker-flask-project` untuk pindah ke direktori proyek.

3. Bangun dan jalankan kontainer Docker:
   - Gunakan perintah `docker-compose up --build` untuk membangun dan menjalankan kontainer Docker.
   - Perintah di atas akan membangun kontainer Docker dan menjalankan aplikasi Flask di dalamnya. Jika ini adalah pertama kalinya Anda menjalankan perintah ini, Docker akan mengunduh dan membangun gambar Docker yang diperlukan terlebih dahulu.

4. Akses aplikasi:
   - Setelah perintah `docker-compose up` berhasil dijalankan, aplikasi Flask dapat diakses melalui browser web di http://localhost:5000.

5. Berhenti menjalankan kontainer:
   - Untuk menghentikan kontainer Docker yang sedang berjalan, cukup tekan `Ctrl+C` di terminal tempat Anda menjalankan perintah `docker-compose up`.
   - Jika Anda ingin menghapus kontainer yang berjalan, gunakan perintah `docker-compose down`.

Aplikasi ini juga dapat dijalankan langsung dengan running file `app.py` jangan lupa untuk menginstall library dalam file `requirements.txt` dengan menjalankan perintah `pip install -r app/requirements.txt`

Kontribusi:
- Jika Anda ingin berkontribusi pada proyek ini, Anda dapat melakukan fork repositori ini, melakukan perubahan yang diinginkan, dan mengajukan pull request ke repositori utama.

Lisensi:
- Proyek ini dilisensikan di bawah MIT License. Silakan lihat berkas LICENSE untuk informasi lebih lanjut.
