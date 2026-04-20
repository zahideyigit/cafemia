import qrcode
# Oluşturmak istediğimiz site.
my_website = "https://www.youtube.com/@RRaenee"
# QR kodunu kaydetmek istediğimiz dosya adı.
output_FN = "cafe_menu.png"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1, # QR kodunun boyutunu belirler (1-40 arasında). 1 en küçük boyuttur.
    error_correction=qrcode.constants.ERROR_CORRECT_H, # H, M, L seçenekleri var. H en yüksek hata düzeltme kapasitesine sahip.
    box_size=10, # QR kodundaki her bir kutunun piksel boyutunu belirler.
    border=4, # QR kodunun etrafındaki beyaz boşluğun kutu sayısı cinsinden genişliğini belirler. Genellikle 4 önerilir.
    )
# QR koduna veri ekleme
qr.add_data(my_website)
# QR kodunu oluşturma
qr.make(fit=True)

# QR kodunu terminalde görselleştirme (isteğe bağlı) boş uğrama laksjdflaksfd
# zorluk = qr.get_matrix()
# for row in zorluk:    print("".join(["██" if cell else "  " for cell in row]))


# QR kodunu görselleştirme ve kaydetme
img = qr.make_image(fill_color="black", back_color="white")
# QR kodunu kaydetme
img.save(output_FN)

# Başarılı mesajı
print(f"Başarılı! QR kod '{output_FN}' adıyla kaydedildi.")