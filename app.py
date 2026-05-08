import streamlit as st
import joblib
import pandas as pd
import time

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="No-Show AI Dashboard",
    page_icon="🏥",
    layout="wide"
)

# =========================
# Load model
# =========================
model = joblib.load("no_show_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# =========================
# CSS Styling
# =========================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #12355b 0%, #061826 38%, #020617 100%);
    color: #f8fafc;
    font-family: 'Segoe UI', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1350px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #082032, #020617);
    border-right: 1px solid rgba(148,163,184,0.25);
}

h1, h2, h3, label, p, span {
    color: #f8fafc !important;
}

.main-title {
    font-size: 46px;
    font-weight: 950;
    line-height: 1.08;
    color: #ffffff;
}

.subtitle {
    font-size: 18px;
    color: #cbd5e1 !important;
    margin-top: 8px;
}

.logo-card {
    background: linear-gradient(135deg, rgba(14,165,233,0.18), rgba(168,85,247,0.14));
    border: 1px solid rgba(125,211,252,0.35);
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0 0 28px rgba(14,165,233,0.15);
}

.sidebar-box {
    background: rgba(15,23,42,0.78);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 18px;
}

.card-title-blue {
    font-size: 30px;
    font-weight: 900;
    color: #38bdf8 !important;
    margin-bottom: 22px;
}

.card-title-purple {
    font-size: 30px;
    font-weight: 900;
    color: #e879f9 !important;
    margin-bottom: 22px;
}

.input-help {
    color: #cbd5e1 !important;
    font-size: 14px;
    margin-top: -8px;
    margin-bottom: 14px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.09) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(148,163,184,0.35);
}

