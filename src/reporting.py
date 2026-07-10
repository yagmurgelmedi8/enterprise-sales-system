import pandas as pd

def generate_executive_report(analytics_data):
    sehir_df = analytics_data['sehir']
    urun_serisi = analytics_data['urun']
    ay_serisi = analytics_data['ay']
    
    # Tuple kullanımı ile idxmax/idxmin
    en_iyi_sehir = sehir_df['Toplam_Satis'].idxmax()
    en_karli_urun = urun_serisi.idxmax()
    en_iyi_ay = ay_serisi.idxmax()
    genel_toplam = sehir_df['Toplam_Satis'].sum()
    
    # Bool ve if ile riskli bölge tespiti (Ortalamanın %70'i altındaysa)
    genel_ortalama = sehir_df['Ortalama_Satis'].mean()
    is_risky = sehir_df['Ortalama_Satis'] < (genel_ortalama * 0.70)
    
    riskli_bolgeler = sehir_df[is_risky].index.tolist()
    if not riskli_bolgeler:
        riskli_bolgeler = ["Riskli Bölge Tespit Edilmedi"]
        
    # Dict formatında çıktı
    rapor_dict = {
        "Toplam Satış": f"{genel_toplam:,.2f} TL",
        "En Kârlı Şehir": en_iyi_sehir,
        "En İyi Ay": en_iyi_ay,
        "En Kârlı Ürün": en_karli_urun,
        "Riskli Bölgeler": ", ".join(riskli_bolgeler)
    }
    
    print("\n" + "="*40)
    print("📈 YÖNETİM KARAR DESTEK RAPORU")
    print("="*40)
    for key, val in rapor_dict.items():
        print(f"🔹 {key.ljust(20)}: {val}")
    print("="*40)
    
    return rapor_dict