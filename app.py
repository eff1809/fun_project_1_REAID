# ======================================================
# IMPORT LIBRARY
# ======================================================

import streamlit as st          # Library utama untuk membuat web app interaktif
import pandas as pd             # Digunakan untuk mengolah data skor menjadi tabel/grafik
import random                   # Digunakan untuk menampilkan teks sambutan secara acak


# ======================================================
# DATA QUIZ
# ======================================================

# Daftar role/profesi yang akan menjadi hasil akhir quiz
ROLES = [
    "Programmer",
    "UI/UX Designer",
    "Data Scientist"
]

# Deskripsi singkat untuk setiap role
# Digunakan agar hasil quiz lebih informatif dan terasa personal
ROLE_DESCRIPTIONS = {
    "Programmer": "Kamu suka memecahkan masalah dengan logika dan kode. Cocok membangun aplikasi dan sistem.",
    "UI/UX Designer": "Kamu peduli dengan pengalaman pengguna dan tampilan visual yang nyaman.",
    "Data Scientist": "Kamu senang menganalisis data dan menarik insight dari data."
}

# Daftar pertanyaan quiz
# Penting: Urutan options HARUS sama dengan urutan ROLES
QUESTIONS = [
    {
        "question": "Saat mengerjakan tugas, kamu paling menikmati bagian...",
        "options": [
            "Menulis dan memperbaiki kode program",      # Programmer
            "Mendesain tampilan agar nyaman digunakan", # UI/UX
            "Menganalisis dan mengolah data"             # Data Scientist
        ]
    },
    {
        "question": "Kegiatan yang paling membuatmu betah berjam-jam adalah...",
        "options": [
            "Debugging dan membangun aplikasi",
            "Membuat wireframe dan prototype",
            "Bermain dengan dataset dan grafik"
        ]
    },
    {
        "question": "Dalam tim, kamu paling sering berperan sebagai...",
        "options": [
            "Orang yang mengerjakan logika utama aplikasi",
            "Orang yang mengatur tampilan dan pengalaman pengguna",
            "Orang yang menganalisis data untuk pengambilan keputusan"
        ]
    }
]


# ======================================================
# LOGIKA QUIZ
# ======================================================

def calculate_score(answers):
    """
    Fungsi ini bertugas menghitung skor untuk setiap role
    berdasarkan jawaban user di setiap pertanyaan.
    """

    # Membuat dictionary skor awal
    # Contoh: {"Programmer": 0, "UI/UX Designer": 0, "Data Scientist": 0}
    scores = {role: 0 for role in ROLES}

    # Loop semua jawaban user berdasarkan index pertanyaan
    for idx, answer in enumerate(answers):

        # Pastikan jawaban tidak kosong
        if answer is not None:

            # Cari index pilihan jawaban pada pertanyaan ke-idx
            option_index = QUESTIONS[idx]["options"].index(answer)

            # Mapping index jawaban ke role
            # Contoh: index 0 → Programmer
            role = ROLES[option_index]

            # Tambahkan skor untuk role tersebut
            scores[role] += 1

    # Kembalikan hasil skor dalam bentuk dictionary
    return scores


def get_final_result(scores):
    """
    Fungsi ini menentukan hasil akhir quiz
    berdasarkan skor tertinggi.
    """

    # Ambil nilai skor tertinggi
    max_score = max(scores.values())

    # Ambil semua role yang memiliki skor tertinggi
    top_roles = [
        role for role, score in scores.items()
        if score == max_score
    ]

    # Jika hanya satu role yang paling dominan
    if len(top_roles) == 1:
        return top_roles[0]

    # Jika lebih dari satu role (skor seri)
    else:
        return " & ".join(top_roles)


# ======================================================
# STREAMLIT UI (TAMPILAN & ALUR APLIKASI)
# ======================================================

# ---------- SESSION STATE ----------
# Session state digunakan agar data tidak hilang
# setiap kali user menekan tombol (rerun Streamlit)

# Menyimpan index pertanyaan yang sedang aktif
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Menyimpan jawaban user untuk setiap pertanyaan
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(QUESTIONS)

# Menandai apakah quiz sudah disubmit atau belum
if "submitted" not in st.session_state:
    st.session_state.submitted = False


