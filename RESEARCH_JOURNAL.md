# 📓 Research & Development Journal (Araştırma ve Öğrenme Günlüğü)
### *E-Commerce Logistics AI Decision Support System*
**Yazar:** Ayşenur Yeşilova  
**Danışman / Mentor:** Barbaros Bey  
**Süre:** 4 Hafta (28 Günlük Öğrenme ve Gelişim Yolculuğu)  

---

## 🎯 Başlangıç Noktası ve Yetkinlik Analizi (Day 0 Baseline)
- **Mevcut Bilgi Seviyesi:** Veri bilimi, makine öğrenmesi (XGBoost, Scikit-Learn), Python, Streamlit, Öneri Sistemleri ve E-ticaret veri kümeleri (TEKNOFEST Hackathon deneyimi).
- **Bilgi Açığı (Neyi Bilmiyordum?):**
  1. Çok Kriterli Karar Verme (MCDM) metodolojilerinin (SWARA ve COBRA) lojistik ve kargo seçiminde matematiksel olarak nasıl formüle edildiği.
  2. Donanım seviyesinde (Edge AI) çalışan yerel LLM mimarileri (Azure Foundry Local SDK, WinML) ve API olmadan çalışabilen True RAG (Retrieval-Augmented Generation) boru hatları.
  3. Lojistik sektöründeki "görünmeyen" gerçek operasyonel darboğazlar: Sadece teslimat süresi değil; kargo firması SLA ihlalleri, iade lojistiği maliyeti, eyaletler arası transfer risk skorları.

---

## 🗓️ 1. HAFTA: Sektörel Problem Keşfi ve Literatür Taraması (Gün 1 - 7)

### 📌 Gün 1-3: E-Ticaret Lojistiğinde Gerçek Dünya Problemlerinin Keşfi
- **Yapılan Çalışma:** Brezilya Olist E-Ticaret ekosistem veri kümesi (113,000+ sipariş) üzerinde EDA (Açıklayıcı Veri Analizi) yapıldı.
- **Keşfedilen Operasyonel Darboğazlar:**
  - Kargo seçiminin sadece "en ucuz" veya "en hızlı" firma olarak yapılamayacağı; mesafe, müşteri memnuniyet skoru, gecikme riski ve rota yoğunluğunun bir arada değerlendirilmesi gerektiği görüldü.
  - SP (São Paulo) eyaletinin lojistik merkezi olduğu ancak RJ (Rio de Janeiro) ve Kuzey eyaletlerine (AM, AC) giden rotalarda gecikme risk skoru ve maliyetin dramatik şekilde yükseldiği tespit edildi.

### 📌 Gün 4-7: Literatür İncelemesi ve Yöntem Seçimi
- **İncelenen Çalışmalar:**
  - Güler, A. (2025). *SWARA ve COBRA yöntemleriyle çok kriterli sıralama analizi*.
  - E-ticaret son kilometre (last-mile) teslimatlarında yapay zeka ve hibrit MCDM yaklaşımları.
- **Sektörel ve Teknik Boşluk (The Gap):**
  - Geleneksel lojistik sistemleri ya sadece kural tabanlı (if-else) ya da tek bir ML modelinin (ör. XGBoost) ürettiği "siyah kutu" skorlara dayanmaktadır.
  - **Bizim Katkımız:** SWARA (uzman ağırlıklandırması) + COBRA (ideal çözüme mesafe sıralaması) matematiksel çekirdeğini, yerel çalışan bir LLM RAG analisti ile birleştirerek karar vericiye **açıklanabilir ve doğal dilde strateji sunan** bir platform inşa etmek.

---

## 🗓️ 2. HAFTA: Veri Mühendisliği ve Matematiksel Karar Çekirdeği (Gün 8 - 14)

### 📌 Gün 8-10: İlişkisel Veri Boru Hattının Kurulması (`veri_isleme.py` & `lojistik.db`)
- **Veri Mühendisliği:**
  - 8 farklı Olist CSV dosyası (`orders`, `items`, `reviews`, `sellers`, `customers`, `products`, `geolocation`) birleştirildi.
  - Eyaletler arası nokta-nokta rotalar (ör. `SP -> RJ`, `SP -> MG`) bazında `Toplam_Siparis`, `Ortalama_Hiz_Gun`, `Ortalama_Maliyet_Real`, `Ortalama_Memnuniyet_Skoru` metrikleri aggregation ile çıkarıldı.
  - Veri `lojistik.db` SQLite veritabanına dönüştürüldü.

