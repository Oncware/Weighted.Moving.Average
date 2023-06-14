import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def hesapla():
    global df
    data = []
    eldeki_miktar = float(baslangic_miktar.get())
    eldeki_tutar = eldeki_miktar * float(baslangic_birim_fiyat.get())
    for hareket in hareketler:
        tarih, hareket_turu, miktar, birim_fiyat = hareket
        miktar = float(miktar)
        birim_fiyat = float(birim_fiyat)
        if hareket_turu == 'Giriş':
            alinan_tutar = miktar * birim_fiyat
            eldeki_miktar += miktar
            eldeki_tutar += alinan_tutar
        else:  # Çıkış
            alinan_tutar = miktar * birim_fiyat
            eldeki_miktar -= miktar
            eldeki_tutar -= alinan_tutar
        eldeki_birim_fiyat = eldeki_tutar / eldeki_miktar if eldeki_miktar > 0 else 0
        data.append([tarih, hareket_turu, miktar, birim_fiyat, alinan_tutar, eldeki_miktar, eldeki_birim_fiyat, eldeki_tutar])
    df = pd.DataFrame(data, columns=columns)
    df['Tarih'] = pd.to_datetime(df['Tarih'], format='%d.%m')
    df = df.sort_values(by='Tarih')
def sonuclari_goster():
    new_window = tk.Toplevel(root)
    new_window.title("Sonuç Tablosu")
    sorted_df = df.sort_values(by='Tarih')  # Sort DataFrame by "Tarih" column
    tree = ttk.Treeview(new_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill='both', expand=True)
    for index, row in sorted_df.iterrows():  # Use the sorted DataFrame
        tree.insert("", "end", values=list(row))
    # Kaydet butonu
    kaydet_btn = ttk.Button(new_window, text="Sonuçları Kaydet", command=kaydet)
    kaydet_btn.pack()


def kaydet():
    dosya_ismi = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dosyası", "*.csv")])
    df.to_csv(dosya_ismi, index=False)
    messagebox.showinfo("Başarılı", f"Veriler başarıyla {dosya_ismi} olarak kaydedildi.")

def giris_ekle():
    tarih = giris_tarih.get()
    miktar = giris_miktar.get()
    birim_fiyat = giris_birim_fiyat.get()
    hareketler.append((tarih, 'Giriş', miktar, birim_fiyat))

def cikis_ekle():
    tarih = cikis_tarih.get()
    miktar = cikis_miktar.get()
    birim_fiyat = cikis_birim_fiyat.get()
    hareketler.append((tarih, 'Çıkış', miktar, birim_fiyat))

columns = ["Tarih", "Hareket Türü", "Alınan Miktar(kg)", "Alınan Birim Fiyat", "Alınan Tutar(TL)", "Eldeki Miktar(kg)", "Eldeki Birim Fiyat", "Eldeki Tutar(TL)"]

hareketler = []

root = tk.Tk()
root.title("Stok Hareketleri")

baslangic_miktar = tk.StringVar()
baslangic_birim_fiyat = tk.StringVar()

giris_tarih = tk.StringVar()
giris_miktar = tk.StringVar()
giris_birim_fiyat = tk.StringVar()

cikis_tarih = tk.StringVar()
cikis_miktar = tk.StringVar()
cikis_birim_fiyat = tk.StringVar()

# Başlangıç girdileri
tk.Label(root, text="Başlangıç Miktarı (kg):").grid(row=0, column=0)
tk.Entry(root, textvariable=baslangic_miktar).grid(row=0, column=1)

tk.Label(root, text="Başlangıç Birim Fiyatı:").grid(row=1, column=0)
tk.Entry(root, textvariable=baslangic_birim_fiyat).grid(row=1, column=1)

# Giriş girdileri
tk.Label(root, text="Giriş Tarihi (GG.AA):").grid(row=2, column=0)
tk.Entry(root, textvariable=giris_tarih).grid(row=2, column=1)

tk.Label(root, text="Giriş Miktarı (kg):").grid(row=3, column=0)
tk.Entry(root, textvariable=giris_miktar).grid(row=3, column=1)

tk.Label(root, text="Giriş Birim Fiyatı:").grid(row=4, column=0)
tk.Entry(root, textvariable=giris_birim_fiyat).grid(row=4, column=1)

tk.Button(root, text="Giriş Ekle", command=giris_ekle).grid(row=5, column=1)

# Çıkış girdileri
tk.Label(root, text="Çıkış Tarihi (GG.AA):").grid(row=6, column=0)
tk.Entry(root, textvariable=cikis_tarih).grid(row=6, column=1)

tk.Label(root, text="Çıkış Miktarı (kg):").grid(row=7, column=0)
tk.Entry(root, textvariable=cikis_miktar).grid(row=7, column=1)

tk.Label(root, text="Çıkış Birim Fiyatı:").grid(row=8, column=0)
tk.Entry(root, textvariable=cikis_birim_fiyat).grid(row=8, column=1)

tk.Button(root, text="Çıkış Ekle", command=cikis_ekle).grid(row=9, column=1)

# Hesapla butonu
tk.Button(root, text="Hesapla", command=hesapla).grid(row=10, column=0)

# Sonuçları göster butonu
tk.Button(root, text="Sonuçları Görüntüle", command=sonuclari_goster).grid(row=10, column=1)

root.mainloop()