# ---------- HEADER APLIKASI ----------
st.title("🎯 Mini Career Quiz App")   # Judul utama aplikasi
st.write("Temukan role IT yang paling cocok untukmu!")  # Subjudul/deskripsi singkat

# Daftar teks sambutan untuk meningkatkan UX
greetings = [
    "Siap menemukan passion IT kamu? 🚀",
    "Jawab jujur ya, ini bukan ujian 😄",
    "Yuk cari tahu kamu paling cocok di bidang apa!"
]

# Menampilkan satu teks sambutan secara acak
st.caption(random.choice(greetings))


# ---------- PROGRESS BAR ----------
# Menunjukkan progress pengerjaan quiz
progress = (st.session_state.question_index + 1) / len(QUESTIONS)
st.progress(progress)


# ---------- MENAMPILKAN PERTANYAAN ----------
# Ambil index pertanyaan saat ini
idx = st.session_state.question_index

# Ambil data pertanyaan sesuai index
question = QUESTIONS[idx]

# Menampilkan judul pertanyaan
st.subheader(f"Pertanyaan {idx + 1} dari {len(QUESTIONS)}")

# Menampilkan opsi jawaban dalam bentuk radio button
answer = st.radio(
    question["question"],      # Teks pertanyaan
    question["options"],       # Daftar opsi jawaban
    key=f"question_{idx}"      # Key unik agar tidak bentrok antar pertanyaan
)

# Simpan jawaban user ke session_state
st.session_state.answers[idx] = answer


# ---------- NAVIGASI ----------
# Tombol navigasi hanya aktif jika quiz belum disubmit
if not st.session_state.submitted:

    # Membuat dua kolom (kiri dan kanan)
    col1, col2 = st.columns(2)

    # Tombol sebelumnya
    with col1:
        st.button(
            "⬅️ Sebelumnya",
            on_click=lambda: st.session_state.update(
                question_index=max(0, st.session_state.question_index - 1)
            )
        )

    # Tombol selanjutnya / submit
    with col2:

        # Jika sudah di pertanyaan terakhir
        if idx == len(QUESTIONS) - 1:

            if st.button("📩 Submit"):

                # Validasi: pastikan semua pertanyaan sudah dijawab
                if None in st.session_state.answers:
                    st.warning("Jawab semua pertanyaan dulu ya!")
                else:
                    st.session_state.submitted = True

        # Jika belum pertanyaan terakhir
        else:
            st.button(
                "➡️ Selanjutnya",
                on_click=lambda: st.session_state.update(
                    question_index=min(
                        len(QUESTIONS) - 1,
                        st.session_state.question_index + 1
                    )
                )
            )


# ======================================================
# HASIL QUIZ
# ======================================================

# Jika quiz sudah disubmit
if st.session_state.submitted:

    # Hitung skor berdasarkan jawaban user
    scores = calculate_score(st.session_state.answers)

    # Tentukan hasil akhir quiz
    result = get_final_result(scores)

    # Tampilkan hasil utama
    st.subheader("✨ Hasil Quiz Kamu ✨")
    st.success(f"Kamu paling cocok sebagai: **{result}**")

    # Jika hasil hanya satu role, tampilkan deskripsi role
    if result in ROLE_DESCRIPTIONS:
        st.info(ROLE_DESCRIPTIONS[result])

    # ---------- DETAIL SKOR ----------
    st.write("📊 **Detail Skor Kamu:**")
    for role, score in scores.items():
        st.write(f"- **{role}** : {score}")

    # ---------- VISUALISASI SKOR ----------
    # Ubah skor menjadi DataFrame agar sinkron antara label & nilai
    score_df = pd.DataFrame({
        "Role": list(scores.keys()),
        "Skor": list(scores.values())
    })

    # Set kolom Role sebagai index
    score_df = score_df.set_index("Role")

    # Tampilkan grafik batang
    st.bar_chart(score_df)

    # ---------- EFEK VISUAL ----------
    # Efek confetti/balloon sebagai feedback positif
    st.balloons()

    # ---------- RESET QUIZ ----------
    if st.button("🔄 Ulangi Quiz"):

        # Reset seluruh state quiz ke kondisi awal
        st.session_state.question_index = 0
        st.session_state.answers = [None] * len(QUESTIONS)
        st.session_state.submitted = False

        # Paksa Streamlit menjalankan ulang aplikasi dari awal
        st.rerun()