### 📌 Gün 11-14: SWARA-COBRA Matematiksel Karar Motorunun Kodlanması
- **SWARA Algoritması:** Uzman tercihlerine göre kriterlerin bağıl önem oranlarının ($s_j$, $k_j$, $q_j$, $w_j$) hesaplanması sağlandı.
- **COBRA Algoritması (Güler, 2025):**
  - Maliyet (Cost) ve Fayda (Benefit) kriterleri ayrı ayrı normalize edildi.
  - Pozitif İdeal Çözüm (PIS), Negatif İdeal Çözüm (NIS) ve Ortalama Çözüm (AS) mesafeleri (Euclidean & Absolute) hesaplanarak `dC` skoru türetildi.
  - Rotalar optimum verimliliğe göre sıralandı.

---

## 🗓️ 3. HAFTA: Yerel LLM, Azure Foundry Local ve True RAG Entegrasyonu (Gün 15 - 21)

### 📌 Gün 15-18: Microsoft Foundry Local SDK ve Donanım Katmanı
- **Edge AI Mimarisi:** Bulut API'lerine (OpenAI vb.) bağımlı kalmadan, veri gizliliğini %100 koruyan yerel donanım üzerinde `phi` dil modelini çalıştıracak `foundry_local_sdk` ve `WinML` mimarisi sarmalandı.
- **Güvenli Fallback Mekanizması:** Donanımda yerel model kurulamazsa dahi uygulamanın kesintisiz çalışması için akıllı bir varsayılan analist raporlama katmanı tasarlandı.

### 📌 Gün 19-21: Gerçek RAG (Retrieval-Augmented Generation) Boru Hattı
- **Vektörel Arama & Bağlam Oluşturma:**
  - Yöneticinin doğal dildeki sorgusu (ör. *"Bütçem kısıtlı, en memnuniyeti yüksek hat hangisi?"*) vektörleştirilip Scikit-Learn Cosine Similarity ile veritabanındaki en yakın rotalarla (Top-K) eşleştirildi.
  - Seçilen rotaların metrikleri dinamik bir System Prompt Context yapısına dönüştürülüp yerel LLM'e beslendi.

---

## 🗓️ 4. HAFTA: Yönetici Paneli, Simülasyon Motoru ve Sunum Hazırlığı (Gün 22 - 28)

### 📌 Gün 22-25: İnteraktif Streamlit Yönetici Paneli
- **Arayüz Tasarımı:**
  - **Tab 1:** Akademik COBRA Sıralama Matrisi, renk ölçekli tablo ve dinamik grafikler.
  - **Tab 2:** Doğal dilde soru sorulabilen True RAG Analist Chat ekranı.
  - **Tab 3:** Metodoloji ve Akademik Rapor Özeti.
  - **Sidebar:** Uzmanların kriter ağırlıklarını canlı değiştirebildiği SWARA Ayar Paneli.

### 📌 Gün 26-28: Testler, Dokümantasyon ve Final Sunum Videosu Hazırlığı
- **Sistem Doğrulaması:** Veri akış hatları, RAG sorgu doğruluğu ve COBRA sıralama kararlılığı test edildi.
- **Çıktılar:** GitHub deposu güncellendi, `README.md`, `LITERATURE_SURVEY.md` ve 5 dakikalık sunum senaryosu (`PRESENTATION_SCRIPT.md`) tamamlandı.

---

## 💡 Sonuç ve Kazanımlar (Key Learnings)
1. **Sektörel Bakış Açısı:** Bir projenin değerinin yazılan kod miktarından değil, çözdüğü gerçek operasyonel problemden ve sağladığı karar desteğinden kaynaklandığını kavradım.
2. **Yerel Yapay Zeka (Edge AI):** Veri mahremiyetinin kritik olduğu lojistik ve finans sektörlerinde Azure Foundry Local / WinML gibi yerel LLM teknolojilerinin geleceğin standardı olduğunu deneyimledim.
3. **Hibrit Mimarı:** Yapay zekayı (LLM) tek başına bir karar mercii yapmak yerine; matematiksel optimizasyon (SWARA-COBRA) ile birleştirip LLM'i "açıklayıcı ve stratejik analist" olarak kullanmanın en güvenilir yaklaşım olduğunu öğrendim.
