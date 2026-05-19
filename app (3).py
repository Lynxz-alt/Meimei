import streamlit as st
import time
import random
from datetime import datetime

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🎂 Happy Birthday Meimie! 🎂",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Nunito:wght@400;600;700&display=swap');

  /* ── Design tokens ──
     Background : #fff8fa  (off-white, sangat terang, tidak menyilaukan)
     Card       : #ffffff  (putih solid)
     Accent     : #d63384  (pink gelap — kontras ≥ 4.5:1 di atas putih)
     Accent-2   : #b5005b  (lebih gelap, untuk hover & heading)
     Body text  : #2d1b28  (hampir hitam, cokelat tua)
     Muted text : #6d4a60  (abu-abu ungu — masih kontras)
     Border     : #f0c6d8  (pink muda, netral)
  */

  html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
    color: #2d1b28;
  }

  .stApp {
    background-color: #fff8fa;
  }

  /* ── Hero ── */
  .hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3em;
    font-weight: 700;
    color: #b5005b;          /* gelap, kontras di #fff8fa */
    text-align: center;
    line-height: 1.2;
    margin-bottom: 0.1em;
  }

  .hero-subtitle {
    font-family: 'Nunito', sans-serif;
    font-size: 1.2em;
    font-weight: 600;
    color: #6d4a60;           /* muted, tapi masih terbaca */
    text-align: center;
    margin-top: 0;
    margin-bottom: 1.5em;
  }

  /* ── Card ── */
  .cute-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 2em 2.5em;
    margin: 1.2em 0;
    border: 1.5px solid #f0c6d8;
    box-shadow: 0 4px 20px rgba(182, 0, 91, 0.07);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }

  .cute-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 28px rgba(182,0,91,0.12);
  }

  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5em;
    font-weight: 700;
    color: #b5005b;
    margin-bottom: 0.6em;
    text-align: center;
  }

  /* ── Wish items ── */
  .wish-item {
    background: #fff0f6;
    border-left: 4px solid #d63384;
    border-radius: 10px;
    padding: 0.85em 1.2em;
    margin: 0.55em 0;
    font-size: 1em;
    color: #2d1b28;           /* teks gelap di background terang */
    font-weight: 600;
  }

  /* ── Confetti bar ── */
  .confetti-bar {
    font-size: 1.9em;
    text-align: center;
    letter-spacing: 0.3em;
    animation: bounce 1.2s ease-in-out infinite alternate;
  }

  @keyframes bounce {
    from { transform: translateY(0); }
    to   { transform: translateY(-8px); }
  }

  /* ── Cake ── */
  .cake-emoji {
    font-size: 5em;
    display: block;
    text-align: center;
    animation: wiggle 2.2s ease-in-out infinite;
  }

  @keyframes wiggle {
    0%, 100% { transform: rotate(-4deg) scale(1); }
    50%       { transform: rotate(4deg) scale(1.08); }
  }

  /* ── Birthday counter strip ── */
  .bday-counter {
    font-size: 1.3em;
    text-align: center;
    color: #2d1b28;
    font-weight: 700;
    padding: 0.5em 1em;
    background: #fce4ef;
    border-radius: 50px;
    margin: 0.5em 0;
    border: 1px solid #f0c6d8;
  }

  /* ── Buttons ── */
  .stButton > button {
    background: #d63384;
    color: #ffffff !important;
    border: none;
    border-radius: 50px;
    padding: 0.55em 2.4em;
    font-family: 'Nunito', sans-serif;
    font-weight: 700;
    font-size: 1em;
    transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 3px 12px rgba(214,51,132,0.28);
  }

  .stButton > button:hover {
    background: #b5005b !important;
    transform: scale(1.04);
    box-shadow: 0 5px 18px rgba(181,0,91,0.35);
  }

  /* ── Radio labels ── */
  .stRadio label {
    color: #2d1b28 !important;
    font-weight: 600;
    font-family: 'Nunito', sans-serif !important;
  }

  /* ── Slider label ── */
  .stSlider label, .stSelectSlider label {
    color: #2d1b28 !important;
    font-weight: 600;
  }

  /* ── Text area ── */
  .stTextArea label { color: #2d1b28 !important; font-weight: 600; }
  .stTextArea textarea {
    border-radius: 14px !important;
    border: 1.5px solid #d63384 !important;
    font-family: 'Nunito', sans-serif !important;
    color: #2d1b28 !important;
    background: #fff8fa !important;
  }

  /* ── Streamlit default text (labels, captions) ── */
  label, p, .stMarkdown p {
    color: #2d1b28;
  }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: #fff0f6; }
  ::-webkit-scrollbar-thumb { background: #d63384; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE ──────────────────────────────────────────────────────────────
if "wishes_sent" not in st.session_state:
    st.session_state.wishes_sent = False
if "candles_blown" not in st.session_state:
    st.session_state.candles_blown = False
if "love_meter" not in st.session_state:
    st.session_state.love_meter = 0
if "treasure_found" not in st.session_state:
    st.session_state.treasure_found = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False


# ─── HELPERS ───────────────────────────────────────────────────────────────────
HEARTS = ["💖", "💗", "💓", "💕", "🌸", "✨", "🦋", "🌺", "🍭", "🎀"]
FLOWERS = ["🌸", "🌺", "🌹", "🌼", "🌻", "💐", "🌷"]

def confetti_rain():
    icons = ["🎉", "🎊", "✨", "🎈", "🌸", "💖", "🍰", "🎀", "🦋", "⭐"]
    return " ".join(random.choices(icons, k=16))

def random_color_heart():
    return random.choice(HEARTS)


# ─── HERO SECTION ──────────────────────────────────────────────────────────────
st.markdown('<div class="confetti-bar">🎊 🎈 🎉 🎂 🎉 🎈 🎊</div>', unsafe_allow_html=True)

st.markdown('<p class="hero-title">Happy Birthday,<br>Clarissa 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">"Meimie" yang selalu ada di hati koko 💖</p>', unsafe_allow_html=True)

st.markdown('<span class="cake-emoji">🎂</span>', unsafe_allow_html=True)

st.markdown(f"""
<div class="bday-counter">
  {confetti_rain()}
</div>
""", unsafe_allow_html=True)

st.divider()


# ─── SECTION 1: TIUP LILIN ─────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🕯️ Tiup Lilin Ulang Tahunmu!</p>', unsafe_allow_html=True)

candle_count = st.slider(
    "Berapa lilin yang mau kamu tiup hari ini, Meimie? 🕯️",
    min_value=1, max_value=25, value=1,
    help="Geser ke jumlah lilinmu!"
)

candles_display = "🕯️" * candle_count
st.markdown(f"<div style='text-align:center; font-size:2em; letter-spacing:4px;'>{candles_display}</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌬️ Tiup Semua Lilin! "):
        st.session_state.candles_blown = True

if st.session_state.candles_blown:
    st.balloons()
    st.markdown(f"""
    <div style='text-align:center; font-size:1.8em;'>{"🌟" * candle_count}</div>
    <div style='text-align:center; color:#e91e8c; font-size:1.2em; font-weight:700; margin-top:0.5em;'>
      ✨ Semua lilin padam! Semoga {candle_count} harapanmu terkabul ya Meimie! ✨
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 2: KATA-KATA MANIS ────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">💌 Pesan dari koko untuk Meimie</p>', unsafe_allow_html=True)

wishes = [
    "🌸 Meimie, kamu itu bukan sekadar adek — kamu permata yang bikin hari-hari lebih berwarna!",
    "💖 Di hari spesialmu ini, semoga semua impian dan harapan kamu jadi kenyataan yang indah.",
    "🦋 Kamu tumbuh jadi wanita luar biasa, dan koko bangga banget punya adek kayak kamu.",
    "🌺 Semoga tahun ini penuh kebahagiaan, kesuksesan, dan hal-hal manis yang kamu layak dapatkan.",
    "✨ Jaga kesehatan ya, Meimie! Koko selalu doain yang terbaik untuk Clarissa kita yang satu ini.",
    "🎀 Senyummu itu menular banget — jangan pernah berhenti senyum ya!",
    "🍰 Selamat ulang tahun, Meimie tersayang! Love you to the moon and back! 🌙",
]

for w in wishes:
    st.markdown(f'<div class="wish-item">{w}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 3: LOVE METER ─────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">💕 Sayang-O-Meter Koko ke Meimie</p>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#880e4f;'>Tekan tombol buat ngukur rasa sayang Koko! 😄</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("❤️ Ukur Sekarang!"):
        st.session_state.love_meter = 101  # Always 101% — beyond limit!

if st.session_state.love_meter > 0:
    st.markdown("""
    <div style='text-align:center;'>
      <div style='font-size:3em; margin-bottom:0.2em;'>💖💖💖💖💖</div>
      <div style='background:linear-gradient(90deg,#f48fb1,#e91e8c); border-radius:50px; 
                  padding:0.5em 2em; color:white; font-weight:700; font-size:1.3em; 
                  display:inline-block; box-shadow:0 4px 15px rgba(233,30,140,0.3);'>
        101% — MELEBIHI BATAS MAKSIMAL! 🚀
      </div>
      <div style='color:#c2185b; margin-top:0.8em; font-size:1.1em;'>
        Rasa sayang koko ke Meimie terlalu besar sampai alat ukurnya error! 😂💕
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 4: QUIZ FUN ───────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🎯 Quiz Ulang Tahun Meimie!</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#880e4f; font-size:0.95em;'>Jawab pertanyaan seru ini ya! 😄</p>", unsafe_allow_html=True)

questions = [
    {
        "q": "1. Apa yang bikin Meimie paling spesial? 🌟",
        "opts": ["Senyumnya yang menular", "Hatinya yang baik", "Semangatnya yang membara", "Semuanya benar! 💯"],
        "ans": "Semuanya benar! 💯"
    },
    {
        "q": "2. Apa yang Meimie layak dapatkan di hari ulang tahunnya?",
        "opts": ["Hanya sedikit kebahagiaan", "Kebahagiaan sebesar-besarnya! 🎉", "Biasa-biasa saja", "Nggak ada"],
        "ans": "Kebahagiaan sebesar-besarnya! 🎉"
    },
    {
        "q": "3. Berapa banyak orang yang sayang sama Meimie?",
        "opts": ["Sedikit", "Lumayan", "Banyak", "Tak terhitung banyaknya! 💖"],
        "ans": "Tak terhitung banyaknya! 💖"
    },
]

score = 0
all_answered = True
answers = []
for i, q in enumerate(questions):
    choice = st.radio(q["q"], q["opts"], key=f"quiz_{i}", index=None)
    answers.append((choice, q["ans"]))
    if choice is None:
        all_answered = False

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎉 Cek Jawaban!"):
        if all_answered:
            st.session_state.quiz_done = True
            st.session_state.quiz_score = sum(1 for c, a in answers if c == a)
        else:
            st.warning("Jawab semua pertanyaan dulu ya, Meimie! 🌸")

if st.session_state.quiz_done:
    s = st.session_state.quiz_score
    if s == 3:
        st.success(f"🏆 Sempurna! Skor: {s}/3 — Meimie jenius! Jawaban kamu 100% benar! ✨")
    elif s == 2:
        st.info(f"💕 Hampir sempurna! Skor: {s}/3 — Meimie hebat! Coba lagi ya!")
    else:
        st.warning(f"🌸 Skor: {s}/3 — Nggak apa-apa! Meimie tetap yang terbaik! 💖")

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 5: BUAT UCAPAN ────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">📝 Kirim Harapan untuk Meimie</p>', unsafe_allow_html=True)

wish_text = st.text_area(
    "Tulis harapan atau doa kamu untuk Meimie di sini 💌",
    placeholder="Contoh: Semoga Meimie selalu bahagia, sehat, dan sukses! 🌸",
    height=120,
)

mood = st.select_slider(
    "Seberapa excited kamu hari ini?",
    options=["😐 Biasa", "🙂 Lumayan", "😊 Senang", "😄 Sangat Senang", "🥰 Super Bahagia!"],
    value="🥰 Super Bahagia!"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💌 Kirim Ucapan!"):
        if wish_text.strip():
            st.session_state.wishes_sent = True
        else:
            st.warning("Tulis harapanmu dulu ya! 🌸")

if st.session_state.wishes_sent and wish_text.strip():
    st.balloons()
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#fce4ec,#f8bbd0); border-radius:20px; 
                padding:1.5em; margin-top:1em; border:2px dashed #f48fb1; text-align:center;'>
      <div style='font-size:2em; margin-bottom:0.5em;'>💌✨💌</div>
      <div style='font-style:italic; color:#880e4f; font-size:1.1em; margin-bottom:0.5em;'>
        "{wish_text}"
      </div>
      <div style='color:#c2185b; font-weight:700;'>
        Mood kamu: {mood} — Ucapan sudah terkirim ke hati Meimie! 🎀
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 6: BIRTHDAY CARD ──────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🎀 Kartu Ultah Digital</p>', unsafe_allow_html=True)

st.markdown(f"""
<div style='
  background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 50%, #fce4ec 100%);
  border: 3px solid #f48fb1;
  border-radius: 24px;
  padding: 2.5em 2em;
  text-align: center;
  position: relative;
  box-shadow: 0 8px 32px rgba(244,143,177,0.25);
'>
  <div style='font-size:3.5em; margin-bottom:0.3em;'>🌸🎂🌸</div>
  <div style='font-family: "Playfair Display", serif; font-size:2em; color:#ad1457; font-weight:700;'>
    Happy Birthday!
  </div>
  <div style='font-family: "Playfair Display", serif; font-size:1.5em; color:#e91e8c; font-style:italic; margin:0.3em 0;'>
    Clarissa "Meimie" Tersayang
  </div>
  <div style='font-size:1.5em; margin:0.8em 0; letter-spacing:8px;'>
    💖 🌺 ✨ 🦋 ✨ 🌺 💖
  </div>
  <div style='color:#880e4f; font-size:1.05em; line-height:1.7; max-width:400px; margin:0 auto;'>
    Setiap hari bersamamu adalah hadiah.<br>
    Terima kasih sudah jadi adek yang luar biasa.<br>
    Koko sayang kamu setulus-tulusnya. 🌙
  </div>
  <div style='margin-top:1.5em; font-size:1.8em;'>
    🎉 🎈 🍰 🎊 🎁 🎈 🎉
  </div>
  <div style='margin-top:1em; color:#c2185b; font-weight:700; font-size:0.9em;'>
    — Dari Koko yang selalu sayang Meimie 💕
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 7: MUSIK MOOD ─────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🎵 Lagu Ultah Versi Kita!</p>', unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; background:linear-gradient(135deg,#fce4ec,#e8f4fd); 
            border-radius:20px; padding:1.5em; border:1.5px solid #f48fb1;'>
  <div style='font-size:3em; animation:bounce 1s infinite alternate; display:inline-block;'>🎵</div>
  <div style='font-family:"Playfair Display", serif; font-size:1.3em; color:#880e4f; 
              margin:0.8em 0; line-height:1.9;'>
    <i>
    🎂 Selamat ulang tahun Meimie,<br>
    🌸 Semoga panjang umur selalu,<br>
    💖 Selamat ulang tahun Clarissa,<br>
    ✨ Bahagia, sehat, dan sukses selalu! ✨
    </i>
  </div>
  <div style='font-size:1.5em; margin-top:0.5em;'>🎶🎸🎹🎺🎶</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── HITUNG MUNDUR HARI INI ─────────────────────────────────────────────────────
now = datetime.now()
st.markdown(f"""
<div style='text-align:center; margin:1.5em 0; color:#c2185b; font-size:0.9em; opacity:0.75;'>
  🕐 Hari ini — Hari paling spesial! 🌟
</div>
""", unsafe_allow_html=True)


# ─── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding:2em 0 1em; color:#ad1457; opacity:0.7;'>
  Made with 💖 especially for <b>Clarissa "Meimie"</b><br>
  <span style='font-size:0.85em;'>Happy Birthday, sayang! 🌸✨🎂</span>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="confetti-bar">{confetti_rain()}</div>', unsafe_allow_html=True)
