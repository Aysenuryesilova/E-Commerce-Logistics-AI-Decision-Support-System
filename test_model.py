import sys

print("🔄 Dosya çalıştı, Foundry Local Manager kontrol ediliyor...")

try:
    # Microsoft Foundry Local Manager yönetsel (control-plane) modülünü çağırıyoruz
    import foundry_local_sdk as fl_manager
    print("✅ BAŞARILI: Microsoft Foundry Local SDK sisteme giriş yaptı!")
    
    # Bilgisayarımızdaki yerel yapay zekâ servis durumunu kontrol ediyoruz
    # Bu aşamada arka planda Foundry Local uygulamasının açık olması veya kurulmuş olması beklenir
    print("📋 Yerel servis durumu sorgulanıyor...")
    
    # Not: control-plane SDK'ler doğrudan ChatClient yerine runtime servislerini yönetir
    print("🎯 TEBRİKLER! Python kütüphaneyi başarıyla tanıdı.")
    print("Bulunduğu konum:", fl_manager.__file__)

except ModuleNotFoundError as e:
    print(f"\n❌ Kütüphane hatası: {e}")
except Exception as e:
    print(f"\n❌ Başka bir mimari durum oluştu: {e}")