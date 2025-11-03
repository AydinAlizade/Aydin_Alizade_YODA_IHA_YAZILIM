import random  # Rastgele sayı üretmek için random modülünü içe aktar
print("Sayı Tahmin Oyununa Hoşgeldiniz! 1 ile 100 arasında bir sayı seçildi.")  # Oyuna hoşgeldiniz mesajı göster
target = random.randint(1, 100)  # 1 ile 100 arasında rastgele hedef sayıyı seç
max_attempts = 10  # Kullanıcıya verilecek maksimum tahmin hakkı
attempts = 0  # Yapılmış geçerli tahmin sayısını tutmak için sayaç
guessed = False  # Doğru tahmin edilip edilmediğini izlemek için bayrak

while attempts < max_attempts and not guessed:  # Tahmin hakkı bitene kadar veya doğru bulunana kadar döngü
    user_input = input(f"{attempts+1}. tahmininizi girin (1-100): ")  # Kullanıcıdan tahmin al
    try:
        guess = int(user_input)  # Girilen değeri tamsayıya dönüştür
    except ValueError:
        print("Lütfen 1 ile 100 arasında bir tamsayı girin.")  # Geçersiz girişte uyarı ver
        continue  # Geçersiz giriş tahmin hakkını tüketmez, döngüye devam et

    if guess < 1 or guess > 100:  # Tahminin geçerli aralıkta olup olmadığını kontrol et
        print("Giriş aralığın dışında. 1 ile 100 arasında bir sayı girin.")  # Aralık dışı giriş uyarısı
        continue  # Aralık dışı giriş tahmin hakkını tüketmez, döngüye devam et

    attempts += 1  # Geçerli bir tahmin yapıldığında tahmin sayısını artır

    if guess < target:  # Tahmin hedef sayıdan küçükse
        print("Tahmininiz çok düşük.")  # Kullanıcıya düşük olduğunu bildir
    elif guess > target:  # Tahmin hedef sayıdan büyükse
        print("Tahmininiz çok yüksek.")  # Kullanıcıya yüksek olduğunu bildir
    else:  # Tahmin hedef sayıya eşitse
        print(f"Tebrikler! Doğru tahmin ettiniz. Sayı {target} idi.")  # Doğru tahmin mesajı göster
        guessed = True  # Doğru tahmin bayrağını güncelle
        break  # Döngüyü sonlandır

if guessed:  # Eğer kullanıcı doğru tahmin ettiyse
    print(f"{attempts} denemede doğru tahmin ettiniz.")  # Kaç denemede bildiğini bildir
else:  # Aksi halde tahmin hakları bitti demektir
    print(f"Tahmin hakkınız bitti. Doğru sayı {target} idi.")  # Doğru sayıyı ve hakkın bittiğini bildir    