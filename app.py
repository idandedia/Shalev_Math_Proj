import random
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

TOTAL_LEVELS = 10

st.set_page_config(page_title="ב'1 בית ספר אפרים צמח", page_icon="🧮", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at 20% 20%, #f7fbff 0%, #eef7ff 35%, #fefeff 100%);
    }
    .block-container {
        max-width: 500px;
        padding-top: 0.8rem;
        padding-left: 0.55rem;
        padding-right: 0.55rem;
    }
    .app-shell {
        border-radius: 24px;
        padding: 1rem 1rem 1.2rem 1rem;
        background: linear-gradient(180deg, #ffffff 0%, #f6fbff 65%, #f3f9ff 100%);
        border: 1px solid #d5e8ff;
        box-shadow: 0 16px 34px rgba(38, 85, 145, 0.16);
    }
    .school-title {
        text-align: center;
        font-size: 1.02rem;
        font-weight: 800;
        color: #1f4e79;
        margin-bottom: 0.25rem;
    }
    .main-title {
        font-size: 1.82rem;
        font-weight: 900;
        color: #123f70;
        margin-bottom: 0.14rem;
        text-align: center;
    }
    .subtitle {
        font-size: 0.98rem;
        color: #355c7d;
        margin-bottom: 0.72rem;
        text-align: center;
    }
    .top-badge {
        margin: 0.45rem auto 0.8rem auto;
        width: fit-content;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: #edf6ff;
        border: 1px solid #c8e3ff;
        color: #285d90;
        font-weight: 700;
        font-size: 0.9rem;
    }
    .stage-card {
        padding: 0.82rem 0.88rem;
        border-radius: 16px;
        background: linear-gradient(90deg, #ecf6ff 0%, #f7fbff 100%);
        border: 1px solid #cfe6ff;
        margin: 0.6rem 0;
        box-shadow: 0 4px 10px rgba(66, 116, 171, 0.08);
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
    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 12px;
        border: 1px solid #9ec8ff;
        background: linear-gradient(180deg, #dff0ff 0%, #cde7ff 100%);
        color: #143f6b;
        font-weight: 800;
        transition: all 0.18s ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 18px rgba(66, 116, 171, 0.18);
        border-color: #84b9ff;
    }
    .stNumberInput label {
        font-weight: 700;
        color: #204b75;
    }
    button[data-baseweb="tab"] {
        border-radius: 10px 10px 0 0 !important;
        font-weight: 800 !important;
    }
    @media (max-width: 560px) {
        .block-container {
            max-width: 420px;
            padding-left: 0.36rem;
            padding-right: 0.36rem;
        }
        .main-title {
            font-size: 1.45rem;
        }
        .subtitle {
            font-size: 0.9rem;
        }
        .exercise-box {
            font-size: 1.82rem;
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
    ("🧒", "יוסי האלוף"),
    ("👧", "נועה החכמה"),
    ("🧑", "אורי המהיר"),
    ("👦", "דוד הכוכב"),
    ("👧", "שירה המצטיינת"),
    ("🧒", "נועם הסקרן"),
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


def reset_mode(mode: str):
    st.session_state[mkey(mode, "level")] = 1
    st.session_state[mkey(mode, "correct_total")] = 0
    st.session_state[mkey(mode, "current_in_stage")] = 0
    st.session_state[mkey(mode, "finished")] = False
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

    mascot_emoji, mascot_name = CHARACTERS[(level - 1) % len(CHARACTERS)]
    st.markdown(
        f'<div class="stage-card"><b>מצב:</b> {MODE_TITLES[mode]} &nbsp;|&nbsp; '
        f'<b>שלב:</b> {level}/{TOTAL_LEVELS} &nbsp;|&nbsp; '
        f'<b>תרגיל בשלב:</b> {current_in_stage + 1}/{stage_count} &nbsp;|&nbsp; '
        f'<b>נכונים:</b> {correct_total}</div>',
        unsafe_allow_html=True,
    )

    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        progress = ((level - 1) + (current_in_stage / max(stage_count, 1))) / TOTAL_LEVELS
        st.progress(min(max(progress, 0.0), 1.0))
    with top_col2:
        if st.button("איפוס מצב", key=f"reset_{mode}"):
            reset_mode(mode)
            st.rerun()

    if finished:
        st.markdown('<div style="text-align:center;font-size:2.6rem">🏆🎉👏</div>', unsafe_allow_html=True)
        st.success(f"כל הכבוד! סיימת את מצב {MODE_TITLES[mode]} כולו.")
        if st.button("שחק/י שוב", key=f"again_{mode}"):
            reset_mode(mode)
            st.rerun()
        return

    st.markdown(f'<div style="text-align:center;font-size:2.5rem">{mascot_emoji}</div>', unsafe_allow_html=True)
    st.markdown(f"#### החבר שלך: {mascot_name}")
    st.markdown('<div class="tiny-note">פתרו נכון כדי להתקדם שלב ולצבור נקודות!</div>', unsafe_allow_html=True)

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

    with st.form(f"answer_form_{mode}", clear_on_submit=True):
        answer = st.number_input("מה התשובה?", step=1, format="%d", key=f"input_{mode}")
        submitted = st.form_submit_button("בדיקה")

    if submitted:
        if int(answer) == exercise["answer"]:
            queue_sound("success")
            queue_celebration()
            st.session_state[mkey(mode, "correct_total")] += 1
            if random.random() < 0.35:
                st.snow()
            next_stage_or_question(mode)
            st.rerun()

        queue_sound("error")
        distance = abs(int(answer) - exercise["answer"])
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

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

logo_path = find_logo_path()
if logo_path:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(logo_path, width=140)

st.markdown('<div class="school-title">כיתה ב׳1 • בית ספר אפרים צמח • טירת הכרמל</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🧮 משחק החשבון של ב׳1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">חיבור, חיסור וכפל עד 100 • מתאים לכיתות ב׳</div>', unsafe_allow_html=True)
st.markdown('<div class="top-badge">10 שלבים לכל מצב • צלילים ואפקטים משתנים</div>', unsafe_allow_html=True)

left_col, center_col, right_col = st.columns([1.1, 2.6, 1.1])
with left_col:
    if st.button("🧒🕍", key="kids_action"):
        st.session_state.side_message = random.choice(KIDS_MESSAGES)
        queue_sound("success")
        queue_celebration()
        st.rerun()
    st.markdown('<div class="side-cta">חבורת הילדים</div>', unsafe_allow_html=True)
with center_col:
    if st.session_state.side_message:
        st.markdown(f'<div class="side-msg">{st.session_state.side_message}</div>', unsafe_allow_html=True)
with right_col:
    if st.button("👽🛸", key="alien_action"):
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
