# Sonsuz döngü başlatıyoruz. Kullanıcı çıkmak isteyene kadar program çalışmaya devam edecek.
while True:
    # Kullanıcıdan iki sayı alıyoruz. float() kullanmamız, ondalıklı sayı girebilmeyi sağlar.
    # try-except yapısı, kullanıcı yanlış giriş (örneğin harf) yaparsa programın çökmesini engeller.
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))  # Kullanıcıdan ilk sayıyı al
        sayi2 = float(input("İkinci sayıyı girin: "))   # Kullanıcıdan ikinci sayıyı al
    except ValueError:
        # Eğer kullanıcı sayısal olmayan bir değer girerse bu kısım çalışır.
        print("Hatalı giriş! Lütfen sayısal bir değer girin.")
        continue  # Döngünün başına dönerek yeniden giriş ister.

    # Kullanıcıdan yapmak istediği işlemi alıyoruz.
    # Kullanıcı sadece +, -, *, / karakterlerinden birini girmelidir.
    islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")

    # Girilen işleme göre farklı hesaplamalar yapacağız.
    # if - elif - else yapısı kullanarak işlemi kontrol ediyoruz.
    if islem == "+":  # Toplama işlemi
        sonuc = sayi1 + sayi2
        print("Sonuç:", sonuc)

    elif islem == "-":  # Çıkarma işlemi
        sonuc = sayi1 - sayi2
        print("Sonuç:", sonuc)

    elif islem == "*":  # Çarpma işlemi
        sonuc = sayi1 * sayi2
        print("Sonuç:", sonuc)

    elif islem == "/":  # Bölme işlemi
        # Burada özel bir durum var: sayi2 sıfır olursa hata verir.
        if sayi2 == 0:
            print("Hata: Bir sayıyı sıfıra bölemezsiniz!")
        else:
            sonuc = sayi1 / sayi2
            print("Sonuç:", sonuc)

    else:
        # Eğer kullanıcı geçersiz bir işlem karakteri girdiyse (örneğin % veya ^)
        print("Geçersiz işlem! Lütfen +, -, * veya / girin.")

    # İşlemden sonra kullanıcıya devam etmek isteyip istemediğini soruyoruz.
    devam = input("Başka bir işlem yapmak ister misiniz? (e/h): ")

    # Kullanıcı 'e' (evet) dışında bir şey yazarsa döngü sonlandırılır.
    if devam.lower() != "e":  # lower() fonksiyonu, harfi küçük hale getirir (E yazsa bile kabul edilir)
        print("Program sonlandırıldı.")
        break  # while döngüsünü bitirir.