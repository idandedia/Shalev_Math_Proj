import random
import streamlit as st
import streamlit.components.v1 as components

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
        padding-top: 0.9rem;
        padding-left: 0.6rem;
        padding-right: 0.6rem;
    }
    .app-shell {
        border-radius: 24px;
        padding: 1.1rem 1.1rem 1.3rem 1.1rem;
        background: linear-gradient(180deg, #ffffff 0%, #f6fbff 65%, #f3f9ff 100%);
        border: 1px solid #d5e8ff;
        box-shadow: 0 16px 34px rgba(38, 85, 145, 0.16);
    }
    .school-title {
        text-align: center;
        font-size: 1.05rem;
        font-weight: 800;
        color: #1f4e79;
        margin-bottom: 0.35rem;
    }
    .main-title {
        font-size: 1.9rem;
        font-weight: 800;
        color: #123f70;
        margin-bottom: 0.2rem;
        text-align: center;
    }
    .subtitle {
        font-size: 1.05rem;
        color: #355c7d;
        margin-bottom: 0.9rem;
        text-align: center;
    }
    .top-badge {
        margin: 0.5rem auto 0.8rem auto;
        width: fit-content;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: #edf6ff;
        border: 1px solid #c8e3ff;
        color: #285d90;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .stage-card {
        padding: 0.9rem 1rem;
        border-radius: 16px;
        background: linear-gradient(90deg, #ecf6ff 0%, #f7fbff 100%);
        border: 1px solid #cfe6ff;
        margin: 0.6rem 0;
        box-shadow: 0 4px 10px rgba(66, 116, 171, 0.08);
    }
    .exercise-box {
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        padding: 0.9rem;
        border-radius: 18px;
        background: linear-gradient(180deg, #fff8dc 0%, #fff2bf 100%);
        border: 2px dashed #ffc85c;
        margin: 0.8rem 0;
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
        padding: 0.8rem 1rem;
        border-radius: 12px;
        background: #ffe8e8;
        border: 1px solid #ffb3b3;
        color: #7a1f1f;
        font-weight: 600;
        margin-top: 0.4rem;
    }
    .success-card {
        padding: 0.8rem 1rem;
        border-radius: 12px;
        background: #e7fce8;
        border: 1px solid #b8e8bd;
        color: #1f6b2a;
        font-weight: 700;
        margin-top: 0.4rem;
    }
    .character {
        font-size: 3.2rem;
        text-align: center;
        margin: 0.2rem 0 0.4rem 0;
    }
    .tiny-note {
        color: #4d6a85;
        font-size: 0.95rem;
        text-align: center;
    }
    .side-strip {
        position: fixed;
        top: 95px;
        z-index: 1;
        width: 64px;
        display: flex;
        flex-direction: column;
        gap: 8px;
        align-items: center;
        pointer-events: none;
        opacity: 0.95;
    }
    .side-left {
        left: 8px;
    }
    .side-right {
        right: 8px;
    }
    .side-char {
        width: 54px;
        height: 54px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 14px;
        background: #ffffff;
        border: 1px solid #d6e8ff;
        box-shadow: 0 6px 14px rgba(51, 88, 143, 0.14);
        font-size: 1.6rem;
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
        font-weight: 700;
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
    @media (max-width: 560px) {
        .block-container {
            max-width: 420px;
            padding-left: 0.4rem;
            padding-right: 0.4rem;
        }
        .main-title {
            font-size: 1.55rem;
        }
        .subtitle {
            font-size: 0.92rem;
        }
        .exercise-box {
            font-size: 1.9rem;
        }
    }
    @media (max-width: 1050px) {
        .side-strip {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

CHARACTERS = [
    ("🦊", "שועל חכם"),
    ("🐼", "פנדה שמחה"),
    ("🐸", "צפרדע קופצת"),
    ("🦁", "אריה אמיץ"),
    ("🐧", "פינגווין מצחיק"),
    ("🐨", "קואלה רגוע"),
    ("🦄", "חד-קרן קסום"),
    ("🐯", "נמר מהיר"),
]


def level_settings(level: int):
    if level <= 5:
        return {"max_num": 20, "ops": ["+"], "count": 3}
    if level <= 10:
        return {"max_num": 50, "ops": ["+", "-"], "count": 3}
    if level <= 15:
        return {"max_num": 80, "ops": ["+", "-"], "count": 4}
    return {"max_num": 100, "ops": ["+", "-"], "count": 5}


def generate_exercise(level: int):
    settings = level_settings(level)
    max_num = settings["max_num"]
    op = random.choice(settings["ops"])

    if op == "+":
        a = random.randint(0, max_num)
        max_b = min(max_num, 100 - a)
        b = random.randint(0, max_b)
        answer = a + b
    else:
        a = random.randint(0, max_num)
        b = random.randint(0, a)
        answer = a - b

    if random.random() < 0.2:
        a = min(a + random.randint(1, 5), 100)
        if op == "+":
            b = min(b, 100 - a)
            answer = a + b
        else:
            b = min(b, a)
            answer = a - b

    return {"a": a, "b": b, "op": op, "answer": answer}


def reset_game():
    st.session_state.level = 1
    st.session_state.correct_total = 0
    st.session_state.current_in_stage = 0
    st.session_state.finished = False
    st.session_state.feedback_type = ""
    st.session_state.feedback_text = ""
    st.session_state.pending_sound = None
    st.session_state.pending_celebration = None
    st.session_state.current_exercise = generate_exercise(1)


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


def next_stage_or_question():
    level = st.session_state.level
    settings = level_settings(level)
    stage_count = settings["count"]

    if st.session_state.current_in_stage + 1 >= stage_count:
        if level >= 20:
            st.session_state.finished = True
            st.session_state.feedback_type = "success"
            st.session_state.feedback_text = "אלופים! סיימתם את כל 20 השלבים! 🎉"
            return

        st.session_state.level = level + 1
        st.session_state.current_in_stage = 0
        st.session_state.feedback_type = "success"
        st.session_state.feedback_text = f"מעולה! עולים לשלב {st.session_state.level} 🚀"
        st.session_state.current_exercise = generate_exercise(st.session_state.level)
        st.balloons()
    else:
        st.session_state.current_in_stage += 1
        st.session_state.feedback_type = "success"
        st.session_state.feedback_text = "נכון מאוד! ממשיכים לתרגיל הבא ⭐"
        st.session_state.current_exercise = generate_exercise(level)


if "level" not in st.session_state:
    reset_game()

if "pending_sound" not in st.session_state:
    st.session_state.pending_sound = None

if "sound_nonce" not in st.session_state:
    st.session_state.sound_nonce = 0

if "pending_celebration" not in st.session_state:
    st.session_state.pending_celebration = None

if "celebration_nonce" not in st.session_state:
    st.session_state.celebration_nonce = 0

level = st.session_state.level
settings = level_settings(level)
stage_count = settings["count"]

emoji, name = CHARACTERS[(level - 1) % len(CHARACTERS)]

st.markdown(
    """
    <div class="side-strip side-left">
        <div class="side-char">👧</div>
        <div class="side-char">🧒</div>
        <div class="side-char">👦</div>
        <div class="side-char">👧</div>
        <div class="side-char">🧒</div>
    </div>
    <div class="side-strip side-right">
        <div class="side-char">👽</div>
        <div class="side-char">🛸</div>
        <div class="side-char">👾</div>
        <div class="side-char">👽</div>
        <div class="side-char">🛸</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

st.markdown('<div class="school-title">כיתה ב׳1 • בית ספר אפרים צמח • טירת הכרמל</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🧮 משחק החשבון של ב׳1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">חיבור וחיסור עד 100 • 20 שלבים אינטראקטיביים</div>', unsafe_allow_html=True)
st.markdown('<div class="top-badge">🎵 עכשיו עם אפקטים קוליים מתחלפים</div>', unsafe_allow_html=True)

col_top1, col_top2 = st.columns([3, 1])
with col_top1:
    st.markdown(
        f'<div class="stage-card"><b>שלב נוכחי:</b> {level}/20 &nbsp;|&nbsp; '
        f'<b>תרגיל בשלב:</b> {st.session_state.current_in_stage + 1}/{stage_count} &nbsp;|&nbsp; '
        f'<b>סה"כ נכונים:</b> {st.session_state.correct_total}</div>',
        unsafe_allow_html=True,
    )
with col_top2:
    if st.button("התחל מחדש"):
        reset_game()
        st.rerun()

overall_progress = ((level - 1) + (st.session_state.current_in_stage / max(stage_count, 1))) / 20
st.progress(min(max(overall_progress, 0.0), 1.0))

if st.session_state.finished:
    render_pending_sound()
    st.markdown('<div class="character">🏆🎉👏</div>', unsafe_allow_html=True)
    st.success("כל הכבוד! סיימת את המשחק כולו. רוצים להתחיל שוב?")
    if st.button("שחק/י שוב מהתחלה"):
        reset_game()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

st.markdown(f'<div class="character">{emoji}</div>', unsafe_allow_html=True)
st.markdown(f"### החבר שלך להיום: {name}")
st.markdown('<div class="tiny-note">פתרו נכון כדי להתקדם שלב ולצבור נקודות!</div>', unsafe_allow_html=True)

exercise = st.session_state.current_exercise
operator = " + " if exercise["op"] == "+" else " − "
st.markdown(
    f'<div class="exercise-box">{exercise["a"]}{operator}{exercise["b"]} = ?</div>',
    unsafe_allow_html=True,
)

with st.form("answer_form", clear_on_submit=True):
    answer = st.number_input("מה התשובה?", step=1, format="%d")
    submitted = st.form_submit_button("בדיקה")

if submitted:
    if int(answer) == exercise["answer"]:
        queue_sound("success")
        queue_celebration()
        st.session_state.correct_total += 1
        if random.random() < 0.35:
            st.snow()
        next_stage_or_question()
        st.rerun()
    else:
        queue_sound("error")
        distance = abs(int(answer) - exercise["answer"])
        if distance <= 2:
            hint = "קרוב מאוד! נסו שוב 💪"
        elif distance <= 10:
            hint = "יפה שניסיתם! תבדקו שוב את החישוב 🙂"
        else:
            hint = "לא נורא בכלל, מנסים שוב ביחד 🌈"

        st.session_state.feedback_type = "error"
        st.session_state.feedback_text = hint

if st.session_state.feedback_text:
    if st.session_state.feedback_type == "success":
        st.markdown(
            f'<div class="success-card pulse-success">{st.session_state.feedback_text}</div>',
            unsafe_allow_html=True,
        )
    elif st.session_state.feedback_type == "error":
        st.markdown(
            f'<div class="error-card">{st.session_state.feedback_text}</div>',
            unsafe_allow_html=True,
        )

render_pending_sound()
render_pending_celebration()

st.markdown("---")
st.markdown('<h4 class="section-title">איך מתקדמים?</h4>', unsafe_allow_html=True)
st.markdown(
    "- פותרים תרגילים נכון כדי להתקדם בשלב.\n"
    "- בסוף כל שלב עוברים לשלב הבא.\n"
    "- בשלב 20 מחכה מסך ניצחון חגיגי!"
)
st.markdown("</div>", unsafe_allow_html=True)
