# Enterprise Sales Intelligence System 

**Proje Özeti:** 
Bu proje, karmaşık ve düzensiz kurumsal satış verilerini işlemek, temizlemek ve yönetici düzeyinde karar destek metriklerine (Business Intelligence) dönüştürmek amacıyla tasarlanmış modüler bir veri analitiği sistemidir. Sistem, baştan uca bir veri hattı (data pipeline) mantığıyla kurgulanmıştır.

---

### 1. Neden NumPy ve Pandas Birlikte Kullanıldı?
Veri analitiği motorunun kalbinde hız ve yapısal esnekliği birleştirmek için **NumPy** ve **Pandas** kütüphaneleri hibrit bir yapıda kullanılmıştır.

* **Vektörel İşlem Gücü (NumPy):** Veri setleri büyüdükçe geleneksel döngülerin (for/while) yarattığı performans darboğazlarını aşmak için performans skorlamaları gibi matematiksel hesaplamalar, NumPy'ın matris tabanlı vektörel operasyonları ile yapılmıştır. Bu sayede hesaplama maliyeti minimize edilmiştir.
* **Yapısal Veri Manipülasyonu (Pandas):** DataFrame yapısı sayesinde farklı veri tiplerini (string, float, datetime) tek bir çatı altında yönetmek, eksik verileri filtrelemek ve Excel/CSV gibi formatlara veri aktarımı yapmak için Pandas tercih edilmiştir. 
* **Sonuç:** NumPy sistemin "motor gücünü" sağlarken, Pandas verinin "şasisini ve sunumunu" üstlenmiştir.

---

### 2. Eksik ve Bozuk Veri (Handling Missing Data) Kararları
Gerçek dünya verilerindeki düzensizlikleri simüle eden veri setinde, veri kaybını en aza indirmek için "silme" yerine "imputation (doldurma)" ve "kategorizasyon" stratejileri izlenmiştir:

* **Satış Tutarı (Sayısal Veri):** Eksik satış tutarları direkt silinmemiş, istatistiksel dağılımı bozmamak adına serinin **ortalama (mean)** değeri ile doldurulmuştur.
* **Şehir (Kategorik Veri):** Eksik lokasyon bilgileri veri setinden çıkarılmak yerine **"BİLİNMEYEN"** adında yeni bir kategoriye atanmıştır. Bu sayede, hatalı kayıtların ne kadar satış hacmine sahip olduğu bilgisinin kaybolması engellenmiştir.
* **Normalizasyon:** Metin tabanlı verilerdeki (boşluklar, büyük/küçük harf tutarsızlıkları) insan kaynaklı hatalar string metodları ile standartlaştırılmıştır.

---

### 3. GroupBy ile İş Kararı ve Karar Destek Mekanizması
Analitik sürecin amacı sadece veriyi özetlemek değil, yönetimsel aksiyon (actionable insight) yaratmaktır. Bu bağlamda Pandas'ın `groupby` ve `aggregation` metodları stratejik olarak kullanılmıştır:

* **Bölgesel Performans ve Risk Analizi:** Şehir bazlı gruplamalar yapılarak sadece toplam ciro değil, aynı zamanda ortalama sepet tutarları hesaplanmıştır. Sistem, genel ortalamanın %70'inin altında kalan bölgeleri dinamik olarak bir boolean maskesi (True/False) ile tespit edip **"Riskli Bölgeler"** olarak yöneticinin önüne sunmaktadır.
* **Kârlılık Endeksi:** Ürün ve ay bazlı kırılımlar hesaplanarak şirketin operasyonel kaynaklarını (reklam, stok, lojistik) nereye yönlendirmesi gerektiğine dair net sonuçlar (En kârlı ürün/ay) çıkarılmıştır.

---

### 4. Modüler Mimari (Modular Architecture) Avantajı
Proje, tüm süreçleri tek bir `.ipynb` dosyasına yığmak (monolithic) yerine, görev ayrılığı prensibine (Separation of Concerns) uygun olarak birden fazla `.py` modülüne bölünmüştür.

* **Geliştirilebilirlik ve Bakım:** Veri üretim (`data_generator.py`), temizleme (`preprocessing.py`), analiz (`analytics.py`) ve raporlama (`reporting.py`) katmanları birbirinden izole edilmiştir. Veritabanından veri çekme yöntemi değiştiğinde sadece tek bir modül güncellenir, analitik motor bu değişiklikten etkilenmez.
* **Hata Yönetimi (Try/Except):** Modüller, oluşabilecek sistem veya sütun hatalarına karşı kendi içlerinde `try/except` blokları ile güvence altına alınmış, sistemin tamamen çökmesi engellenmiştir.
* **Yeniden Kullanılabilirlik (Reusability):** Yazılan temizleme ve analiz fonksiyonları, gelecekteki farklı kurumsal projelerde kolayca içe aktarılıp (import) tekrar kullanılabilecek şekilde parametrik tasarlanmıştır.