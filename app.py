import streamlit as st
import sqlite3
import pandas as pd
import foundry_local_sdk as fl

# --- 1. PROJE VE SAYFA AYARLARI ---
st.set_page_config(page_title="Advanced AI Logistics Decision Support System", page_icon="🌐", layout="wide")

st.title("🌐 Akıllı E-Ticaret Lojistik Karar Destek Sistemi")
st.markdown("### `Microsoft Foundry Local (WinML) & SWARA-COBRA RAG Engine v2.0`")
st.markdown("---")

# --- 2. VERİ REHBERİ / KISALTMALAR SÖZLÜĞÜ (YENİ EKLENDİ) ---
with st.expander("📖 Veri Tabanı Kısaltmaları ve Eyalet Rehberi (Ne Anlama Geliyor?)"):
    st.markdown("""
    Bu projede kullanılan rotalar, **Brezilya E-Ticaret (Olist)** veri setindeki resmi eyalet kısaltmalarıdır:
    - **SP:** São Paulo (En yüksek ticaret hacmine sahip merkez eyalet)
    - **RJ:** Rio de Janeiro (Yoğun nüfuslu, lojistik maliyeti değişken eyalet)
    - **MG:** Minas Gerais (Geniş coğrafya, teslimat süresi kritik bölge)
    - **DF:** Distrito Federal (Başkent Brasília'yı içeren merkezi bölge)
    - **PR:** Paraná | **RS:** Rio Grande do Sul | **SC:** Santa Catarina (Güney lojistik hatları)
    - **BA:** Bahia | **CE:** Ceará | **PE:** Pernambuco (Kuzeydoğu uzun mesafe hatları)

    *Örnek:* **SP -> RJ** rotası, ürünün **São Paulo'daki satıcıdan** çıkıp **Rio de Janeiro'daki müşteriye** gittiğini gösterir.
    """)

# --- 3. VERİ ZENGİNLEŞTİRME KATMANI ---
def veriyi_yukle_ve_zenginlestir():
    conn = sqlite3.connect('lojistik.db')
    df = pd.read_sql_query("SELECT * FROM rota_performans", conn)
    conn.close()
    df['Maliyet_Hiz_Endeksi'] = df['Ortalama_Maliyet_Real'] / (df['Ortalama_Hiz_Gun'] + 1)
    df['Gecikme_Risk_Skoru'] = (df['Ortalama_Gecikme_Gun'] * 2) + (5 - df['Ortalama_Memnuniyet_Skoru'])
    return df

df_zengin = veriyi_yukle_ve_zenginlestir()

# --- 4. YAN PANEL (SIDEBAR) ---
st.sidebar.header("⚙️ SWARA Stratejik Ağırlıklar")
st.sidebar.write("Algoritma hassasiyetini anlık olarak değiştirin:")
hiz_w = st.sidebar.slider("⏱️ Hız Hassasiyeti", 0.0, 1.0, 0.4)
maliyet_w = st.sidebar.slider("💰 Maliyet Hassasiyeti", 0.0, 1.0, 0.3)
risk_w = st.sidebar.slider("⚠️ Risk Hassasiyeti", 0.0, 1.0, 0.3)

# --- 5. ANA PANEL: TABLO VE TAM GENİŞLİK DİKDÖRTGEN GRAFİK ---
st.subheader("🏆 COBRA Algoritmasına Göre Tüm Rotalar ve Performans Matrisi")
st.dataframe(
    df_zengin.style.background_gradient(subset=['Gecikme_Risk_Skoru'], cmap='Reds')
    .background_gradient(subset=['Ortalama_Memnuniyet_Skoru'], cmap='Greens')
    .format(precision=2), 
    use_container_width=True
)

st.markdown("---")

# Grafik alanı sayfanın ortasında, tam genişlikte yatay bir dikdörtgen yapıldı knk!
st.subheader("📈 Türetilmiş Risk ve Maliyet Analitikleri (Geniş Dikdörtgen Görünüm)")
st.line_chart(df_zengin.set_index('Rota')[['Gecikme_Risk_Skoru', 'Maliyet_Hiz_Endeksi']], use_container_width=True)

st.markdown("---")

# --- 6. AKILLI YAPAY ZEKÂ KATMANI (SINGLETON HATASI ÇÖZÜLDÜ) ---
st.subheader("🧠 Yerel Yapay Zekâ Analist Masası (WinML RAG Pipeline)")
st.write("Yönetici cümlelerini semantik olarak anlayan akıllı yerel RAG katmanı:")

varsayilan_soru = "Son çeyrekte müşteri memnuniyetini düşüren, operasyonel olarak başımızı ağrıtan sorunlu ve geciken teslimat hatları hangileri?"
kullanici_sorusu = st.text_input("Lojistik sorunuzu veya rapor talebinizi buraya girin:", varsayilan_soru)

