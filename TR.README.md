# ÖNEMLİ !! : Giriş ve çıkışları kronolojik sıraya göre ekleyin

Bu kod, bir stok takip uygulamasını basit bir grafik arayüzü (GUI) kullanarak gerçekleştiriyor. Kullanıcı, başlangıç miktarını ve birim fiyatını girdikten sonra giriş ve çıkış hareketlerini ekleyebilir. Ardından "Hesapla" düğmesine basarak stok hareketlerine dayalı hesaplamaları yapabilir ve "Sonuçları Görüntüle" düğmesine basarak sonuçları görebilir. Ayrıca sonuçları bir CSV dosyasına kaydedebilir.

Kullanım adımları:

Başlangıç miktarını ve birim fiyatını girmek için "Başlangıç Miktarı (kg)" ve "Başlangıç Birim Fiyatı" alanlarına değerleri girin.
Giriş hareketi eklemek için "Giriş Tarihi (GG.AA)", "Giriş Miktarı (kg)" ve "Giriş Birim Fiyatı" alanlarına değerleri girin. Ardından "Giriş Ekle" düğmesine basın.
Çıkış hareketi eklemek için "Çıkış Tarihi (GG.AA)", "Çıkış Miktarı (kg)" ve "Çıkış Birim Fiyatı" alanlarına değerleri girin. Ardından "Çıkış Ekle" düğmesine basın.
Tüm giriş ve çıkış hareketlerini ekledikten sonra "Hesapla" düğmesine basın. Bu, stok hareketlerine dayalı hesaplamaları yapacak ve sonuçları bir veri çerçevesinde depolayacaktır.
"Sonuçları Görüntüle" düğmesine basarak sonuçları yeni bir pencerede görebilirsiniz. Sonuçlar, bir ağaç görünümünde görüntülenecektir.
Sonuçları kaydetmek için "Sonuçları Kaydet" düğmesini kullanabilirsiniz. Bu, sonuçları bir CSV dosyasına kaydedecektir. Kaydetme işleminden sonra başarılı bir mesaj görüntülenecektir.
Not: Bu kod parçası, Pandas ve Tkinter kütüphanelerini kullanır. Bu kütüphanelerin yüklü olduğundan emin olun. Ayrıca, giriş ve çıkış tarihlerini "GG.AA" formatında girilmesi gerektiğini unutmayın.
