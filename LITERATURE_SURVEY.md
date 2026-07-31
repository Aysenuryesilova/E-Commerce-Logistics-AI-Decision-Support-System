# 📚 Literature Survey & Market Benchmark (Literatür Taraması ve Sektörel Boşluk Analizi)

## 📌 1. Giriş ve Sektörel Problem Metni
E-ticaret ekosisteminde kargo ve lojistik operasyonları, müşteri memnuniyetini ve şirket karlılığını doğrudan etkileyen en kritik bileşendir. Son km (last-mile) teslimat süreçlerinde karşılaşılan aksamalar; müşteri terk oranlarını artırmakta, iade maliyetlerini katlamakta ve kargo firması SLA (Service Level Agreement) ihlallerine yol açmaktadır.

Geleneksel kararlarda kargo firması veya rota seçimi genellikle yalnızca **birim teslimat fiyatı** veya **tahmini teslimat süresi** gibi tek boyutlu kriterlere göre yapılmaktadır. Ancak gerçek dünyada:
- Teslimat süresi düşük olan bir rota yüksek gecikme riski taşıyabilir.
- Maliyeti ucuz olan bir firma düşük müşteri memnuniyet skoruna sahip olabilir.
- Bölgesel coğrafi zorluklar (ör. Brezilya Amazon bölgesi veya Türkiye Doğu Anadolu transfer noktaları) ek risk skoru yaratmaktadır.

---

## 🔬 2. Literatür İncelemesi (Academic Literature Review)

### A. Çok Kriterli Karar Verme (MCDM) Metodolojileri
- **Güler, A. (2025).** *Türkiye’deki bilişim sistemleri ve teknolojileri bölümlerinin SWARA yöntemi ile ağırlıklandırılması ve COBRA yöntemiyle sıralanması.* Uluslararası Avrasya Sosyal Bilimler Dergisi, 16(60), 825-840.
  - **İnceleme:** Güler (2025), subjektif uzman tercihlerinin SWARA (Step-wise Weight Assessment Ratio Analysis) ile ağırlıklandırılıp, COBRA (COmprehensive Distance Based Ranking) ile hem Pozitif (PIS), hem Negatif (NIS), hem de Ortalama Çözüme (AS) göre mesafelerin hesaplanarak alternatiflerin sıralanabileceğini kanıtlamıştır.
  - **Lojistiğe Uyarlanması:** Teslimat Hızı (Cost - Düşük iyi), Operasyonel Maliyet (Cost - Düşük iyi) ve Müşteri Memnuniyeti (Benefit - Yüksek iyi) parametreleri COBRA matrisine dahil edilerek en optimum rota skorlanmıştır.

### B. E-Ticaret Lojistiğinde Yapay Zeka ve Tahminleme
- **Olist E-Commerce Benchmark Çalışmaları (Kaggle & Academic Datasets):**
  - Brezilya e-ticaret ağındaki 100,000'den fazla sipariş üzerinde yapılan çalışmalarda (XGBoost, Random Forest, CatBoost), teslimat sürelerinin coğrafi mesafe ve satıcı-müşteri eyalet çiftlerine yüksek bağımlı olduğu gösterilmiştir.

### C. Yerel LLM, RAG ve Agentic AI Mimarları (2025-2026 Paradigm Değişimi)
- **Microsoft Foundry Local & WinML Architecture:**
  - Veri gizliliğinin ön planda olduğu kurumsal sistemlerde (bankacılık, lojistik, savunma), bulut LLM servisleri yerine cihaz üzerinde (Edge AI) çalışan modeller tercih edilmektedir.
  - **Retrieval-Augmented Generation (RAG):** Vektör veritabanından alınan bağlamın LLM'e beslenmesi ile dil modelinin halüsinasyon görmesi engellenmekte ve %100 deterministik raporlama sağlanmaktadır.

---

## 🎯 3. Sektörel ve Teknik Boşluk (The Gap)

Mevcut açık kaynak kodlu ve akademik kargo karar sistemleri incelendiğinde şu eksiklikler tespit edilmiştir:

| İncelenen Sistem Türü | Sınırlılık / Boşluk | Bizim Projemizin Katkısı (Value-Add) |
| :--- | :--- | :--- |
| **Klasik Kural Motorları (If-Else)** | Statiktir, dinamik uzman tercihlerini (SWARA) adapte edemez. | Uzman paneli ile canlı ağırlıklandırılabilen **SWARA-COBRA Engine** entegre edilmiştir. |
| **Tekil ML Tahmin Modelleri** | "Siyah kutu" tahmin verir. Kararın **neden** alındığını yöneticiye açıklayamaz. | **True RAG & Local LLM Analisti** eklenerek doğal dilde gerekçelendirilmiş strateji raporu üretilmektedir. |
| **Bulut Tabanlı LLM Çözümleri** | Şirket veri mahremiyetini riske atar, yüksek API maliyeti oluşturur. | **Microsoft Foundry Local / Edge AI** mimarisi ile sıfır veri sızıntısı ve yerel donanım üzerinde çalışma sağlanmıştır. |

---

## 🚀 4. Projemizin Özgün Değeri (Core Innovation)

Bu proje, kargo ve lojistik seçim problemini **matematiksel kesinlik (MCDM)** ile **doğal dil anlayışının (RAG & Local LLM)** hibrit bir birleşimi olarak ele alan uçtan uca bir Kurumsal Karar Destek Sistemidir (Decision Support System).
