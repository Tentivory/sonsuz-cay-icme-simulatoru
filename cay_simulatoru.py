#!/usr/bin/env python3
# Sonsuz Çay İçme Simülatörü - Gerçekten çalışır, ciddiye almayın.
# Gizli not: aGVya2VzIG9uZW1saWRpciA=  (bunu çözersen anlarsın)

import time
import random

def cay_ic():
    bardak_sayisi = 0
    sekerler = ["şekersiz", "az şekerli", "orta", "bol şekerli", "şeker dağı"]
    
    print("🍵 Sonsuz Çay İçme Simülatörü başlatıldı!")
    print("Çay demlendi, bardak hazır. Çıkış yok, sadece çay var.\n")
    
    try:
        while True:
            bardak_sayisi += 1
            seker = random.choice(sekerler)
            print(f"{bardak_sayisi}. bardak çay içildi. Şeker: {seker}")
            
            if bardak_sayisi % 10 == 0:
                print("⚠️  Uyarı: Çay içmekten bıkmadın mı? Hayır, bıkamazsın. Çay bitmez.")
            
            if bardak_sayisi == 42:
                print("🤔 Cevap 42 imiş, ama çay önce.")
            
            time.sleep(1)  # Gerçekçi tempo, yoksa CPU yanar
    except KeyboardInterrupt:
        print(f"\n🚪 Simülatör durduruldu. Toplam {bardak_sayisi} bardak içildi.")
        print("Çay içmeye devam etmek istersen tekrar çalıştır. Çay seni bekler.")

if __name__ == "__main__":
    cay_ic()
