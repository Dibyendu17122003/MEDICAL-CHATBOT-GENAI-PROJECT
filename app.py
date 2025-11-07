import streamlit as st
import io
import base64
import nest_asyncio
from PIL import Image
import os, time

from src.medical_bot import MedicalVisionBot 
import numpy as np
import plotly.express as px

nest_asyncio.apply()

st.set_page_config(
    page_title="MedNova – Medical Vision AI",
    page_icon="🏥",
    layout="wide"
)

@st.cache_resource
def get_bot(api_key: str):
    return MedicalVisionBot(api_key)


if "uploaded_images" not in st.session_state:
    st.session_state.uploaded_images = []

if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None

if "is_thinking" not in st.session_state:
    st.session_state.is_thinking = False

if "history" not in st.session_state:
    st.session_state.history = []

if "analysis_records" not in st.session_state:
    st.session_state.analysis_records = []

if "page" not in st.session_state:
    st.session_state.page = "chat"



def apply_theme():

    st.markdown("""
    <style>
    body {
        background: #f3f8ff;
        font-family: 'Segoe UI', sans-serif;
    }
    .nav-btn {
        padding: 10px 18px;
        border-radius: 6px;
        background: white;
        border: 1px solid #d7e3ff;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s;
        color: #1e3a8a;
    }
    .nav-btn:hover {
        background: #e3edff;
    }
    .thumb-img {
        border-radius: 10px;
        border: 2px solid #89b3ff;
        max-width: 140px;
        transition: .2s;
    }
    .thumb-img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    /* Updated AI/User Bubbles for better dark-mode compatibility if needed, though background is #000 (black) */
    .chat-bubble-ai {
        background: #202020; /* Darker than pure black for contrast */
        border:1px solid #b3caff;
        color: white; /* Ensure text is visible */
        border-radius: 14px;
        padding: 14px;
        width: fit-content;
        margin-bottom: 12px;
        animation: fadeIn .25s ease;
    }
    .chat-bubble-user {
        background: #202020;
        border:1px solid #CA1A25;
        color: white;
        border-radius: 14px;
        padding: 14px;
        width: fit-content;
        margin-left: auto;
        margin-bottom: 12px;
        animation: fadeIn .25s ease;
    }
    @keyframes fadeIn {
        from {opacity:0; transform:translateY(6px);}
        to {opacity:1; transform:translateY(0);}
    }

    .tip-card {
        background: white;
        border-radius: 14px;
        padding: 18px;
        border: 1px solid #dce8ff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 140px;
        transition: 0.25s;
    }
    .tip-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    }
    .tip-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .tip-text {
        font-size: 15px;
        color: #475569;
    }
    </style>
    """, unsafe_allow_html=True)

apply_theme()



with st.sidebar:
    st.title("🏥 MedNova AI")

    
    api_key = st.secrets.get("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY"))
    if not api_key:
        st.error("Missing OPENROUTER_API_KEY")
        st.stop()

    bot = get_bot(api_key)
    st.markdown(f"**Model:** `{bot.model}`")

    st.markdown("---")
    st.subheader("📌 Purpose")
    st.write("Educational medical image understanding & guidance.")

    st.subheader("🧪 Tech Used")
    st.write("- OpenRouter Llama Vision\n- Streamlit\n- Plotly Dashboard")

    st.markdown("---")
    st.subheader("⚠ Disclaimer")
    st.write("AI is not a doctor. Consult medical professionals.")
    
 
    st.markdown("---")
    st.subheader("🧹 Session Control")
    if st.button("**Clear Chat & History**", type="secondary", use_container_width=True):
        st.session_state.uploaded_images = []
        st.session_state.last_prompt = None
        st.session_state.is_thinking = False
        st.session_state.history = []
        st.session_state.analysis_records = []
        st.toast("Chat history and analysis cleared!")
        time.sleep(0.5)
        st.rerun()



col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    if st.button("💬 Chat & Analysis", use_container_width=True,
                 type="primary" if st.session_state.page=="chat" else "secondary"):
        st.session_state.page="chat"; st.rerun()
