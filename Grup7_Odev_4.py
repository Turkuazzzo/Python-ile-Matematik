import math
import matplotlib.pyplot as plt

# --- 1. SABİTLER (Roket ve Ortam Değerleri) ---
GRAVITY = 9.80665  # Yerçekimi ivmesi (m/s^2)
MASS = 20.0        # Motor kapandıktan sonraki roket kütlesi (kg)
RHO = 1.0          # Hava yoğunluğu (kg/m^3)
CD = 0.45          # Sürtünme katsayısı
AREA = 0.018       # Kesit alanı (m^2)

# İşlem yükünü azaltmak için önceden hesaplanan aerodinamik sabit
K_CONSTANT = 0.5 * RHO * CD * AREA


# --- 2. MODÜLER FONKSİYONLAR ---

def calculate_estimated_apogee(current_altitude, current_velocity):
    """
    Algoritma Açıklaması: Anlık irtifa ve dikey hızı kullanarak, 
    roketin hava sürtünmesi ve yerçekimi etkisi altında çıkacağı tahmini tepe noktasını (apogee) hesaplar.
    """
    # Roket zaten düşüşe geçmişse, mevcut irtifayı maksimum olarak kabul et
    if current_velocity <= 0.0: # Mevcut hızı 0 veya negatifse, roket yükselmeyi bırakmış demektir (Yerçekimi vektörüyle aynı yönde hareket ediyor)
        return current_altitude
    
    # Matematiksel diferansiyel denklemin Python uyarlaması
    term1 = MASS / (2.0 * K_CONSTANT)
    term2 = 1.0 + ((K_CONSTANT * current_velocity**2) / (MASS * GRAVITY))
    
    # Ekstra çıkılacak irtifa (delta_h)
    delta_h = term1 * math.log(term2) # Mevcut irtifanın üzerine çıkılacak ekstra irtifa miktarı (delta_h) F = ma prensibinden elde edilmiş formüldür
    
    # Tahmini Apogee = Anlık İrtifa + Çıkılacak Ekstra İrtifa
    return current_altitude + delta_h

def get_mock_flight_data():
    """
    Örnek Senaryo: Motor kapandıktan sonra saniye saniye değişen 
    (Zaman, İrtifa, Dikey Hız) değerlerini simüle eder.
    """
    return [
        (0.0, 1000.0, 300.0),
        (0.5, 1145.0, 280.0),
        (1.0, 1280.0, 261.0),
        (1.5, 1405.0, 243.0),
        (2.0, 1522.0, 226.0),
        (2.5, 1630.0, 210.0),
        (3.0, 1730.0, 195.0),
        (3.5, 1823.0, 180.0),
        (4.0, 1908.0, 166.0)
    ]

# CSV dosyası oluşturma ve yazma işlemi (isteğe bağlı)

"""
csv_dosya = "ucus_loglari.csv"
fieldnames = ['zaman', 'irtifa', 'hiz']
"""

# --- 3. ANA AKIŞ VE İŞLEM HATTI ---

def main():
    print("Yüksek İrtifa Roketi - Apogee Tahmin Simülasyonu Başlatılıyor...\n")
    
    # Örnek senaryo verilerini çek
    flight_data = get_mock_flight_data()
    
    # Grafik için listeler
    times = []
    actual_altitudes = []
    predicted_apogees = []
    
    # Tablo başlığı (Ara çıktı üretimi)
    print(f"{'Zaman (s)':<10} | {'Anlık İrtifa (m)':<18} | {'Anlık Hız (m/s)':<18} | {'Tahmini Apogee (m)':<18}")
    print("-" * 72)
    
    # İşlem hattının baştan sona çalıştırılması
    for t, alt, vel in flight_data:
        # Hesaplama Modülü
        pred_apogee = calculate_estimated_apogee(alt, vel)
        
        # Grafik için verileri kaydet
        times.append(t)
        actual_altitudes.append(alt)
        predicted_apogees.append(pred_apogee)
        
        # Tablo formatında ekrana yazdır
        print(f"{t:<10.1f} | {alt:<18.1f} | {vel:<18.1f} | {pred_apogee:<18.1f}")
        
    print("\nSimülasyon tamamlandı. Grafik oluşturuluyor...")

    # Başarı Ölçütü: Somut Grafik Çıktısı Üretimi
    plt.figure(figsize=(10, 6))
    plt.plot(times, actual_altitudes, label="Anlık İrtifa (Sensör Verisi)", marker='o', color='blue')
    plt.plot(times, predicted_apogees, label="Tahmini Tepe Noktası (Hesaplanan)", linestyle='--', marker='x', color='red')
    
    plt.title("Uçuş Senaryosu: Anlık İrtifa ve Apogee Tahmini Değişimi")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("İrtifa (metre)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    # Grafiği ekranda göster
    plt.show()

if __name__ == "__main__":
    main()