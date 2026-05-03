import numpy as np
import matplotlib.pyplot as plt

# --- Genel Ayarlar ---
plt.rcParams['figure.figsize'] = [15, 5]

# 1. FONKSİYON: f(x) = x^2 + 5
# Parametreler: x0=10, alpha=0.1, iter=100, tol=1e-5
f1 = lambda x: x**2 + 5
df1 = lambda x: 2 * x
x0_1, alpha_1, iter_1, tol_1 = 10, 0.1, 100, 1e-5

x1 = x0_1
hist1 = [x1]
for _ in range(iter_1):
    nx1 = x1 - alpha_1 * df1(x1)
    if abs(nx1 - x1) < tol_1: break
    x1 = nx1
    hist1.append(x1)

# 2. FONKSİYON: f(x,y) = x^2 + y^2
# Parametreler: x0=(3,3), alpha=0.01, iter=500, tol=1e-5
f2 = lambda x, y: x**2 + y**2
df2 = lambda p: np.array([2 * p[0], 2 * p[1]])
x0_2, alpha_2, iter_2, tol_2 = np.array([3.0, 3.0]), 0.01, 500, 1e-5

p2 = x0_2
hist2 = [p2]
for _ in range(iter_2):
    np2 = p2 - alpha_2 * df2(p2)
    if np.linalg.norm(np2 - p2) < tol_2: break
    p2 = np2
    hist2.append(p2)
hist2 = np.array(hist2)

# 3. FONKSİYON: f(x) = x^4 - 5x^2 + 4
# Parametreler: x0=0.5, alpha=0.005, iter=1000, tol=1e-6
f3 = lambda x: x**4 - 5*x**2 + 4
df3 = lambda x: 4 * x**3 - 10 * x
x0_3, alpha_3, iter_3, tol_3 = 0.5, 0.005, 1000, 1e-6

x3 = x0_3
hist3 = [x3]
for _ in range(iter_3):
    nx3 = x3 - alpha_3 * df3(x3)
    if abs(nx3 - x3) < tol_3: break
    x3 = nx3
    hist3.append(x3)

# --- FONKSİYON TANIMLARI ---
f2 = lambda x, y: x**2 + y**2
df2 = lambda p: np.array([2 * p[0], 2 * p[1]])

f3 = lambda x: x**4 - 5*x**2 + 4
df3 = lambda x: 4 * x**3 - 10 * x

def run_gd(df, x0, alpha, iterations):
    x = x0
    hist = [x]
    for _ in range(iterations):
        grad = df(x)
        x = x - alpha * grad
        hist.append(x)
        if np.linalg.norm(grad) > 1e10: break # Patlama kontrolü
    return np.array(hist)

# --- SENARYOLARIN HAZIRLANMASI ---

# Senaryo A: Başlangıç Noktası Duyarlılığı ve Yerel Minimum (3. Fonksiyon)
# x0 = 0.5 iken yerel çukura takılır, x0 = 2.0 iken küresel minimumu bulur
hist3_local = run_gd(df3, 0.5, 0.005, 1000)
hist3_global = run_gd(df3, 2.0, 0.005, 1000)
hist3_zero = run_gd(df3, 0.0, 0.005, 100) # Gradyan 0 durumu

# Senaryo B: Büyük Öğrenme Oranı (Alpha) Sorunu (2. Fonksiyon)
# alpha = 0.01 (Normal), alpha = 1.1 (Hedefin etrafında zıplama/uzaklaşma)
hist2_normal = run_gd(df2, np.array([3.0, 3.0]), 0.01, 50)
hist2_bad = run_gd(df2, np.array([3.0, 3.0]), 1.05, 10)

# --- GÖRSELLEŞTİRME ---
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# GRAFİK 1: Yerel Minimum ve Başlangıç Noktası Sorunu
_x3 = np.linspace(-2.5, 2.5, 200)
axes[0].plot(_x3, f3(_x3), 'k', alpha=0.3)
axes[0].plot(hist3_local, f3(hist3_local), 'ro-', label='x0=0.5: Yerel Çukura Takıldı', markersize=4)
axes[0].plot(hist3_global, f3(hist3_global), 'go-', label='x0=2.0: Küresel Minimum', markersize=4)
axes[0].scatter([0], [f3(0)], color='blue', s=100, label='x0=0.0: Hareket Yok (Gradyan 0)', zorder=5)
axes[0].set_title("Hata 1: Yerel Minimum ve Başlangıç Noktası Duyarlılığı")
axes[0].legend()

# GRAFİK 2: Hatalı Öğrenme Oranı (Zıplama Etkisi)
_x2 = np.linspace(-4, 4, 100)
_y2 = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(_x2, _y2)
axes[1].contour(X, Y, f2(X, Y), levels=15, cmap='viridis')
axes[1].plot(hist2_normal[:,0], hist2_normal[:,1], 'go-', label='Doğru Alpha (0.01)')
axes[1].plot(hist2_bad[:,0], hist2_bad[:,1], 'rx--', label='Büyük Alpha (1.05): Zıplama/Uzaklaşma')
axes[1].set_title("Hata 2: Öğrenme Oranı Gereğinden Büyük Seçildiğinde[cite: 1]")
axes[1].legend()

plt.tight_layout()
plt.show()    

# --- GÖRSELLEŞTİRME ---
fig = plt.figure(figsize=(18, 5))

# Grafik 1: Basit Parabol
ax1 = fig.add_subplot(1, 3, 1)
_x = np.linspace(-11, 11, 100)
ax1.plot(_x, f1(_x), 'k--', alpha=0.5)
ax1.plot(hist1, [f1(i) for i in hist1], 'ro-', markersize=4, label='Adımlar')
ax1.set_title("1. Fonksiyon: $f(x)=x^2+5$\n(Hızlı Yakınsama)")
ax1.legend()

# Grafik 2: İki Değişkenli Yüzey (Kontur Haritası)
ax2 = fig.add_subplot(1, 3, 2)
_x = np.linspace(-3.5, 3.5, 100)
_y = np.linspace(-3.5, 3.5, 100)
X, Y = np.meshgrid(_x, _y)
Z = f2(X, Y)
cp = ax2.contour(X, Y, Z, levels=20)
ax2.plot(hist2[:, 0], hist2[:, 1], 'ro-', markersize=3, label='Yol')
ax2.set_title("2. Fonksiyon: $f(x,y)=x^2+y^2$\n(Merkeze Yönelme)")
ax2.legend()

# Grafik 3: Yerel Extremum Noktaları
ax3 = fig.add_subplot(1, 3, 3)
_x = np.linspace(-2.5, 2.5, 100)
ax3.plot(_x, f3(_x), 'k--', alpha=0.5)
ax3.plot(hist3, [f3(i) for i in hist3], 'ro-', markersize=4, label='Adımlar')
ax3.set_title("3. Fonksiyon: $f(x)=x^4-5x^2+4$\n(Yerel Çukura Takılma)")
ax3.legend()

plt.tight_layout()
plt.show()