with col2:
    if st.button("📊 Image Dashboard", use_container_width=True,
                 type="primary" if st.session_state.page=="dash" else "secondary"):
        st.session_state.page="dash"; st.rerun()
with col3:
    if st.button("📁 Chat History", use_container_width=True,
                 type="primary" if st.session_state.page=="history" else "secondary"):
        st.session_state.page="history"; st.rerun()
with col4:
    if st.button("❤️ Health Tips", use_container_width=True,
                 type="primary" if st.session_state.page=="tips" else "secondary"):
        st.session_state.page="tips"; st.rerun()



if st.session_state.page == "chat":
    st.header("🩺 Medical Image Analysis Chat")
    

    up = st.file_uploader(
        "📂 **Click here to add image(s)** (PNG, JPG, JPEG, DCM)",
        type=["png","jpg","jpeg","dcm"],
        accept_multiple_files=True
    )

    if up:
        st.session_state.uploaded_images = up
    

    if st.session_state.uploaded_images:
        st.subheader("Uploaded Images")
        
        cols = st.columns(len(st.session_state.uploaded_images))
        
        for i, file in enumerate(st.session_state.uploaded_images):
            try:
                img = Image.open(io.BytesIO(file.getvalue()))
                img.thumbnail((140,140))
                buf = io.BytesIO(); img.save(buf, "PNG")
                b64 = base64.b64encode(buf.getvalue()).decode()
                
                if i < len(cols):
                    cols[i].markdown(
                        f"<img src='data:image/png;base64,{b64}' class='thumb-img' />",
                        unsafe_allow_html=True
                    )
            except:
                if i < len(cols):
                    cols[i].warning("❗ Invalid image")

    st.markdown("---")
    

    with st.container():
        for m in st.session_state.history:
            if m["role"]=="user":
                st.markdown(f"<div class='chat-bubble-user'>{m['text']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-bubble-ai'>{m['text']}</div>", unsafe_allow_html=True)
                
    # Prompt input
    user_text = st.chat_input("Ask anything...")

    if user_text:
        st.session_state.last_prompt = user_text
        st.session_state.is_thinking = True
        st.session_state.history.append({"role":"user","text": user_text})
        st.rerun()


# =============== STREAMING RESPONSE ===============
if st.session_state.last_prompt and st.session_state.is_thinking:
    st.session_state.is_thinking = False

    prompt = st.session_state.last_prompt
    images = st.session_state.uploaded_images

    if not prompt and images:
        prompt = "Analyze these medical images with findings, severity, and causes."
        st.session_state.history[-1]['text'] = "Analyze images."

    full = ""

    if images:
        for i, file in enumerate(images):
            img_bytes = file.getvalue()
            stream = bot.analyze_stream(img_bytes, prompt)

            for ch in stream:
                if "success" in ch and ch["success"]:
                    full += ch.get("chunk","")
                else:
                    st.error(f"AI Error on image {i+1}: "+str(ch.get("error")))
                    break

            st.session_state.analysis_records.append({"img": img_bytes, "report": full})
    
    elif prompt and not images:
        stream = bot.analyze_stream(None, prompt)
        for ch in stream:
            if "success" in ch and ch["success"]:
                full += ch.get("chunk","")
            else:
                st.error("AI Error: "+str(ch.get("error")))
                break

    if full:
        st.session_state.history.append({"role":"ai","text":full})
        
    st.session_state.last_prompt=None
    st.rerun()