.stButton>button {
    width: 100%;
    border-radius: 18px;
    height: 60px;
    border: none;
    color: white;
    font-size: 20px;
    font-weight: 900;
    background: linear-gradient(90deg, #0ea5e9, #2563eb, #9333ea);
    box-shadow: 0 0 26px rgba(14,165,233,0.42);
    transition: 0.25s;
}

.stButton>button:hover {
    transform: scale(1.015);
    box-shadow: 0 0 38px rgba(168,85,247,0.75);
}

/* Streamlit bordered containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(15, 23, 42, 0.84);
    border: 1.8px solid rgba(56, 189, 248, 0.36);
    border-radius: 26px;
    padding: 8px;
    box-shadow: 0 0 32px rgba(14, 165, 233, 0.14);
}

/* Result text */
.risk-percent {
    font-size: 72px;
    font-weight: 950;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 4px;
}

.risk-label {
    font-size: 36px;
    font-weight: 950;
    text-align: center;
    margin-top: 18px;
}

.low-pulse {
    animation: softPulse 1.6s infinite;
}

.high-pulse {
    animation: dangerPulse 1s infinite;
}

@keyframes softPulse {
    0% { transform: scale(1); text-shadow: 0 0 8px rgba(34,197,94,0.45); }
    50% { transform: scale(1.03); text-shadow: 0 0 22px rgba(34,197,94,0.9); }
    100% { transform: scale(1); text-shadow: 0 0 8px rgba(34,197,94,0.45); }
}

@keyframes dangerPulse {
    0% { transform: scale(1); text-shadow: 0 0 8px rgba(239,68,68,0.45); }
    50% { transform: scale(1.04); text-shadow: 0 0 30px rgba(239,68,68,1); }
    100% { transform: scale(1); text-shadow: 0 0 8px rgba(239,68,68,0.45); }
}

.result-box {
    background: rgba(34,197,94,0.13);
    border: 1px solid rgba(34,197,94,0.48);
    border-radius: 18px;
    padding: 18px;
    margin-top: 18px;
    font-size: 16px;
}

.warning-box {
    background: rgba(239,68,68,0.14);
    border: 1px solid rgba(239,68,68,0.52);
    border-radius: 18px;
    padding: 18px;
    margin-top: 18px;
    font-size: 16px;
}

.moderate-box {
    background: rgba(234,179,8,0.13);
    border: 1px solid rgba(234,179,8,0.50);
    border-radius: 18px;
    padding: 18px;
    margin-top: 18px;
    font-size: 16px;
}

.info-box {
    background: rgba(37,99,235,0.13);
    border: 1px solid rgba(59,130,246,0.45);
    border-radius: 18px;
    padding: 18px;
    margin-top: 18px;
    font-size: 16px;
}

.action-box {
    background: rgba(20,184,166,0.12);
    border: 1px solid rgba(45,212,191,0.45);
    border-radius: 18px;
    padding: 18px;
    margin-top: 18px;
    font-size: 16px;
}

.bottom-card {
    background: rgba(15, 23, 42, 0.78);
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 0 18px rgba(14, 165, 233, 0.10);
}

.stProgress > div > div > div > div {
    background-image: linear-gradient(to right, #22c55e, #eab308, #ef4444);
}

.small-muted {
    color: #cbd5e1 !important;
    font-size: 15px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Helper function
# =========================
def set_value_if_exists(df, col_name, value):
    if col_name in df.columns:
        df[col_name] = value

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.markdown("""
    <div class="logo-card">
    <h2>🏥 No-Show Predictor</h2>
    <p style="color:#cbd5e1;">AI for better appointment management</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
    <h3>📌 Dashboard</h3>
    <p>👤 Patient Input</p>
    <p>📊 Risk Prediction</p>
    <p>🩺 Clinical Action</p>
    <p>🤖 AI Model Summary</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
    <h3>🧠 Model Details</h3>
    <p><b>Algorithm:</b> XGBoost</p>
    <p><b>Target:</b> No-show prediction</p>
    <p><b>Focus:</b> Recall-oriented evaluation</p>
    <p><b>Status:</b> Academic prototype</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
    <h3>💡 Clinical Tip</h3>
    <p>Long waiting time may reflect scheduling inefficiency, not only patient behavior.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div style="display:flex; align-items:center; justify-content:space-between; gap:20px; margin-bottom:28px;">
    <div style="display:flex; align-items:center; gap:22px;">
        <div style="font-size:84px;">🏥</div>
        <div>
            <div class="main-title">Medical Appointment<br>No-Show Prediction</div>
            <div class="subtitle">AI-powered clinical dashboard for estimating appointment no-show risk.</div>
        </div>
    </div>
    <div style="font-size:92px;">🩺</div>
</div>
""", unsafe_allow_html=True)

# =========================
# Main layout
# =========================
left_col, right_col = st.columns([1.1, 1], gap="large")

# =========================
# Patient Information Card
# =========================
with left_col:
    with st.container(border=True):
        st.markdown('<div class="card-title-blue">👤 Patient Information</div>', unsafe_allow_html=True)

        age = st.slider("🎂 Age (years)", min_value=10, max_value=95, value=38)
        st.markdown('<div class="input-help">Realistic clinical age range: 10–95 years.</div>', unsafe_allow_html=True)

        waiting_days = st.slider("📅 Waiting Days", min_value=0, max_value=120, value=14)
        st.markdown('<div class="input-help">Number of days between scheduling and appointment date.</div>', unsafe_allow_html=True)

        gender = st.selectbox("🚻 Gender", ["Female", "Male"])

        sms_received = st.selectbox("💬 SMS Received", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        hypertension = st.selectbox("❤️ Hypertension", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        diabetes = st.selectbox("🩸 Diabetes", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        alcoholism = st.selectbox("🚭 Alcoholism", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        scholarship = st.selectbox("💳 Social Scholarship", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        handicap = st.selectbox("♿ Disability / Handicap", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

        predict_btn = st.button("🤖 Predict No-Show Risk")

# =========================
# Prepare input data
# =========================
input_data = pd.DataFrame(columns=model_columns)
input_data.loc[0] = 0

set_value_if_exists(input_data, "Age", age)
set_value_if_exists(input_data, "WaitingDays", waiting_days)
set_value_if_exists(input_data, "SMS_received", sms_received)
set_value_if_exists(input_data, "Hypertension", hypertension)
set_value_if_exists(input_data, "Diabetes", diabetes)
set_value_if_exists(input_data, "Alcoholism", alcoholism)
set_value_if_exists(input_data, "Scholarship", scholarship)
set_value_if_exists(input_data, "Handicap", handicap)
set_value_if_exists(input_data, "Handcap", handicap)

if "Gender_M" in input_data.columns:
    input_data["Gender_M"] = 1 if gender == "Male" else 0

# =========================
# Prediction Result Card
# =========================
with right_col:
    with st.container(border=True):
        st.markdown('<div class="card-title-purple">📊 Prediction Result</div>', unsafe_allow_html=True)

        if predict_btn:
            with st.spinner("🤖 AI model is analyzing patient information..."):
                time.sleep(0.7)
                probability = float(model.predict_proba(input_data)[0][1])

            risk_percent = probability * 100

            if risk_percent >= 70:
                risk_level = "High Risk"
                icon = "🚨"
                result_color = "#ef4444"
                box_class = "warning-box"
                anim_class = "high-pulse"
                recommendation = [
                    "Send an additional SMS reminder.",
                    "Follow up with a phone call.",
                    "Prioritize appointment confirmation.",
                    "Consider reducing waiting time if possible."
                ]
            elif risk_percent >= 40:
                risk_level = "Moderate Risk"
                icon = "⚠️"
                result_color = "#eab308"
                box_class = "moderate-box"
                anim_class = ""
                recommendation = [
                    "Send a reminder before the appointment.",
                    "Monitor if waiting time is high.",
                    "Confirm appointment availability.",
                    "Use follow-up if the patient has prior risk factors."
                ]
            else:
                risk_level = "Low Risk"
                icon = "✅"
                result_color = "#22c55e"
                box_class = "result-box"
                anim_class = "low-pulse"
                recommendation = [
                    "Routine reminder is sufficient.",
                    "No urgent intervention required.",
                    "Continue standard scheduling workflow."
                ]
                st.balloons()

            st.markdown(
                f'<div class="risk-label {anim_class}" style="color:{result_color};">{icon} {risk_level}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="risk-percent {anim_class}" style="color:{result_color};">{risk_percent:.1f}%</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="text-align:center; color:#cbd5e1; font-size:17px;">Estimated probability of appointment no-show</p>',
                unsafe_allow_html=True
            )

            st.progress(float(min(risk_percent / 100, 1.0)))

            st.markdown(f"""
            <div class="{box_class}">
            <b>🔍 Interpretation:</b><br>
            The AI model estimates a <b>{risk_percent:.1f}%</b> probability that this patient may miss the scheduled appointment.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box">
            <b>🩺 Clinical Meaning:</b><br>
            A higher risk score suggests that the patient may benefit from reminder-based or scheduling interventions.
            This is especially relevant when waiting time is long.
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="action-box"><b>✅ Suggested Clinical Actions</b><ul>', unsafe_allow_html=True)
            for item in recommendation:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="info-box">
            <b>Ready for prediction.</b><br><br>
            Enter patient and appointment information, then click <b>Predict No-Show Risk</b>.
            </div>
            """, unsafe_allow_html=True)

# =========================
# Bottom cards
# =========================
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="bottom-card">
    <h3>🎯 Main Objective</h3>
    <p class="small-muted">
    Prioritize detection of possible no-show cases using recall-focused evaluation.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="bottom-card">
    <h3>⏱️ Key Factor</h3>
    <p class="small-muted">
    WaitingDays is strongly associated with appointment non-attendance and may reflect scheduling-system factors.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="bottom-card">
    <h3>🔐 Data Use</h3>
    <p class="small-muted">
    This dashboard is for academic demonstration and clinical decision-support illustration only.
    </p>
    </div>
    """, unsafe_allow_html=True)