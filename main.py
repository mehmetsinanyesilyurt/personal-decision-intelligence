import streamlit as st
import pandas as pd
import psutil
from database_manager import DatabaseManager
from system_monitor import SystemMonitor
import time
import plotly.graph_objects as go # Havalı grafikler için

# --- FENASAL CSS BAŞLANGICI ---
def local_css():
    st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #00ff41; /* Matrix Yeşili */
    }
    
    /* Kartlar ve Kutular */
    div[data-testid="metric-container"] {
        background-color: rgba(0, 255, 65, 0.05);
        border: 1px solid #00ff41;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 10px #00ff41;
    }
    
    /* Sidebar (Menü) */
    .css-1d391kg {
        background-color: rgba(20, 20, 20, 0.9);
    }
    
    /* Başlıklar */
    h1, h2, h3 {
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 2px 2px #ff00ff; /* Cyberpunk Pembe */
        color: #00f3ff !important;
    }

    /* Input Alanları */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1a1a1a;
        color: #00f3ff;
        border: 1px solid #00f3ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PROGRAM BAŞLANGICI ---
st.set_page_config(page_title="SENTINEL-V CORE", layout="wide")
local_css()
db = DatabaseManager()
monitor = SystemMonitor()

# Header Section
st.markdown("<h1 style='text-align: center;'>🛡️ SENTINEL-V: NEURAL INTERFACE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff00ff;'>System Operations & Decision Engine v1.0.4</p>", unsafe_allow_html=True)

# Sidebar - Karar Girişi (Input)
st.sidebar.markdown("### 🧠 NEURAL INPUT")
category = st.sidebar.selectbox("Kategori", ["Kariyer", "Finans", "Sistem", "Eğitim"])
decision = st.sidebar.text_area("Karar / Analiz:")
outcome = st.sidebar.text_input("Beklenen Çıktı:")
risk_lvl = st.sidebar.select_slider("Risk Seviyesi", options=["Safe", "Low", "Moderate", "Critical"])

if st.sidebar.button("VERİTABANINA ENJEKTE ET"):
    db.add_decision(category, decision, outcome, risk_lvl)
    st.sidebar.balloons() # Küçük bir kutlama

# --- ANA PANEL: SİSTEM METRİKLERİ ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📡 Real-time Telemetry")
    cpu, ram, alert = monitor.get_metrics()
    
    st.metric(label="CPU LOAD", value=f"{cpu}%", delta="SİSTEM AKTİF")
    st.metric(label="RAM USAGE", value=f"{ram}%", delta="STABİL")
    
    if alert:
        st.error("🚨 SİSTEM KRİTİK EŞİKTE! Kaynakları kontrol et.")
    else:
        st.success("🛰️ Tüm sistemler nominal.")

with col2:
    st.subheader("📈 Verimlilik Analizi")
    # Havalı bir Plotly grafiği ekleyelim (Sadece görsel şov için)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = cpu,
        title = {'text': "İşlemci Gücü"},
        gauge = {'axis': {'range': [None, 100]},
                 'bar': {'color': "#00f3ff"},
                 'steps' : [
                     {'range': [0, 70], 'color': "lightgray"},
                     {'range': [70, 90], 'color': "gray"},
                     {'range': [90, 100], 'color': "red"}]}
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "#00f3ff"})
    st.plotly_chart(fig, use_container_width=True)

# --- ALT PANEL: VERİTABANI ANALİZİ ---
st.markdown("---")
st.subheader("📑 Arşivlenmiş Kararlar & Loglar")
with DatabaseManager().get_connection() as conn: # db_manager'a get_connection eklediğini varsayıyoruz
    query = "SELECT date, category, decision_text, risk_level FROM decisions ORDER BY id DESC"
    df = pd.read_sql_query(query, conn)
    st.dataframe(df.style.highlight_max(axis=0, color='#1a1a1a'))
