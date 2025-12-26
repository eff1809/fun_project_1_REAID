# Mini Career Quiz App

Mini Career Quiz App adalah aplikasi web interaktif berbasis **Streamlit** yang membantu pengguna mengetahui **role IT yang paling cocok** berdasarkan jawaban dari beberapa pertanyaan sederhana.

Aplikasi ini dirancang dengan alur yang jelas, UI sederhana namun informatif, serta memanfaatkan **session state Streamlit** agar pengalaman pengguna tetap konsisten saat berpindah pertanyaan.

---

## Fitur Utama

**Quiz Interaktif**
- Pertanyaan pilihan ganda menggunakan radio button
- Navigasi antar pertanyaan (Sebelumnya & Selanjutnya)
- Validasi agar semua pertanyaan harus dijawab sebelum submit

**Hasil & Visualisasi**
- Menampilkan role IT yang paling sesuai
- Deskripsi singkat untuk setiap role
- Detail skor untuk masing-masing role
- Grafik batang (bar chart) untuk visualisasi skor

**User Experience**
- Progress bar untuk menunjukkan kemajuan quiz
- Teks sambutan acak agar terasa lebih personal
- Efek visual (balloons) setelah quiz selesai
- Tombol **Ulangi Quiz** untuk reset aplikasi

---

## Role yang Tersedia

Aplikasi ini saat ini mendukung 3 role IT:

- **Programmer**  
  Cocok untuk pengguna yang senang dengan logika, coding, dan membangun aplikasi.

- **UI/UX Designer**  
  Cocok untuk pengguna yang peduli dengan tampilan visual dan pengalaman pengguna.

- **Data Scientist**  
  Cocok untuk pengguna yang suka menganalisis data dan mencari insight.

---

## Cara Kerja Aplikasi

1. Pengguna menjawab pertanyaan satu per satu
2. Setiap jawaban dipetakan ke role tertentu
3. Skor dihitung berdasarkan frekuensi jawaban
4. Role dengan skor tertinggi menjadi hasil akhir
5. Jika skor seri, hasil akan menampilkan lebih dari satu role

---

## Teknologi yang Digunakan

- **Python**
- **Streamlit** → Web app interaktif
- **Pandas** → Pengolahan data skor
- **Random** → Menampilkan teks sambutan secara acak



