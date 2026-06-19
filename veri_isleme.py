import pandas as pd
import numpy as np

print("🔄 Veriler yükleniyor...")

# Tabloları oku
orders = pd.read_csv('olist_orders_dataset.csv')
items = pd.read_csv('olist_order_items_dataset.csv')
reviews = pd.read_csv('olist_order_reviews_dataset.csv')
sellers = pd.read_csv('olist_sellers_dataset.csv')

print("✅ Tablolar başarıyla hafızaya alındı!")

# Tabloları birleştirme (Merge)
print("🔗 Tablolar birleştiriliyor...")
master_df = pd.merge(orders, items, on='order_id', how='inner')
master_df = pd.merge(master_df, reviews, on='order_id', how='left')
master_df = pd.merge(master_df, sellers, on='seller_id', how='left')
print(f"🎯 Birleştirme tamamlandı! Satır sayısı: {master_df.shape[0]}")

# Tarih dönüşümleri ve temizlik
tarih_sutunlari = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for sutun in tarih_sutunlari:
    master_df[sutun] = pd.to_datetime(master_df[sutun])

master_df = master_df.dropna(subset=['order_delivered_customer_date'])
print("📆 Tarih formatları düzeltildi ve temizlendi!")

# Kontrol için ilk 3 satırın özetini terminale basalım
print("\n--- İlk Üç Satırın Özeti ---")
print(master_df[['order_id', 'freight_value']].head(3))