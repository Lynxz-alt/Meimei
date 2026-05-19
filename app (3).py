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
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Quicksand:wght@400;600;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
    background: #fff0f6;
  }

  /* Animated pastel gradient background */
  .stApp {
    background: linear-gradient(135deg, #ffdde1 0%, #fff0f5 30%, #e8f4fd 60%, #f3e5f5 100%);
    background-size: 400% 400%;
    animation: gradientShift 8s ease infinite;
  }

  @keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  /* Floating hearts animation */
  @keyframes floatUp {
    0%   { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-120px) scale(1.5); opacity: 0; }
  }

  /* Hero title */
  .hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.2em;
    font-weight: 700;
    color: #c2185b;
    text-align: center;
    line-height: 1.2;
    text-shadow: 2px 4px 15px rgba(194,24,91,0.15);
    margin-bottom: 0;
  }

  .hero-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.5em;
    color: #e91e8c;
    text-align: center;
    margin-top: 0;
    margin-bottom: 1.5em;
  }

  /* Card style */
  .cute-card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 2em 2.5em;
    margin: 1.2em 0;
    border: 1.5px solid rgba(255, 182, 193, 0.5);
    box-shadow: 0 8px 32px rgba(194,24,91,0.08);
    transition: transform 0.3s ease;
  }

  .cute-card:hover {
    transform: translateY(-4px);
  }

  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6em;
    color: #ad1457;
    margin-bottom: 0.5em;
    text-align: center;
  }

  /* Wish cards */
  .wish-item {
    background: linear-gradient(135deg, #fff9fc, #fce4ec);
    border-left: 4px solid #f48fb1;
    border-radius: 12px;
    padding: 0.9em 1.2em;
    margin: 0.6em 0;
    font-size: 1.05em;
    color: #880e4f;
    box-shadow: 0 4px 12px rgba(244,143,177,0.15);
  }

  /* Confetti emoji rain */
  .confetti-bar {
    font-size: 2em;
    text-align: center;
    letter-spacing: 0.3em;
    animation: bounce 1s infinite alternate;
  }

  @keyframes bounce {
    from { transform: translateY(0); }
    to   { transform: translateY(-10px); }
  }

  /* Cake animation */
  .cake-emoji {
    font-size: 5em;
    display: block;
    text-align: center;
    animation: wiggle 2s ease-in-out infinite;
  }

  @keyframes wiggle {
    0%, 100% { transform: rotate(-5deg) scale(1); }
    50%       { transform: rotate(5deg) scale(1.1); }
  }

  /* Buttons override */
  .stButton > button {
    background: linear-gradient(135deg, #f48fb1, #e91e8c);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.6em 2.5em;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.05em;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(233,30,140,0.3);
    cursor: pointer;
  }

  .stButton > button:hover {
    background: linear-gradient(135deg, #e91e8c, #ad1457);
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(233,30,140,0.4);
  }

  /* Slider */
  .stSlider [data-baseweb=slider] {
    accent-color: #e91e8c;
  }

  /* Radio */
  .stRadio label { color: #880e4f !important; font-weight: 600; }

  /* Text area */
  .stTextArea textarea {
    border-radius: 16px !important;
    border: 1.5px solid #f48fb1 !important;
    font-family: 'Quicksand', sans-serif !important;
  }

  /* Metric */
  [data-testid="metric-container"] {
    background: rgba(255,255,255,0.7);
    border-radius: 16px;
    padding: 0.8em;
    border: 1px solid #f8bbd0;
    text-align: center;
  }

  .footer-text {
    text-align: center;
    color: #ad1457;
    font-size: 0.95em;
    margin-top: 2em;
    opacity: 0.7;
  }

  /* Birthday counter */
  .bday-counter {
    font-size: 1.3em;
    text-align: center;
    color: #c2185b;
    font-weight: 700;
    padding: 0.5em;
    background: rgba(255,182,193,0.3);
    border-radius: 50px;
    margin: 0.5em 0;
  }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: #fff0f6; }
  ::-webkit-scrollbar-thumb { background: #f48fb1; border-radius: 3px; }
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
st.markdown('<p class="hero-subtitle">"Meimie" yang selalu ada di hati kak 💖</p>', unsafe_allow_html=True)

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
st.markdown('<p class="section-title">💌 Pesan dari Kak untuk Meimie</p>', unsafe_allow_html=True)

wishes = [
    "🌸 Meimie, kamu itu bukan sekadar adek — kamu permata yang bikin hari-hari lebih berwarna!",
    "💖 Di hari spesialmu ini, semoga semua impian dan harapan kamu jadi kenyataan yang indah.",
    "🦋 Kamu tumbuh jadi wanita luar biasa, dan kak bangga banget punya adek kayak kamu.",
    "🌺 Semoga tahun ini penuh kebahagiaan, kesuksesan, dan hal-hal manis yang kamu layak dapatkan.",
    "✨ Jaga kesehatan ya, Meimie! Kak selalu doain yang terbaik untuk Clarissa kita yang satu ini.",
    "🎀 Senyummu itu menular banget — jangan pernah berhenti senyum ya!",
    "🍰 Selamat ulang tahun, Meimie tersayang! Love you to the moon and back! 🌙",
]

for w in wishes:
    st.markdown(f'<div class="wish-item">{w}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ─── SECTION 3: LOVE METER ─────────────────────────────────────────────────────
st.markdown('<div class="cute-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">💕 Sayang-O-Meter Kak ke Meimie</p>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#880e4f;'>Tekan tombol buat ngukur rasa sayang kak! 😄</p>", unsafe_allow_html=True)

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
        Rasa sayang kak ke Meimie terlalu besar sampai alat ukurnya error! 😂💕
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
    Kak sayang kamu setulus-tulusnya. 🌙
  </div>
  <div style='margin-top:1.5em; font-size:1.8em;'>
    🎉 🎈 🍰 🎊 🎁 🎈 🎉
  </div>
  <div style='margin-top:1em; color:#c2185b; font-weight:700; font-size:0.9em;'>
    — Dari Kak yang selalu sayang Meimie 💕
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
  🕐 Hari ini: {now.strftime("%d %B %Y, %H:%M")} WIB — Hari paling spesial! 🌟
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
