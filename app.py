import random
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

TOTAL_LEVELS = 10

st.set_page_config(page_title="ב'1 בית ספר אפרים צמח", page_icon="🧮", layout="centered")

THEMES = {
    "brawl": {"label": "🎮 בראול סטארס", "bg_url": "https://loremflickr.com/1920/1080/gaming?lock=11"},
    "minecraft": {"label": "🧱 מיינקראפט", "bg_url": "https://loremflickr.com/1920/1080/minecraft?lock=12"},
    "football": {"label": "⚽ כדורגל", "bg_url": "https://loremflickr.com/1920/1080/football,stadium?lock=13"},
    "ice_princess": {"label": "❄️ אלזה לבנות", "bg_url": "https://loremflickr.com/1920/1080/ice,winter,princess?lock=14"},
    "space": {"label": "🚀 חלל", "bg_url": "https://loremflickr.com/1920/1080/space,stars?lock=15"},
    "ocean": {"label": "🌊 ים", "bg_url": "https://loremflickr.com/1920/1080/ocean,waves?lock=16"},
    "jungle": {"label": "🌿 ג'ונגל", "bg_url": "https://loremflickr.com/1920/1080/jungle,forest?lock=17"},
    "rainbow": {"label": "🌈 קשת צבעונית", "bg_url": "https://loremflickr.com/1920/1080/rainbow,colorful?lock=18"},
    "unicorn": {"label": "🦄 חד קרן", "bg_url": "https://loremflickr.com/1920/1080/unicorn,pink?lock=19"},
    "dinosaur": {"label": "🦖 דינוזאורים", "bg_url": "https://loremflickr.com/1920/1080/dinosaur?lock=20"},
    "robot": {"label": "🤖 רובוטים", "bg_url": "https://loremflickr.com/1920/1080/robot,future?lock=21"},
    "basketball": {"label": "🏀 כדורסל", "bg_url": "https://loremflickr.com/1920/1080/basketball,court?lock=22"},
    "mountains": {"label": "⛰️ הרפתקה", "bg_url": "https://loremflickr.com/1920/1080/mountains,adventure?lock=23"},
    "castle": {"label": "🏰 טירה קסומה", "bg_url": "https://loremflickr.com/1920/1080/castle,magic?lock=24"},
}

if "selected_theme" not in st.session_state:
    st.session_state.selected_theme = "brawl"
if st.session_state.selected_theme not in THEMES:
    st.session_state.selected_theme = "brawl"

