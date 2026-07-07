# Gerekli Kütüphaneler ve Veri Yapıları

## 1. Gerekli Kütüphaneler
Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:
- numpy
- scipy
- librosa
- rawpy
- pillow
- PyWavelets

Gereksinimleri yüklemek için şu komutu çalıştırabilirsiniz:
```bash
pip install -r requirements.txt
```

## 2. GitHub Kurulumu
Depoyu yerel bilgisayarınıza kopyalamak için:
```bash
git clone https://github.com/Turkuazzzo/Python-ile-Matematik
```
Gerekli yetkiler `korayaki@uludag.edu.tr` adresine verilmiştir.

## 3. Ses ve Görüntü Dosyası Yapıları

### Ses Dosyaları
- **Ham Ses Verisi (.wav):** Örnekleme hızı genellikle 48000 Hz olup stereo mikrofon kayıtlarında (N, 2) matrisi formatındadır.
- **İşlenmiş Ses Verisi (.mp3):** Sıkıştırılmış ses dosyasının veri formatı genellikle (N,) matrisi şeklindedir.

### Görüntü Dosyaları
- **Ham Görüntü Verisi (.png vb.):** Görüntü verileri, boyutlarına (genişlik, yükseklik, kanal) göre yapılandırılır. Örneğin (2314, 3474, 3) şeklinde bir RGB matrisi formatındadır.

## 4. Kullanılan Kütüphanelerin Açıklamaları
- **numpy:** Çok boyutlu diziler ve matrislerle çalışmak için temel bir paket.
- **scipy:** Bilimsel hesaplamalar ve mühendislik uygulamaları için.
- **librosa:** Ses ve müzik analizi için yaygın olarak kullanılan bir kütüphane.
- **rawpy:** RAW formatındaki resim dosyalarını işlemek için.
- **pillow:** Görüntü işleme (açma, dönüştürme, kaydetme vb.) için.
- **PyWavelets:** Ayrık Dalgacık Dönüşümü (DWT) işlemleri için.

## 5. Veritabanı ve Veri Seti
- **Veritabanı:** Bu projede bir veritabanı kullanılmamaktadır.
- **Veri Seti Linki:** .rar dosyası içerisinde bulunmaktadır.
