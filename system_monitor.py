import psutil

class SystemMonitor:
    @staticmethod
    def get_metrics():
        """CPU ve RAM verilerini çeker, kritik eşik kontrolü yapar."""
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        
        # Risk Analizi: Eşik değerlerini burada kontrol ediyoruz
        is_alert = False
        if cpu > 85 or ram > 90:
            is_alert = True
            
        return cpu, ram, is_alert

    @staticmethod
    def get_risk_report():
        """Disk ve ağ trafiği gibi daha derin veriler."""
        disk = psutil.disk_usage('/').percent
        return f"Disk Doluluğu: %{disk}"
