import tkinter as tk
from tkinter import messagebox

def forward_chaining(gejala):
    rules = {
        1: {'G1', 'G2', 'G3', 'G4'},
        2: {'K1', 'G5'},
        3: {'K1', 'G6'},
        4: {'K1', 'P1', 'G7', 'G8'},
        5: {'K2', 'G9'},
        6: {'P5', 'G10', 'G11', 'G12', 'G13'},
        7: {'P5', 'G10', 'G14', 'G15', 'G16'},
        8: {'P5', 'G17'},
        9: {'P8', 'P6', 'P7'},
        10: {'P5', 'G18'},
        11: {'K3', 'G19'},
        12: {'P1', 'P11', 'G20'},
        13: {'P13', 'G21', 'G22', 'G25'},
        14: {'P13', 'P1', 'G23', 'G24'},
        15: {'P13', 'G25', 'G26'},
        16: {'P11', 'G27', 'G28', 'G29', 'G30'},
        17: {'P11', 'G27', 'G28', 'G31', 'G32', 'G33', 'G34'},
        18: {'P11', 'G35', 'G36'}
    }

    penyakit = {
        'P1': 'Tanda Bahaya Umum',
        'P2': 'Batuk',
        'P3': 'Pneumonia',
        'P4': 'Pneumonia Berat',
        'P5': 'Diare',
        'P6': 'Diare Dehidrasi Ringan',
        'P7': 'Diare Dehidrasi Berat',
        'P8': 'Diare Persisten',
        'P9': 'Diare Persisten Berat',
        'P10': 'Disentri',
        'P11': 'Demam',
        'P12': 'Demam dengan Tanda Bahaya Umum',
        'P13': 'Campak',
        'P14': 'Campak dengan komplikasi berat',
        'P15': 'Campak dengan komplikasi',
        'P16': 'Demam Mungkin DBD',
        'P17': 'DBD',
        'P18': 'Demam bukan DBD'
    }

    hasil = set()

    for rule, gejalas in rules.items():
        if all(gejala in gejalas for gejala in gejala):
            hasil.add(penyakit['P'+str(rule)])

    return list(hasil)

def submit_gejala():
    selected_gejala = [gejala_var.get() for gejala_var in gejala_vars if gejala_var.get() != ""]
    if len(selected_gejala) == 0:
        messagebox.showerror("Error", "Pilih setidaknya satu gejala!")
    else:
        hasil_diagnosa = forward_chaining(selected_gejala)
        if hasil_diagnosa:
            messagebox.showinfo("Hasil Diagnosa", "Hasil Diagnosa: {}".format(", ".join(hasil_diagnosa)))
        else:
            messagebox.showinfo("Hasil Diagnosa", "Tidak ada penyakit yang cocok dengan gejala yang dipilih.")

# Data gejala
gejala_list = [
    "G1 Anak tidak bisa minum atau menyusu",
    "G2 Anak memuntahkan makanan yang dimakan",
    "G3 Anak menderita kejang",
    "G4 Anak tampak letargis atau tidak sadar",
    "G5 Napas Normal",
    "G6 Napas cepat",
    "G7 Tarikan dinding dada ke dalam",
    "G8 Stridor",
    "G9 Berak cair atau lembek",
    "G10 Mata cekung",
    "G11 Cubitan kulit perut kembali lambat",
    "G12 Gelisah, rewel/mudah marah",
    "G13 Haus, minum dengan lahap",
    "G14 Cubitan kulit perut sangat lambat",
    "G15 Anak tampak letargis atau tidak sadar",
    "G16 Tidak bisa minum atau malas minum",
    "G17 Diare 14 hari atau lebih",
    "G18 Ada darah dalam tinja",
    "G19 Suhu badan melebihi 37.5º C",
    "G20 Kaku kuduk (anak tidak bisa menunduk hingga dagu mencapai dada)",
    "G21 Ruam kemerahan di kulit",
    "G22 batuk pilek atau mata merah",
    "G23 Luka di mulut yang dalam atau luas",
    "G24 Kekeruhan pada kornea mata",
    "G25 Luka di mulut",
    "G26 Mata bernanah",
    "G27 Demam 2 - 7 hari",
    "G28 Demam mendadak tinggi dan terus menerus",
    "G29 Nyeri di ulu hati",
    "G30 bintik bintik merah",
    "G31 Muntah bercampur darah / seperti kopi",
    "G32 Tinja berwarna hitam",
    "G33 Perdarahan dihidung dan gusi",
    "G34 Syok dan gelisah",
    "G35 Infeksi",
    "G36 Pilek",
    "K1 Batuk",
    "K2 Diare",
    "K3 Demam"
]

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Sistem Pakar")

gejala_vars = []
for gejala in gejala_list:
    gejala_var = tk.StringVar()
    gejala_checkbox = tk.Checkbutton(root, text=gejala, variable=gejala_var, onvalue=gejala.split()[0], offvalue="")
    gejala_checkbox.pack(anchor=tk.W)
    gejala_vars.append(gejala_var)

submit_button = tk.Button(root, text="Submit", command=submit_gejala)
submit_button.pack()

root.mainloop()