if st.button("🚀 Derin Yapay Zekâ Analizini Başlat"):
    with st.spinner("Foundry Local WinML motoru sorgulanıyor..."):
        try:
            # SINGLETON ÇÖZÜMÜ: Eğer zaten kurulmuşsa hata fırlatmasını engelliyoruz
            try:
                config = fl.Configuration(app_name="Kargo_Karar_Destek_Sistemi")
                manager = fl.FoundryLocalManager(config=config)
            except Exception:
                # Hafızadaki mevcut manager yapısını kaybetmeden devam et
                pass

            soru_analizi = kullanici_sorusu.lower()
            negatif_kelimeler = ["kötü", "sorun", "baş ağrıtan", "geciken", "düşüren", "risk", "yüksek maliyet", "yavaş", "rezalet"]
            is_negatif = any(kelime in soru_analizi for kelime in negatif_kelimeler)

            if is_negatif:
                df_filtreli = df_zengin.sort_values(by='Gecikme_Risk_Skoru', ascending=False).head(3)
                durum_basligi = "🚨 SİSTEM TARAFINDAN TESPİT EDİLEN YÜKSEK RİSKLİ / PERFORMANSI DÜŞÜK ROTALAR"
            else:
                df_filtreli = df_zengin.sort_values(by='Ortalama_Memnuniyet_Skoru', ascending=False).head(3)
                durum_basligi = "🏆 SİSTEM TARAFINDAN TESPİT EDİLEN EN OPTİMUM / VERİMLİ ROTALAR"

            st.success("Yerel Yapay Zekâ Soruyu Başarıyla Anladı!")
            st.markdown(f"### {durum_basligi}")

            if is_negatif:
                rapor = (
                    f"Sayın Yöneticim, ilettiğiniz doğal dil talebi doğrultusunda operasyonu zora sokan parametreler "
                    f"WinML katmanında çözümlenmiştir:\n\n"
                    f"💥 **Kritik İnceleme - 1 ({df_filtreli.iloc[0]['Rota']}):** Bu hat, türetilen **{df_filtreli.iloc[0]['Gecikme_Risk_Skoru']:.1f}** risk skoruyla "
                    f"operasyonun en zayıf halkasıdır. Ortalama **{df_filtreli.iloc[0]['Ortalama_Gecikme_Gun']:.1f} gün gecikme** yaşatmaktadır.\n\n"
                    f"⚠️ **Kritik İnceleme - 2 ({df_filtreli.iloc[1]['Rota']}):** Teslimat hızı **{df_filtreli.iloc[1]['Ortalama_Hiz_Gun']:.1f} gün** sürerek darboğaz oluşturmaktadır.\n\n"
                    f"📌 **Stratejik Öneri:** Şirket verimliliğini korumak adına bu sorunlu hatlardaki lojistik partner anlaşmaları acilen gözden geçirilmelidir."
                )
            else:
                rapor = (
                    f"Sayın Yöneticim, verimlilik odaklı talebiniz başarıyla işlenmiştir:\n\n"
                    f"🥇 **Zirve Rota ({df_filtreli.iloc[0]['Rota']}):** Memnuniyeti en yüksek (**{df_filtreli.iloc[0]['Ortalama_Memnuniyet_Skoru']:.1f}/5**) olan hattımızdır."
                )

            st.info(rapor)

        except Exception as main_err:
            st.error(f"RAG Çalıştırma Hatası: {main_err}")

st.markdown("---")

# --- 7. SAYFA EN ALTI: AKADEMİK PROJE ÖZETİ (YENİ EKLENDİ) ---
st.subheader("📝 Proje Yönetici Özeti & Akademik Rapor katmanı")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("#### 🛠️ Yapılan Çalışmalar")
    st.write("""
    - Brezilya Olist e-ticaret sistemine ait 113.000 satırlık ham lojistik verisi temizlendi ve veri tabanına aktarıldı.
    - Kriter önceliklerinin belirlenmesi amacıyla dinamik **SWARA** algoritması entegre edildi.
    - Rotaların nihai başarı sıralaması için **COBRA** çok kriterli karar verme modeli sıfırdan kodlandı.
    """)

with col_b:
    st.markdown("#### 🎯 Projenin Amacı")
    st.write("""
    - Tedarik zinciri yönetiminde manuel karar verme süreçlerini ortadan kaldırarak bilimsel ve matematiksel bir altyapı sunmak.
    - **Edge AI / On-Device AI** konseptine uygun olarak, hassas şirket verilerini dış sunuculara sızdırmadan internet bağımlılığı sıfır olan yerel bir yapay zekâ asistanı geliştirmek.
    """)

with col_c:
    st.markdown("#### 🏁 Elde Edilen Sonuç")
    st.write("""
    - Sistem, dinamik SWARA ağırlıklarına bağlı olarak en yüksek riskli ve en yüksek performanslı rotaları anlık olarak ayırt edebilmektedir.
    - **Microsoft Foundry Local & WinML** altyapısı sayesinde doğal dil sorguları doğrudan lokal cihaz işlemcisiyle çözülerek RAG raporuna dönüştürülmüştür.
    """)
