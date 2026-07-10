import pandas as pd
import numpy as np

def clean_and_transform(df):
    try:
        # Local scope (Kopya üzerinde çalışıyoruz)
        df_clean = df.copy()
        
        # 1. Eksik Verileri Doldurma / Silme
        satis_ortalama = df_clean['Satis_Tutari'].mean()
        df_clean['Satis_Tutari'] = df_clean['Satis_Tutari'].fillna(satis_ortalama)
        
        # 2. String Metodları ve Normalizasyon (Slicing/Upper)
        df_clean['Sehir'] = df_clean['Sehir'].fillna('BİLİNMEYEN')
        df_clean['Sehir'] = df_clean['Sehir'].str.strip().str.upper()
        
        # 3. Yeni Sütun Üretme (KDV'li satış)
        df_clean['KDV_Dahil'] = df_clean['Satis_Tutari'] * 1.20
        
        # Negatif değerler varsa filtrele (Bool Karşılaştırma)
        df_clean = df_clean[df_clean['Satis_Tutari'] > 0]
        
        return df_clean
        
    except KeyError as e:
        print(f"Hata: İstenen sütun bulunamadı -> {e}")
        return None
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        return None