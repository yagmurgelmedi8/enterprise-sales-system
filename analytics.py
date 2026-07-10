import numpy as np
import pandas as pd

def run_analytics(df_clean):
    # --- NumPy Vektörel Operasyonlar & Matrix Indexing ---
    # Satış tutarlarını NumPy dizisine (array) çevirip min-max normalizasyonu yapıyoruz
    satis_matrisi = df_clean['Satis_Tutari'].values
    min_satis, max_satis = np.min(satis_matrisi), np.max(satis_matrisi)
    
    # Hiç döngü kullanmadan tüm diziyi normalize etme (axis ve vektörel işlem)
    df_clean['Performans_Skoru'] = ((satis_matrisi - min_satis) / (max_satis - min_satis)) * 100
    
    # --- Pandas GroupBy & Aggregation ---
    sehir_analizi = df_clean.groupby('Sehir').agg(
        Toplam_Satis=('Satis_Tutari', 'sum'),
        Ortalama_Satis=('Satis_Tutari', 'mean'),
        İslem_Adedi=('Musteri_ID', 'count')
    )
    
    urun_analizi = df_clean.groupby('Urun')['Satis_Tutari'].sum().sort_values(ascending=False)
    ay_analizi = df_clean.groupby('Ay')['Satis_Tutari'].sum()
    
    # Sonuçları dictionary olarak döndürüyoruz
    return {
        'sehir': sehir_analizi,
        'urun': urun_analizi,
        'ay': ay_analizi,
        'raw_clean_df': df_clean
    }