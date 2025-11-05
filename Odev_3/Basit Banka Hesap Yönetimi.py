# Önce bir 'Hesap' sınıfı oluşturuyoruz.
# Bu sınıf, bir banka hesabının temel özelliklerini ve işlevlerini tutar.
class Hesap:
    # Yapıcı (constructor) metot: Nesne oluşturulurken otomatik olarak çalışır.
    def __init__(self, sahip_adi, hesap_no, bakiye=0):
        self.sahip_adi = sahip_adi   # Hesap sahibinin adı
        self.hesap_no = hesap_no     # Hesap numarası
        self.bakiye = bakiye         # Başlangıç bakiyesi (varsayılan 0)

    # Para yatırma işlemi
    def para_yatir(self, miktar):
        if miktar > 0:  # Negatif bir miktar yatırmaya çalışılmasın diye kontrol
            self.bakiye += miktar
            print(f"{miktar} TL başarıyla yatırıldı.")
        else:
            print("Geçersiz miktar! Lütfen pozitif bir değer girin.")

    # Para çekme işlemi
    def para_cek(self, miktar):
        if miktar <= 0:
            print("Geçersiz miktar! Lütfen pozitif bir değer girin.")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye! Bu kadar para çekemezsiniz.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi.")

    # Bakiye görüntüleme
    def bakiye_goruntule(self):
        print(f"Mevcut bakiyeniz: {self.bakiye} TL")


# Kullanıcıdan hesap bilgilerini alıyoruz.
ad = input("Hesap sahibinin adını girin: ")
hesap_numarasi = input("Hesap numarasını girin: ")
bakiye_baslangic = float(input("Başlangıç bakiyesini girin (varsayılan 0): ") or 0)

# Hesap nesnesi oluşturuluyor.
hesabim = Hesap(ad, hesap_numarasi, bakiye_baslangic)

print("\nBanka Hesabınız oluşturuldu!\n")

# Program sürekli çalışacak, kullanıcı çıkmak isteyene kadar
while True:
    print("\n--- İşlemler ---")
    print("1. Para Yatır")
    print("2. Para Çek")
    print("3. Bakiye Görüntüle")
    print("4. Çıkış")

    secim = input("Bir işlem seçin (1-4): ")

    # Kullanıcının seçimine göre işlem yapılır.
    if secim == "1":
        miktar = float(input("Yatırmak istediğiniz miktar: "))
        hesabim.para_yatir(miktar)

    elif secim == "2":
        miktar = float(input("Çekmek istediğiniz miktar: "))
        hesabim.para_cek(miktar)

    elif secim == "3":
        hesabim.bakiye_goruntule()

    elif secim == "4":
        print("Çıkış yapılıyor... Görüşmek üzere!")
        break  # Döngüyü sonlandırır.

    else:
        print("Geçersiz seçim! Lütfen 1-4 arasında bir değer girin.")