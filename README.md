# 🛡️ Sentinel-V | Personal Intelligence & System Watcher

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Database](https://img.shields.io/badge/SQL-PostgreSQL%2FSQLite-orange)
![License](https://img.shields.io/badge/License-Apache%202.0-red)

> **"Veriyle yönetilmeyen bir hayat, optimize edilemez."**

Sentinel-V, günlük kararlarınızı, sistem sağlığınızı ve kişisel verimliliğinizi tek bir otonom yapıda birleştiren bir **Karar Destek Sistemi (DSS)** ve **Sistem Gözlemcisi**'dir. Bir MIS (Yönetim Bilişim Sistemleri) vizyonuyla, karmaşayı veriye dönüştürmek için tasarlanmıştır.

---

## 🚀 Temel Özellikler

* **🧠 Decision Ledger (Karar Defteri):** Günlük kritik kararları kaydeder, başarı olasılığını tahmin eder ve geçmiş hatalardan ders çıkarır.
* **📊 Live System Metrics:** Sistem (CPU, RAM, Disk) sağlığını anlık izleyerek kriz anlarını önceden raporlar.
* **🛡️ Autonomous Safeguard:** Kritik kaynak tüketimi tespit edildiğinde otomatik uyarılar (Telegram/Slack) gönderir.
* **📈 SQL Intelligence:** Tüm olayları ilişkisel bir veritabanında saklayarak haftalık "Verimlilik ve Risk Analizi" raporu sunar.

---

## 🛠️ Teknoloji Yığını

- **Dil:** Python (Core Logic)
- **Veritabanı:** SQL (SQLite for local / PostgreSQL for scale)
- **Arayüz:** Streamlit (Dynamic Dashboard)
- **Analiz:** Pandas & Scikit-learn (Behavioral Analytics)

---

## ⚠️ Risk Analizi & Güvenlik (SysOps Perspective)

Bu proje, bir Sistem Operasyonları uzmanının titizliğiyle yapılandırılmıştır:
1. **Data Leak Prevention:** `.gitignore` ile tüm hassas veriler (`.env`, `*.db`) yerel ortamda izole edilmiştir.
2. **Circuit Breaker:** Sistem kaynakları %90'ın üzerine çıktığında otomatik "Mola Modu" devreye girer.
3. **Privacy by Design:** Hiçbir kişisel veri üçüncü taraf bulut servislerine anonimleştirilmeden gönderilmez.

---

## 📂 Dosya Yapısı

```text
├── main.py            # Dashboard ve giriş ekranı
├── core/
│   ├── monitor.py     # Sistem izleme motoru
│   └── brain.py       # Karar analiz algoritmaları
├── database/
│   └── schema.sql     # Veritabanı mimarisi
├── .env.example       # Örnek çevre değişkenleri
└── .gitignore         # Güvenlik kalkanı