st.markdown(
    """
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at 20% 20%, #f7fbff 0%, #eef7ff 35%, #fefeff 100%);
    }
    .block-container {
        max-width: 560px;
        padding-top: 0.7rem;
        padding-left: 0.55rem;
        padding-right: 0.55rem;
    }
    .app-shell {
        border-radius: 28px;
        padding: 1rem 1rem 1.25rem 1rem;
        background: linear-gradient(180deg, #ffffff 0%, #f8fbff 56%, #eef6ff 100%);
        border: 1px solid #d5e8ff;
        box-shadow: 0 18px 40px rgba(38, 85, 145, 0.18);
        position: relative;
        overflow: hidden;
    }
    .app-shell::before,
    .app-shell::after {
        content: "";
        position: absolute;
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
    }
    .app-shell::before {
        width: 210px;
        height: 210px;
        left: -95px;
        top: -95px;
        background: radial-gradient(circle, rgba(146, 203, 255, 0.42) 0%, rgba(146, 203, 255, 0.03) 75%);
    }
    .app-shell::after {
        width: 240px;
        height: 240px;
        right: -110px;
        bottom: -115px;
        background: radial-gradient(circle, rgba(255, 218, 150, 0.38) 0%, rgba(255, 218, 150, 0.04) 70%);
    }
    .app-content {
        position: relative;
        z-index: 1;
    }
    .school-title {
        text-align: center;
        font-size: 1.02rem;
        font-weight: 800;
        color: #1f4e79;
        margin-bottom: 0.25rem;
    }
    .main-title {
        font-size: 1.95rem;
        font-weight: 900;
        color: #123f70;
        margin-bottom: 0.14rem;
        text-align: center;
        letter-spacing: 0.2px;
    }
    .subtitle {
        font-size: 1.02rem;
        color: #355c7d;
        margin-bottom: 0.58rem;
        text-align: center;
    }
    .top-badge {
        margin: 0.38rem auto 0.68rem auto;
        width: fit-content;
        padding: 0.36rem 0.84rem;
        border-radius: 999px;
        background: linear-gradient(180deg, #e8f4ff 0%, #dcedff 100%);
        border: 1px solid #b8d9ff;
        color: #1f5b8f;
        font-weight: 800;
        font-size: 0.9rem;
        box-shadow: 0 4px 10px rgba(54, 110, 173, 0.12);
    }
    .hero-panel {
        border-radius: 18px;
        border: 1px solid #c7e2ff;
        background: linear-gradient(125deg, #eef7ff 0%, #f7fbff 55%, #fff7e3 100%);
        padding: 0.78rem 0.95rem;
        margin-bottom: 0.65rem;
        box-shadow: 0 6px 14px rgba(80, 126, 180, 0.1);
        text-align: center;
    }
    .hero-title {
        font-size: 1.04rem;
        color: #1d4f80;
        font-weight: 900;
        margin-bottom: 0.18rem;
    }
    .hero-sub {
        font-size: 0.9rem;
        color: #426487;
        font-weight: 700;
    }
    .badge-row {
        display: flex;
        justify-content: center;
        gap: 0.44rem;
        flex-wrap: wrap;
        margin-bottom: 0.6rem;
    }
    .badge-pill {
        border-radius: 999px;
        padding: 0.22rem 0.65rem;
        font-size: 0.82rem;
        font-weight: 700;
        border: 1px solid #cae5ff;
        background: #f2f9ff;
        color: #275683;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.46rem;
        margin: 0.58rem 0 0.45rem 0;
    }
    .stat-pill {
        padding: 0.52rem 0.6rem;
        border-radius: 12px;
        background: linear-gradient(180deg, #edf6ff 0%, #f8fbff 100%);
        border: 1px solid #cfe3fb;
        box-shadow: 0 3px 8px rgba(73, 125, 187, 0.08);
        color: #1b4f80;
        text-align: center;
        font-size: 0.9rem;
        font-weight: 800;
    }
    .mode-frame {
        border-radius: 18px;
        border: 1px solid #cee5ff;
        background: linear-gradient(180deg, #fafdff 0%, #f4f9ff 100%);
        padding: 0.72rem 0.72rem 0.82rem 0.72rem;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8);
        margin-top: 0.25rem;
    }
    .progress-wrap {
        border-radius: 14px;
        border: 1px solid #cfe5ff;
        background: #f5faff;
        padding: 0.48rem 0.62rem 0.56rem 0.62rem;
        margin: 0.25rem 0 0.55rem 0;
    }
    .progress-note {
        text-align: center;
        color: #2f5f8e;
        font-size: 0.84rem;
        font-weight: 700;
        margin-top: 0.28rem;
    }
    .mascot-card {
        border-radius: 16px;
        border: 1px solid #cfe4ff;
        background: linear-gradient(180deg, #ffffff 0%, #f1f8ff 100%);
        padding: 0.58rem 0.7rem;
        margin: 0.25rem 0 0.55rem 0;
        text-align: center;
    }
    .mascot-emoji {
        font-size: 2.25rem;
        line-height: 1;
        margin-bottom: 0.12rem;
    }
    .mascot-name {
        color: #1f527f;
        font-size: 1rem;
        font-weight: 900;
        margin-bottom: 0.14rem;
    }
    .mascot-tip {
        color: #3d6689;
        font-size: 0.86rem;
        font-weight: 700;
    }
    .exercise-box {
        font-size: 2.05rem;
        font-weight: 900;
        text-align: center;
        padding: 0.82rem;
        border-radius: 18px;
        background: linear-gradient(180deg, #fff8dc 0%, #fff2bf 100%);
        border: 2px dashed #ffc85c;
        margin: 0.7rem 0;
    }
    .pulse-success {
        animation: pulseGlow 0.7s ease;
    }
    @keyframes pulseGlow {
        0% { transform: scale(0.98); box-shadow: 0 0 0 rgba(101, 214, 126, 0.1); }
        50% { transform: scale(1.01); box-shadow: 0 0 22px rgba(101, 214, 126, 0.34); }
        100% { transform: scale(1); box-shadow: 0 0 0 rgba(101, 214, 126, 0.1); }
    }
    .error-card {
        padding: 0.74rem 0.9rem;
        border-radius: 12px;
        background: #ffe8e8;
        border: 1px solid #ffb3b3;
        color: #7a1f1f;
        font-weight: 700;
        margin-top: 0.4rem;
    }
    .hint-card {
        padding: 0.74rem 0.9rem;
        border-radius: 12px;
        background: #fff8e6;
        border: 1px solid #ffd98b;
        color: #7b5711;
        font-weight: 800;
        margin-top: 0.4rem;
    }
    .answer-input-wrap {
        max-width: 210px;
        margin: 0 auto 0.15rem auto;
    }
    .success-card {
        padding: 0.74rem 0.9rem;
        border-radius: 12px;
        background: #e7fce8;
        border: 1px solid #b8e8bd;
        color: #1f6b2a;
        font-weight: 800;
        margin-top: 0.4rem;
    }
    .tiny-note {
        color: #4d6a85;
        font-size: 0.95rem;
        text-align: center;
        margin-bottom: 0.4rem;
    }
    .side-cta {
        text-align: center;
        font-size: 0.84rem;
        color: #255f8e;
        font-weight: 700;
        margin-top: 0.2rem;
    }
    .side-msg {
        text-align: center;
        border-radius: 12px;
        padding: 0.55rem 0.75rem;
        background: #eef8ff;
        border: 1px solid #cfe8ff;
        color: #1d4d79;
        font-weight: 700;
        margin-bottom: 0.55rem;
    }
    .section-title {
        text-align: center;
        color: #204b75;
    }
    .finish-card {
        border-radius: 16px;
        border: 1px solid #bfe4c5;
        background: linear-gradient(180deg, #effff1 0%, #dff8e4 100%);
        padding: 0.8rem;
        text-align: center;
        margin: 0.35rem 0 0.6rem 0;
        color: #1e6c2d;
        font-weight: 900;
    }
    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 14px;
        border: 1px solid #90c0ff;
        background: linear-gradient(180deg, #e3f2ff 0%, #cde7ff 100%);
        color: #143f6b;
        font-weight: 800;
        min-height: 2.5rem;
        transition: all 0.18s ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 18px rgba(66, 116, 171, 0.18);
        border-color: #84b9ff;
    }
    .stFormSubmitButton > button {
        background: linear-gradient(180deg, #58a9ff 0%, #2f84e4 100%);
        color: #ffffff;
        border: 1px solid #3f8fe7;
    }
    .stFormSubmitButton > button:hover {
        box-shadow: 0 9px 20px rgba(47, 132, 228, 0.28);
        border-color: #2f84e4;
    }
    .stNumberInput label,
    .stTextInput label {
        font-weight: 700;
        color: #204b75;
    }
    .stNumberInput input,
    .stTextInput input {
        border-radius: 12px !important;
        border: 1px solid #b9d8ff !important;
        background: #fafdff !important;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #5caeff 0%, #2f84e4 100%);
    }
    button[data-baseweb="tab"] {
        border-radius: 10px 10px 0 0 !important;
        font-weight: 800 !important;
        background: #f4f9ff !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #1a4f81 !important;
        background: #e6f2ff !important;
        border-bottom: 2px solid #6eaef5 !important;
    }
    @media (max-width: 560px) {
        .block-container {
            max-width: 450px;
            padding-left: 0.36rem;
            padding-right: 0.36rem;
        }
        .main-title {
            font-size: 1.55rem;
        }
        .subtitle {
            font-size: 0.9rem;
        }
        .exercise-box {
            font-size: 1.82rem;
        }
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

MODE_TITLES = {
    "add_sub": "➕➖ חיבור וחיסור",
    "mul": "✖️ כפל",
}

CHARACTERS = [
    ("👦", "שליו"),
    ("👦", "ליאם"),
    ("👦", "ראם"),
    ("👦", "אופק"),
    ("👦", "בארי"),
    ("👦", "משה ישראל"),
    ("👦", "רום"),
    ("👦", "אליה"),
    ("👦", "אליה.ב."),
    ("👦", "נדב"),
    ("👦", "אמיתי"),
    ("👦", "אביתר"),
    ("👦", "רפאל .ג."),
    ("👦", "רפאל .ל."),
    ("👦", "ישי"),
    ("👧", "נועה"),
    ("👧", "נעה"),
    ("👧", "מיכאלה"),
    ("👧", "תהילה"),
    ("👧", "אליה.פ."),
    ("👧", "נויה"),
    ("👧", "טוהר"),
    ("👧", "יהלי"),
    ("👧", "אליאן"),
    ("👩", "אלישבע המחנכת ✨"),
    ("👧", "הדר"),
    ("👧", "הודיה"),
]

LOGO_CANDIDATES = [
    "school_logo.png",
    "school_logo.jpg",
    "school_logo.jpeg",
    "logo.png",
    "logo.jpg",
    "אפרייםצמח JPG",
    "אפרייםצמח.jpg",
    "אפרייםצמח.jpeg",
    "אפריםצמח.jpg",
    "אפריםצמח.jpeg",
    "אפריים צמח.jpg",
    "אפריים צמח.jpeg",
    "אפרייםצמח.JPG",
    "אפרייםצמח.JPEG",
    "assets/school_logo.png",
    "assets/school_logo.jpg",
    "assets/אפרייםצמח.jpg",
    "assets/אפרייםצמח.jpeg",
    "assets/אפרייםצמח.JPG",
    "assets/logo.png",
]

KIDS_MESSAGES = [
    "חבורת הילדים שולחת לך כוח! 💙",
    "איזה יופי של ריכוז! ממשיכים! ⭐",
    "יאללה כיתה ב׳ — אתם תותחים! 🏆",
]

ALIEN_MESSAGES = [
    "החייזר שלח בונוס אומץ! 🚀",
    "👽 אומר: עוד תרגיל ואת/ה אלוף/ה!",
    "קרן חללית של הצלחה בדרך אליך! ✨",
]


def apply_theme_style(theme_key: str):
    theme = THEMES.get(theme_key, THEMES["brawl"])
    dark_like_themes = {"brawl", "minecraft", "football", "space", "jungle", "robot", "mountains"}
    overlay = "rgba(7, 18, 28, 0.52)" if theme_key in dark_like_themes else "rgba(255, 255, 255, 0.24)"
    text_color = "#103a64" if theme_key not in dark_like_themes else "#0f3558"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                linear-gradient(160deg, {overlay} 0%, {overlay} 100%),
                url('{theme['bg_url']}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .app-shell {{
            background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(240,248,255,0.92) 100%) !important;
            border-color: rgba(170, 210, 255, 0.75) !important;
        }}
        .school-title,
        .main-title,
        .subtitle,
        .hero-title,
        .hero-sub,
        .badge-pill,
        .top-badge,
        .stat-pill,
        .progress-note,
        .mascot-name,
        .mascot-tip,
        .tiny-note,
        .side-cta,
        .side-msg,
        .section-title,
        .finish-card {{
            color: {text_color} !important;
        }}
        .hero-panel,
        .mode-frame,
        .progress-wrap,
        .mascot-card,
        .side-msg,
        .top-badge,
        .badge-pill,
        .stat-pill {{
            border-color: rgba(170, 210, 255, 0.8) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def mkey(mode: str, name: str) -> str:
    return f"{mode}_{name}"


def find_logo_path() -> str | None:
    base = Path(__file__).resolve().parent
    for relative_path in LOGO_CANDIDATES:
        full_path = base / relative_path
        if full_path.exists() and full_path.is_file():
            return str(full_path)
    return None


def level_settings(mode: str, level: int):
    if mode == "add_sub":
        if level <= 3:
            return {"max_num": 20, "ops": ["+"], "count": 3}
        if level <= 6:
            return {"max_num": 50, "ops": ["+", "-"], "count": 3}
        if level <= 8:
            return {"max_num": 80, "ops": ["+", "-"], "count": 4}
        return {"max_num": 100, "ops": ["+", "-"], "count": 5}

    if level <= 3:
        return {"max_factor": 5, "count": 3}
    if level <= 6:
        return {"max_factor": 8, "count": 4}
    if level <= 8:
        return {"max_factor": 10, "count": 4}
    return {"max_factor": 10, "count": 5}


def generate_exercise(mode: str, level: int):
    settings = level_settings(mode, level)

    if mode == "add_sub":
        max_num = settings["max_num"]
        op = random.choice(settings["ops"])
        if op == "+":
            a = random.randint(0, max_num)
            b = random.randint(0, min(max_num, 100 - a))
            answer = a + b
        else:
            a = random.randint(0, max_num)
            b = random.randint(0, a)
            answer = a - b
        return {"a": a, "b": b, "op": op, "answer": answer}

    max_factor = settings["max_factor"]
    a = random.randint(1, max_factor)
    b = random.randint(1, min(max_factor, 100 // a))
    answer = a * b
    return {"a": a, "b": b, "op": "*", "answer": answer}


def build_hint(exercise: dict) -> str:
    a = exercise["a"]
    b = exercise["b"]
    op = exercise["op"]
    answer = exercise["answer"]
    answer_str = str(answer)

    if op == "+":
        hints = [
            f"טיפ: אפשר לפרק לעשרות ואחדות — {a} ו-{b}, ואז לחבר קודם את העשרות ואז את האחדות.",
            f"טיפ חשיבה: התוצאה תהיה גדולה מ-{max(a, b)}. נסו להוסיף בהדרגה, בקפיצות קטנות.",
            f"רמז ספרתי: הספרה הראשונה של התשובה היא {answer_str[0]}.",
            f"רמז ספרתי: ספרת האחדות בתשובה היא {answer % 10}.",
            f"טיפ: התחילו מהמספר הגדול יותר ({max(a, b)}) וספרו קדימה {min(a, b)} צעדים.",
        ]
        return random.choice(hints)

    if op == "-":
        hints = [
            f"טיפ: אפשר להוריד קודם עשרות ואז אחדות מ-{a} — זה מקל מאוד.",
            f"טיפ חשיבה: התוצאה קטנה מ-{a} ולא יורדת מתחת ל-0.",
            f"רמז ספרתי: הספרה הראשונה של התשובה היא {answer_str[0]}.",
            f"רמז ספרתי: ספרת האחדות בתשובה היא {answer % 10}.",
            f"טיפ: בדקו מה ההפרש בין {a} ל-{b} דרך קפיצות לעשר הקרובה.",
        ]
        return random.choice(hints)

    hints = [
        f"טיפ: כפל הוא חיבור חוזר — חשבו על {a} קבוצות של {b}.",
        f"טיפ: אפשר להפוך את הסדר ({b} × {a}) אם זה מרגיש לכם קל יותר.",
        f"רמז ספרתי: הספרה הראשונה של התשובה היא {answer_str[0]}.",
        f"רמז ספרתי: ספרת האחדות בתשובה היא {answer % 10}.",
        f"טיפ: פרקו גורם אחד לחלקים נוחים, ואז חברו את המכפלות.",
    ]
    return random.choice(hints)


def reset_mode(mode: str):
    st.session_state[mkey(mode, "level")] = 1
    st.session_state[mkey(mode, "correct_total")] = 0
    st.session_state[mkey(mode, "current_in_stage")] = 0
    st.session_state[mkey(mode, "finished")] = False
    st.session_state[mkey(mode, "mascot_idx")] = random.randint(0, len(CHARACTERS) - 1)
    st.session_state[mkey(mode, "help_used_in_stage")] = False
    st.session_state[mkey(mode, "help_confirm_pending")] = False
    st.session_state[mkey(mode, "help_hint_text")] = ""
    st.session_state[mkey(mode, "feedback_type")] = ""
    st.session_state[mkey(mode, "feedback_text")] = ""
    st.session_state[mkey(mode, "current_exercise")] = generate_exercise(mode, 1)


def ensure_mode_initialized(mode: str):
    if mkey(mode, "level") not in st.session_state:
        reset_mode(mode)


def queue_sound(sound_type: str):
    variant = random.randint(0, 3)
    nonce = st.session_state.get("sound_nonce", 0) + 1
    st.session_state.sound_nonce = nonce
    st.session_state.pending_sound = {
        "type": sound_type,
        "variant": variant,
        "nonce": nonce,
    }


def queue_celebration():
    nonce = st.session_state.get("celebration_nonce", 0) + 1
    st.session_state.celebration_nonce = nonce
    st.session_state.pending_celebration = {"nonce": nonce}


def render_pending_sound():
    sound = st.session_state.get("pending_sound")
    if not sound:
        return

    sound_type = sound["type"]
    variant = sound["variant"]
    nonce = sound["nonce"]

    components.html(
        f"""
        <script>
            const soundType = "{sound_type}";
            const variant = {variant};
            const nonce = {nonce};
            const key = "math-sfx-" + nonce;
            if (!window[key]) {{
                window[key] = true;
                const AudioContextClass = window.AudioContext || window.webkitAudioContext;
                if (AudioContextClass) {{
                    const ctx = new AudioContextClass();
                    const successPatterns = [
                        [523, 659, 784],
                        [587, 784, 988, 1175],
                        [659, 880, 988],
                        [523, 659, 784, 988, 1318]
                    ];
                    const failPatterns = [
                        [392, 330, 294],
                        [415, 349, 277],
                        [370, 311, 262],
                        [349, 294, 247, 220]
                    ];
                    const pattern = soundType === "success"
                        ? successPatterns[variant % successPatterns.length]
                        : failPatterns[variant % failPatterns.length];
                    const baseDur = soundType === "success" ? 0.12 : 0.17;
                    const waveformCycle = ["triangle", "sine", "square", "sawtooth"];
                    pattern.forEach((freq, i) => {{
                        const osc = ctx.createOscillator();
                        const overtone = ctx.createOscillator();
                        const gain = ctx.createGain();
                        const wave = waveformCycle[(variant + i) % waveformCycle.length];
                        osc.type = soundType === "success" ? wave : "triangle";
                        overtone.type = "sine";
                        osc.frequency.value = freq;
                        overtone.frequency.value = freq * (soundType === "success" ? 1.5 : 0.75);
                        gain.gain.setValueAtTime(0.0001, ctx.currentTime + i * baseDur);
                        gain.gain.exponentialRampToValueAtTime(0.18, ctx.currentTime + i * baseDur + 0.015);
                        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + i * baseDur + baseDur);
                        osc.connect(gain);
                        overtone.connect(gain);
                        gain.connect(ctx.destination);
                        osc.start(ctx.currentTime + i * baseDur);
                        overtone.start(ctx.currentTime + i * baseDur + 0.01);
                        osc.stop(ctx.currentTime + i * baseDur + baseDur + 0.02);
                        overtone.stop(ctx.currentTime + i * baseDur + baseDur + 0.02);
                    }});

                    if (soundType === "success") {{
                        const pop = ctx.createOscillator();
                        const popGain = ctx.createGain();
                        pop.type = "square";
                        pop.frequency.setValueAtTime(190, ctx.currentTime);
                        pop.frequency.exponentialRampToValueAtTime(320, ctx.currentTime + 0.08);
                        popGain.gain.setValueAtTime(0.0001, ctx.currentTime);
                        popGain.gain.exponentialRampToValueAtTime(0.08, ctx.currentTime + 0.02);
                        popGain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.1);
                        pop.connect(popGain);
                        popGain.connect(ctx.destination);
                        pop.start(ctx.currentTime + 0.02);
                        pop.stop(ctx.currentTime + 0.12);
                    }}
                }}
            }}
        </script>
        """,
        height=0,
    )
    st.session_state.pending_sound = None


def render_pending_celebration():
    burst = st.session_state.get("pending_celebration")
    if not burst:
        return

    nonce = burst["nonce"]
    components.html(
        f"""
        <script>
            const nonce = {nonce};
            const key = "math-burst-" + nonce;
            if (!window[key]) {{
                window[key] = true;
                const root = window.parent.document.body;
                for (let i = 0; i < 18; i++) {{
                    const p = window.parent.document.createElement('div');
                    p.textContent = i % 3 === 0 ? '⭐' : (i % 3 === 1 ? '✨' : '🎉');
                    p.style.position = 'fixed';
                    p.style.left = (40 + Math.random() * 20) + '%';
                    p.style.top = '52%';
                    p.style.fontSize = (18 + Math.random() * 18) + 'px';
                    p.style.zIndex = '9999';
                    p.style.pointerEvents = 'none';
                    p.style.transition = 'transform 850ms ease-out, opacity 850ms ease-out';
                    root.appendChild(p);
                    const x = (Math.random() - 0.5) * 360;
                    const y = -80 - Math.random() * 220;
                    requestAnimationFrame(() => {{
                        p.style.transform = `translate(${{x}}px, ${{y}}px) rotate(${{Math.random() * 260 - 130}}deg)`;
                        p.style.opacity = '0';
                    }});
                    setTimeout(() => p.remove(), 900);
                }}
            }}
        </script>
        """,
        height=0,
    )
    st.session_state.pending_celebration = None


def next_stage_or_question(mode: str):
    level = st.session_state[mkey(mode, "level")]
    stage_count = level_settings(mode, level)["count"]

    if st.session_state[mkey(mode, "current_in_stage")] + 1 >= stage_count:
        if level >= TOTAL_LEVELS:
            st.session_state[mkey(mode, "finished")] = True
            st.session_state[mkey(mode, "feedback_type")] = "success"
            st.session_state[mkey(mode, "feedback_text")] = "אלופים! סיימתם את כל 10 השלבים! 🎉"
            return

        st.session_state[mkey(mode, "level")] = level + 1
        st.session_state[mkey(mode, "current_in_stage")] = 0
        st.session_state[mkey(mode, "help_used_in_stage")] = False
        st.session_state[mkey(mode, "help_confirm_pending")] = False
        st.session_state[mkey(mode, "help_hint_text")] = ""
        st.session_state[mkey(mode, "feedback_type")] = "success"
        st.session_state[mkey(mode, "feedback_text")] = (
            f"מעולה! עולים לשלב {st.session_state[mkey(mode, 'level')]} 🚀"
        )
        st.session_state[mkey(mode, "current_exercise")] = generate_exercise(
            mode, st.session_state[mkey(mode, "level")]
        )
        st.balloons()
    else:
        st.session_state[mkey(mode, "current_in_stage")] += 1
        st.session_state[mkey(mode, "feedback_type")] = "success"
        st.session_state[mkey(mode, "feedback_text")] = "נכון מאוד! ממשיכים לתרגיל הבא ⭐"
        st.session_state[mkey(mode, "current_exercise")] = generate_exercise(mode, level)


def render_mode_tab(mode: str):
    level = st.session_state[mkey(mode, "level")]
    settings = level_settings(mode, level)
    stage_count = settings["count"]
    correct_total = st.session_state[mkey(mode, "correct_total")]
    current_in_stage = st.session_state[mkey(mode, "current_in_stage")]
    finished = st.session_state[mkey(mode, "finished")]
    help_used_in_stage = st.session_state.get(mkey(mode, "help_used_in_stage"), False)
    help_confirm_pending = st.session_state.get(mkey(mode, "help_confirm_pending"), False)
    help_hint_text = st.session_state.get(mkey(mode, "help_hint_text"), "")

    mascot_idx_key = mkey(mode, "mascot_idx")
    if mascot_idx_key not in st.session_state:
        st.session_state[mascot_idx_key] = (level - 1) % len(CHARACTERS)
    mascot_idx = st.session_state[mascot_idx_key]
    mascot_emoji, mascot_name = CHARACTERS[mascot_idx]
    st.markdown('<div class="mode-frame">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="stats-grid">
            <div class="stat-pill">📘 מצב: {MODE_TITLES[mode]}</div>
            <div class="stat-pill">🚀 שלב: {level}/{TOTAL_LEVELS}</div>
            <div class="stat-pill">🧩 תרגיל: {current_in_stage + 1}/{stage_count}</div>
            <div class="stat-pill">⭐ נכונים: {correct_total}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        progress = ((level - 1) + (current_in_stage / max(stage_count, 1))) / TOTAL_LEVELS
        st.markdown('<div class="progress-wrap">', unsafe_allow_html=True)
        st.progress(min(max(progress, 0.0), 1.0))
        st.markdown(
            f'<div class="progress-note">התקדמות כוללת: {int(progress * 100)}%</div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)
    with top_col2:
        if st.button("איפוס מצב", key=f"reset_{mode}", use_container_width=True):
            reset_mode(mode)
            st.rerun()

    if finished:
        st.markdown('<div style="text-align:center;font-size:2.6rem">🏆🎉👏</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="finish-card">אלוף/ה! סיימת את מצב {MODE_TITLES[mode]} בהצלחה גדולה ✨</div>',
            unsafe_allow_html=True,
        )
        if st.button("שחק/י שוב", key=f"again_{mode}", use_container_width=True):
            reset_mode(mode)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        return

    st.markdown(
        f"""
        <div class="mascot-card">
            <div class="mascot-emoji">{mascot_emoji}</div>
            <div class="mascot-name">החבר שלך: {mascot_name}</div>
            <div class="mascot-tip">פתרו נכון כדי להתקדם שלב ולצבור נקודות!</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("החלף חבר", key=f"swap_mascot_{mode}", use_container_width=True):
        available_indexes = [i for i in range(len(CHARACTERS)) if i != mascot_idx]
        st.session_state[mascot_idx_key] = random.choice(available_indexes)
        st.rerun()

    if not help_used_in_stage and not help_confirm_pending:
        if st.button("רמז מהחבר 💡", key=f"ask_hint_{mode}", use_container_width=True):
            st.session_state[mkey(mode, "help_confirm_pending")] = True
            st.rerun()

    if help_confirm_pending and not help_used_in_stage:
        st.warning("⚠️ שימו לב: יש רק עזרה אחת בכל שלב. להפעיל את הרמז עכשיו?")
        confirm_col, cancel_col = st.columns(2)
        with confirm_col:
            if st.button("כן, קח/י רמז", key=f"confirm_hint_{mode}", use_container_width=True):
                exercise_for_hint = st.session_state[mkey(mode, "current_exercise")]
                st.session_state[mkey(mode, "help_hint_text")] = build_hint(exercise_for_hint)
                st.session_state[mkey(mode, "help_used_in_stage")] = True
                st.session_state[mkey(mode, "help_confirm_pending")] = False
                queue_sound("success")
                st.rerun()
        with cancel_col:
            if st.button("ביטול", key=f"cancel_hint_{mode}", use_container_width=True):
                st.session_state[mkey(mode, "help_confirm_pending")] = False
                st.rerun()

    if help_used_in_stage:
        st.info("העזרה לשלב הזה כבר נוצלה ✅")
    if help_hint_text:
        st.markdown(f'<div class="hint-card">{help_hint_text}</div>', unsafe_allow_html=True)

    exercise = st.session_state[mkey(mode, "current_exercise")]
    if exercise["op"] == "+":
        operator = " + "
    elif exercise["op"] == "-":
        operator = " − "
    else:
        operator = " × "

    st.markdown(
        f'<div class="exercise-box">{exercise["a"]}{operator}{exercise["b"]} = ?</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="tiny-note">קחו נשימה, תחשבו לאט, ותנו תשובה 💡</div>', unsafe_allow_html=True)

    with st.form(f"answer_form_{mode}", clear_on_submit=True):
        st.markdown('<div class="answer-input-wrap">', unsafe_allow_html=True)
        answer_raw = st.number_input(
            "מה התשובה?",
            value=None,
            step=1,
            format="%d",
            key=f"input_{mode}",
        )
        st.markdown('</div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("בדיקה", use_container_width=True)

    if submitted:
        if answer_raw is None:
            st.session_state[mkey(mode, "feedback_type")] = "error"
            st.session_state[mkey(mode, "feedback_text")] = "צריך להקליד תשובה לפני בדיקה 🙂"
            st.rerun()

        user_answer = int(answer_raw)

        if user_answer == exercise["answer"]:
            queue_sound("success")
            queue_celebration()
            st.session_state[mkey(mode, "correct_total")] += 1
            if random.random() < 0.35:
                st.snow()
            next_stage_or_question(mode)
            st.rerun()

        queue_sound("error")
        distance = abs(user_answer - exercise["answer"])
        if distance <= 2:
            hint = "קרוב מאוד! נסו שוב 💪"
        elif distance <= 10:
            hint = "יפה שניסיתם! תבדקו שוב את החישוב 🙂"
        else:
            hint = "לא נורא בכלל, מנסים שוב ביחד 🌈"

        st.session_state[mkey(mode, "feedback_type")] = "error"
        st.session_state[mkey(mode, "feedback_text")] = hint

    feedback_type = st.session_state[mkey(mode, "feedback_type")]
    feedback_text = st.session_state[mkey(mode, "feedback_text")]
    if feedback_text:
        if feedback_type == "success":
            st.markdown(f'<div class="success-card pulse-success">{feedback_text}</div>', unsafe_allow_html=True)
        if feedback_type == "error":
            st.markdown(f'<div class="error-card">{feedback_text}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


if "pending_sound" not in st.session_state:
    st.session_state.pending_sound = None
if "sound_nonce" not in st.session_state:
    st.session_state.sound_nonce = 0
if "pending_celebration" not in st.session_state:
    st.session_state.pending_celebration = None
if "celebration_nonce" not in st.session_state:
    st.session_state.celebration_nonce = 0
if "side_message" not in st.session_state:
    st.session_state.side_message = ""

ensure_mode_initialized("add_sub")
ensure_mode_initialized("mul")

apply_theme_style(st.session_state.selected_theme)

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

logo_path = find_logo_path()
if logo_path:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(logo_path, width=140)

title_col, theme_col = st.columns([2.2, 1.8])
with title_col:
    st.markdown('<div class="school-title">כיתה ב׳1 • בית ספר אפרים צמח • טירת הכרמל</div>', unsafe_allow_html=True)
with theme_col:
    quick_col1, quick_col2, quick_col3 = st.columns(3)
    with quick_col1:
        if st.button("🎮 בראול", key="theme_btn_brawl", use_container_width=True):
            st.session_state.selected_theme = "brawl"
            st.rerun()
    with quick_col2:
        if st.button("🧱 מיינקראפט", key="theme_btn_minecraft", use_container_width=True):
            st.session_state.selected_theme = "minecraft"
            st.rerun()
    with quick_col3:
        if st.button("⚽ כדורגל", key="theme_btn_football", use_container_width=True):
            st.session_state.selected_theme = "football"
            st.rerun()

    theme_keys = list(THEMES.keys())
    st.selectbox(
        "בחרו רקע",
        options=theme_keys,
        format_func=lambda key: THEMES[key]["label"],
        key="selected_theme",
    )

apply_theme_style(st.session_state.selected_theme)

st.markdown('<div class="main-title">🧮 משחק החשבון של ב׳1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">חיבור, חיסור וכפל עד 100 • מתאים לכיתות ב׳</div>', unsafe_allow_html=True)
st.markdown('<div class="top-badge">10 שלבים לכל מצב • צלילים ואפקטים משתנים</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-panel"><div class="hero-title">🎮 מתאמנים, נהנים ומתחזקים בחשבון</div>'
    '<div class="hero-sub">התקדמות בשלבים + חיזוקים בדרך = הצלחה אמיתית</div></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="badge-row"><span class="badge-pill">🎯 מטרה: דיוק ומהירות</span>'
    '<span class="badge-pill">🧠 אימון יומי קצר</span></div>',
    unsafe_allow_html=True,
)

left_col, center_col, right_col = st.columns([1.1, 2.6, 1.1])
with left_col:
    if st.button("🧒🕍", key="kids_action", use_container_width=True):
        st.session_state.side_message = random.choice(KIDS_MESSAGES)
        queue_sound("success")
        queue_celebration()
        st.rerun()
    st.markdown('<div class="side-cta">חבורת הילדים</div>', unsafe_allow_html=True)
with center_col:
    if st.session_state.side_message:
        st.markdown(f'<div class="side-msg">{st.session_state.side_message}</div>', unsafe_allow_html=True)
with right_col:
    if st.button("👽🛸", key="alien_action", use_container_width=True):
        st.session_state.side_message = random.choice(ALIEN_MESSAGES)
        queue_sound("success")
        queue_celebration()
        st.rerun()
    st.markdown('<div class="side-cta">צוות החייזרים</div>', unsafe_allow_html=True)

tab_add, tab_mul = st.tabs([MODE_TITLES["add_sub"], MODE_TITLES["mul"]])

with tab_add:
    render_mode_tab("add_sub")

with tab_mul:
    render_mode_tab("mul")

render_pending_sound()
render_pending_celebration()

st.markdown("---")
st.markdown('<h4 class="section-title">איך מתקדמים?</h4>', unsafe_allow_html=True)
st.markdown(
    "- בכל מצב יש 10 שלבים לפי רמת קושי.\n"
    "- פותרים נכון ועוברים שלב.\n"
    "- אפשר לעבור בין הטאבים חיבור/חיסור וכפל בכל רגע."
)
st.markdown("</div>", unsafe_allow_html=True)
