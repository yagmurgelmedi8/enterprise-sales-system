import numpy as np
import pandas as pd

def generate_sales_data(n_rows=1000, *args): # *args kullanımı
    np.random.seed(42) # Sonuçların tekrarlanabilir olması için
    
    # NumPy ile rastgele veri üretimi
    customer_ids = np.random.randint(1000, 5000, n_rows)
    products = np.random.choice(['Laptop', 'Telefon', 'Tablet', 'Monitör', 'Klavye'], n_rows)
    cities = np.random.choice(['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Erzurum', 'Diyarbakır'], n_rows)
    sales = np.random.normal(loc=15000, scale=5000, size=n_rows)
    months = np.random.choice(['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'], n_rows)
    
    df = pd.DataFrame({
        'Musteri_ID': customer_ids,
        'Urun': products,
        'Sehir': cities,
        'Satis_Tutari': sales,
        'Ay': months
    })
    
    # Bilerek NaN (eksik veri) ekleme
    nan_indices = np.random.choice(df.index, size=int(n_rows * 0.05), replace=False)
    df.loc[nan_indices, 'Satis_Tutari'] = np.nan
    
    nan_cities = np.random.choice(df.index, size=int(n_rows * 0.03), replace=False)
    df.loc[nan_cities, 'Sehir'] = np.nan
    
    # Uç değerler (Outliers) ekleme
    outlier_indices = np.random.choice(df.index, size=5, replace=False)
    df.loc[outlier_indices, 'Satis_Tutari'] = df.loc[outlier_indices, 'Satis_Tutari'] * 15
    
    return df