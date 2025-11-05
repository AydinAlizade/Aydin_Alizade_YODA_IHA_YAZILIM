# Kullanıcıdan bir cümle veya paragraf girmesini ister
metin = input("Bir cümle veya paragraf giriniz: ")

# Büyük/küçük harf duyarlılığını ortadan kaldırmak için tüm metni küçük harfe çeviriyoruz
# Böylece "Merhaba" ve "merhaba" aynı kelime olarak kabul edilir
metin = metin.lower()

# Metindeki kelimeleri boşluk karakterine göre ayırıyoruz (dizi şeklinde)
kelimeler = metin.split()

# Toplam kelime sayısını hesaplıyoruz
toplam_kelime = len(kelimeler)

# Toplam karakter sayısını (boşluklar dahil) hesaplıyoruz
toplam_karakter = len(metin)

# En uzun kelimenin uzunluğunu bulmak için max() fonksiyonunu kullanıyoruz
en_uzun_kelime_uzunlugu = len(max(kelimeler, key=len)) if kelimeler else 0

# Her kelimenin kaç kez geçtiğini tutmak için bir sözlük (dictionary) oluşturuyoruz
kelime_sayaci = {}

# Listedeki her kelimeyi sayıyoruz
for kelime in kelimeler:
    if kelime in kelime_sayaci:
        kelime_sayaci[kelime] += 1  # Eğer kelime zaten varsa sayısını bir artır
    else:
        kelime_sayaci[kelime] = 1   # Eğer yoksa sözlüğe ekle ve değeri 1 yap

# Sonuçları ekrana yazdırıyoruz
print("\n--- Metin İstatistikleri ---")
print(f"Toplam kelime sayısı: {toplam_kelime}")
print(f"Toplam karakter sayısı (boşluklar dahil): {toplam_karakter}")
print(f"En uzun kelimenin uzunluğu: {en_uzun_kelime_uzunlugu}")
print("\nKelime tekrar sayıları:")

# Her kelimenin kaç kez geçtiğini yazdırıyoruz
for kelime, sayi in kelime_sayaci.items():
    print(f"{kelime}: {sayi}")