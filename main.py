import streamlit as st
import pandas as pd
from database_manager import DatabaseManager
from system_monitor import SystemMonitor
import time

# Sayfa Yapılandırması
st.set_page_config(page_title="Sentinel-V", layout="wide")
db = DatabaseManager()
monitor = SystemMonitor()

st.title("🛡️ Sentinel-V: Intelligent OS & Decision Hub")
st.markdown("---")

# Yan Menü (Sidebar) - Veri Girişi
st.sidebar.header("🧠 Yeni Karar Kaydı")
category = st.sidebar.selectbox("Kategori", ["Kariyer", "Finans", "Eğitim", "Sağlık"])
decision = st.sidebar.text_area("Karar Nedir?")
outcome = st.sidebar.text_input("Beklenen Sonuç?")
risk_lvl = st.sidebar.select_slider("Risk Seviyesi", options=["Düşük", "Orta", "Yüksek", "Kritik"])

if st.sidebar.button("Sisteme İşle"):
    db.add_decision(category, decision, outcome, risk_lvl)
    st.sidebar.success("Karar veritabanına güvenli şekilde işlendi.")

# Ana Panel - Sistem Durumu
col1, col2, col3 = st.columns(3)
cpu, ram, alert = monitor.get_metrics()

with col1:
    st.metric("CPU Yükü", f"%{cpu}", delta="-2%" if cpu < 50 else "+5%", delta_color="inverse")
with col2:
    st.metric("RAM Kullanımı", f"%{ram}")
with col3:
    status = "🚨 KRİTİK" if alert else "✅ STABİL"
    st.metric("Sistem Sağlığı", status)

# Veritabanı Görüntüleme (Analiz Kısmı)
st.subheader("📋 Geçmiş Kararlar ve Analitik")
with sqlite3.connect("sentinel_data.db") as conn:
    df = pd.read_sql_query("SELECT * FROM decisions ORDER BY id DESC LIMIT 5", conn)
    st.table(df)

# Otomatik Yenileme (Sistem izleme için)
if st.checkbox("Canlı İzlemeyi Başlat"):
    while True:
        cpu, ram, alert = monitor.get_metrics()
        db.log_system(cpu, ram, alert)
        time.sleep(5) # 5 saniyede bir logla
