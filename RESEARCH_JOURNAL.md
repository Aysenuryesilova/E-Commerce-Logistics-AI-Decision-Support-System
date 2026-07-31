# 📓 Research & Development Journal (Araştırma ve Öğrenme Günlüğü)
### *E-Commerce Logistics AI Decision Support System*
**Yazar:** Ayşenur Yeşilova  
**Danışman / Mentor:** Barbaros Bey  
**Süre:** 4 Hafta (28 Günlük Öğrenme ve Gelişim Yolculuğu + İnceleme Revizyonları)  

---

## 🎯 Başlangıç Noktası ve Yetkinlik Analizi (Day 0 Baseline)
- **Mevcut Bilgi Seviyesi:** Veri bilimi, makine öğrenmesi (XGBoost, Scikit-Learn), Python, Streamlit, TEKNOFEST Hackathon e-ticaret deneyimi.
- **Bilgi Açıkları:** SWARA-COBRA Çok Kriterli Karar Verme (MCDM) formülasyonu, Yerel LLM mimarisi (Azure Foundry Local / WinML), Taşıyıcı ve Rota kavramsal ayrımı, Hibrit RAG ve Query Router mimarisi.

---

## 🗓️ 1. HAFTA: Sektörel Problem Keşfi ve Literatür Taraması (Gün 1 - 7)
- **Problem Keşfi:** Olist veri setindeki teslimat aksamaları ve son km (last-mile) kargo risklerinin analizi.
- **Literatür Taraması:** Güler, A. (2025) SWARA-COBRA makalesi ve e-ticaret lojistiği SOTA incelemesi.

---

## 🗓️ 2. HAFTA: Veri Mühendisliği & SWARA-COBRA Matematiksel Motoru (Gün 8 - 14)
- **Veri Mühendisliği:** Olist tablolarının müşteri id (`customer_id`) ile hassas birleştirilmesi (Simpson Paradoksu önlemi).
- **SWARA & COBRA Geliştirmeleri:** 
  - SWARA ağırlıklarının toplamının **kesinlikle 1.0 ($\sum w_j = 1.0$)** olması zorunluluğu sağlandı.
  - COBRA denklemindeki Pozitif İdeal (PIS), Negatif İdeal (NIS) ve Ortalama Çözüm (AS+/AS-) Öklid mesafeleri Güler (2025) formülüne birebir oturtuldu.

---

## 🗓️ 3. HAFTA: Türkiye Lojistik Ekosistemi & Hibrit RAG Mimarisi (Gün 15 - 21)
- **Türkiye Veri Seti Entegrasyonu:** Türkiye 81 il lojistik hatları ve gerçek kargo firmaları (Yurtiçi Kargo, Aras Kargo, MNG Kargo, Trendyol Express, Sendeo) ile sentetik/yerel veri motoru (`turkiye_rota_performans`) inşa edildi.
- **Taşıyıcı ve Rota Ayrımı:** Rota başarısı (hat verimliliği) ile Taşıyıcı Firma başarısı iki bağımsız veri boyutu olarak ayrıldı.

---

## 🗓️ 4. HAFTA: Query Router, Görsel RAG & Yönetici Paneli (Gün 22 - 28)
- **Query Router Mimarisi:** Sayısal kargo soruları doğrudan **SQL Sorgu Motoruna**, serbest metinli sorular ise **Vektör Arama RAG Mimarisine** yönlendirildi.
- **Kaynak & Görsel Gösterimi:** Her RAG cevabının altına **Doğrulanmış Veritabanı Kaynak Tablosu** ve **Canlı Matplotlib Grafiği** eklendi.
- **Karar Motoru İzolasyonu:** SWARA-COBRA karar motoru, LLM'den %100 bağımsız saf matematiksel Python/NumPy algoritması olarak izole edildi.