# =============== PAGE 2: DASHBOARD ===============
if st.session_state.page == "dash":
    st.header("📊 Image Analysis Dashboard")

    if not st.session_state.analysis_records:
        st.info("No analysis history yet. Analyze an image in the Chat page first.")
    else:
        st.subheader("Recent Images")
        cols = st.columns(min(len(st.session_state.analysis_records), 5)) 
        for i, rec in enumerate(st.session_state.analysis_records[:5]): 
            img = Image.open(io.BytesIO(rec["img"]))
            img.thumbnail((140,140))
            buf = io.BytesIO(); img.save(buf,"PNG")
            b64 = base64.b64encode(buf.getvalue()).decode()
            if i < len(cols):
                cols[i].markdown(
                    f"<img src='data:image/png;base64,{b64}' class='thumb-img'/>",
                    unsafe_allow_html=True
                )

        st.subheader("Severity Distribution")

        sev = []
        for r in st.session_state.analysis_records:
            txt = r["report"].lower()
            if "severe" in txt: sev.append("Severe")
            elif "moderate" in txt: sev.append("Moderate")
            else: sev.append("Mild")

        if sev:
            df = {"Severity": sev}
            fig = px.pie(
                df,
                names="Severity",
                title="Severity Distribution",
                color="Severity",
                color_discrete_map={
                    "Mild":"#90EE90",
                    "Moderate":"#FFD966",
                    "Severe":"#FF6B6B"
                }
            )
            st.plotly_chart(fig, use_container_width=True)


# =============== PAGE 3: CHAT HISTORY ===============
if st.session_state.page == "history":
    st.header("📁 Chat History (Last 10 AI Responses)")
    msgs = [m for m in st.session_state.history if m["role"]=="ai"][-10:][::-1]
    if not msgs:
        st.info("No AI response history yet.")
    else:
        for i, m in enumerate(msgs,1):
            st.markdown(f"**{i}.** {m['text']}")


# =============== PAGE 4: HEALTH TIPS (2 CARDS/ROW + HOVER) ===============
if st.session_state.page == "tips":
    st.header("❤️ Health Care Tips")

    cards = [
        ("🥗 Healthy Eating", "Whole foods, fruits, vegetables, lean proteins, whole grains."),
        ("🏃‍♂️ Exercise", "150 minutes of weekly physical activity."),
        ("⚖️ Weight Control", "Healthy weight prevents diabetes & heart issues."),
        ("🧘 Stress Control", "Meditation or yoga reduces stress."),
        ("💧 Hydration", "Drink 6–8 glasses of water daily."),
        ("😴 Sleep", "7–8 hours daily."),
        ("🚭 No Smoking", "Reduces lung and heart disease."),
        ("🍎 Fruits", "Boost immunity."),
        ("🥦 Vegetables", "Better digestion & heart health."),
        ("☀ Vitamin D", "Sunlight improves bone health."),
        ("👣 Walking", "Improves blood flow & weight."),
        ("🧂 Low Salt", "Controls BP."),
        ("🍬 Low Sugar", "Prevents diabetes."),
        ("🧼 Hygiene", "Avoid infections."),
        ("🧊 Skip Junk", "Reduces cholesterol & obesity."),
        ("🧍 Posture", "Protects spine."),
        ("🩺 Checkups", "Early detection saves life."),
        ("🍵 Green Tea", "Boosts metabolism."),
        ("🍛 Home Food", "More hygienic."),
        ("🍶 Healthy Oils", "Better for heart."),
        ("🧠 Mental Care", "Talk & relax."),
        ("😌 Meditation", "Improves focus."),
        ("🚰 Clean Water", "Avoid diseases."),
        ("👁 Eye Care", "Use sunglasses."),
        ("💊 Avoid Painkiller Misuse", "Harms liver & kidneys."),
        ("🌈 **Positive Mindset**", "Reduces stress, improves mood, and boosts recovery."),
    ]

    for i in range(0, len(cards), 2):
        c1, c2 = st.columns(2)

        title, txt = cards[i]
        with c1:
            st.markdown(f"""
                <div class='tip-card'>
                    <div class='tip-title'>{title}</div>
                    <div class='tip-text'>{txt}</div>
                </div>
            """, unsafe_allow_html=True)

        if i+1 < len(cards):
            title, txt = cards[i+1]
            with c2:
                st.markdown(f"""
                    <div class='tip-card'>
                        <div class='tip-title'>{title}</div>
                        <div class='tip-text'>{txt}</div>
                    </div>
                """, unsafe_allow_html=True)
