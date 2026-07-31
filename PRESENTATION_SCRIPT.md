# 🎬 5-Minute Final Presentation Video Script & Guide
### *Akıllı E-Ticaret Lojistik Karar Destek Sistemi*
**Hazırlayan:** Ayşenur Yeşilova  
**Hedef Kitle:** Barbaros Bey, Değerlendirme Jürisi ve Github Topluluğu  

---

## ⏱️ Video Süre Akışı ve Konuşma Metni Outline

```
[0:00 - 0:45] ── 1. Giriş, Tanışma ve Sektörel Problem Metni
[0:45 - 1:30] ── 2. Literatür Taraması ve Projenin Özgün Değeri (The Gap)
[1:30 - 3:00] ── 3. Sistem Mimarısı: SWARA-COBRA Matematiksel Motorü & True RAG
[3:00 - 4:15] ── 4. Canlı Ekran Gösterimi & Senaryo Simülasyonu (Live Demo)
[4:15 - 5:00] ── 5. Gelişim Yolculuğu, Öğrenilenler ve Kapanış
```

---

### 🎙️ 1. GİRİŞ VE SEKTÖREL PROBLEM METNİ (0:00 - 0:45)
- **Ekran Gösterimi:** Proje Başlık Slaydı / GitHub Depo Arayüzü.
- **Konuşma Metni:**
  > *"Merhaba Barbaros Bey ve değerli jüri üyeleri, ben Ayşenur Yeşilova. Bu projede e-ticaret sektörünün en kritik maliyet ve memnuniyet kalemi olan **Kargo ve Rota Seçim Problemini** uçtan uca çözen **Akıllı E-Ticaret Lojistik Karar Destek Sistemi**'ni geliştirdim.*
  > 
  > *E-ticarette kargo seçimi genelde sadece fiyat üzerinden yapılır. Ancak bu durum teslimat gecikmelerine, müşteri şikayetlerine ve ciddi iade maliyetlerine yol açar. Ben projeye başlamadan önce sektörün gerçek darboğazlarını ve veritabanlarında görünmeyen risk skorlarını analiz ederek yola çıktım."*

---

### 🎙️ 2. LİTERATÜR TARAMASI VE ÖZGÜN DEĞER / THE GAP (0:45 - 1:30)
- **Ekran Gösterimi:** `LITERATURE_SURVEY.md` ve Karşılaştırma Tablosu.
- **Konuşma Metni:**
  > *"Araştırma sürecimde Güler (2025) tarafından yayınlanan SWARA ve COBRA çok kriterli karar verme metodolojilerini inceledim. Mevcut akademik ve endüstriyel çözümlerde iki temel eksiklik gördüm:*
  > 
  > *Birincisi, makine öğrenmesi modelleri sadece sayısal tahmin üretir ama yöneticiye gerekçeyi açıklayamaz.*
  > *İkincisi, bulut tabanlı yapay zekalar şirket veri gizliliğini ihlal edebilir.*
  > 
  > *Benim geliştirdiğim sistem ise **SWARA-COBRA matematiksel optimizasyonunu** ve **Microsoft Foundry Local SDK** ile cihaz üzerinde (Edge AI) çalışan **True RAG** dil analistini hibrit olarak birleştiriyor."*

---

### 🎙️ 3. SİSTEM MİMARİSİ VE TEKNİK DETAYLAR (1:30 - 3:00)
- **Ekran Gösterimi:** README Mimari Şeması ve Kod Yapısı (`app.py`, `veri_isleme.py`).
- **Konuşma Metni:**
  > *"Sistem mimarimiz 3 temel katmandan oluşuyor:*
  > 
  > *1. **Veri Mühendisliği Katmanı:** Brezilya Olist e-ticaret veri kümesindeki 113.000'den fazla sipariş işlenerek SQLite veritabanına aktarıldı ve eyalet bazlı lojistik performans metrikleri çıkarıldı.*
  > *2. **SWARA-COBRA Motoru:** Teslimat Hızı, Maliyet ve Memnuniyet parametreleri uzman ağırlıklarıyla COBRA matrisine sokularak ideal çözüme olan Euclidean mesafeleri hesaplandı.*
  > *3. **Yerel True RAG Katmanı:** Yöneticinin doğal dildeki talebi vektörel arama ile eşleştirilip yerel LLM (`phi`) modeline beslenerek bağımsız bir analist raporu üretildi."*

---

### 🎙️ 4. CANLI UYGULAMA GÖSTERİMİ / LIVE DEMO (3:00 - 4:15)
- **Ekran Gösterimi:** Çalışan Streamlit Arayüzü (`app.py`).
- **Konuşma Metni:**
  > *"Şimdi uygulamamızı canlı üzerinde inceleyelim.*
  > 
  > *Sol taraftaki panelden lojistik müdürü olarak kriter önem sıralamamızı değiştirebiliyoruz. Örneğin teslimat hızının önemini artırdığımızda COBRA matrisi anında güncelleniyor ve optimum rotaları yeşilden kırmızıya skorluyor.*
  > 
  > *RAG Analisti sekmesinde ise doğal dilde soru sorabiliyoruz: 'Bütçemiz kısıtlı, en ucuz ve memnuniyeti yüksek hat hangisidir?' Sistem veritabanındaki en alakalı rotaları getiriyor ve yerel AI modeli bize stratejik bir analist raporu sunuyor."*

---

### 🎙️ 5. 4 HAFTALIK ÖĞRENME YOLCULUĞU VE KAPANIŞ (4:15 - 5:00)
- **Ekran Gösterimi:** `RESEARCH_JOURNAL.md` ve Sonuç Ekranı.
- **Konuşma Metni:**
  > *"Bu 4 haftalık süreçte sadece kod yazmayı değil; sektörel bir problemi tanımlamayı, literatürdeki boşluğu bulmayı, Edge AI ve yerel LLM teknolojilerini matematiksel karar modelleriyle birleştirmeyi öğrendim. Tüm gelişim sürecimi gün gün `RESEARCH_JOURNAL.md` dosyamda dokümante ettim.*
  > 
  > *Bana bu araştırmacı ve ürün odaklı bakış açısını kazandırdığınız için Barbaros Bey'e teşekkür ederim. Dinlediğiniz için teşekkürler!"*
