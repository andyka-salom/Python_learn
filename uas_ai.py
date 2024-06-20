import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data_nasabah.csv')

# Encoding fitur kategori
le_status = LabelEncoder()
le_riwayat = LabelEncoder()
le_kelayakan = LabelEncoder()

data['Status_Pekerjaan'] = le_status.fit_transform(data['Status_Pekerjaan'])
data['Riwayat_Pembayaran'] = le_riwayat.fit_transform(data['Riwayat_Pembayaran'])
data['Kelayakan_Kredit'] = le_kelayakan.fit_transform(data['Kelayakan_Kredit'])

# Memisahkan fitur dan label
X = data.drop(['ID', 'Nama', 'Kelayakan_Kredit'], axis=1)
y = data['Kelayakan_Kredit']

# Membagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Melatih model Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Melakukan prediksi
y_pred = model.predict(X_test)

# Evaluasi model
print(f"Akurasi: {accuracy_score(y_test, y_pred)}")
print("Laporan Klasifikasi:")
print(classification_report(y_test, y_pred))

# Melakukan prediksi untuk seluruh data nasabah
data['Prediksi_Kelayakan'] = model.predict(X)

# Mengembalikan label hasil prediksi ke bentuk asli
data['Prediksi_Kelayakan'] = le_kelayakan.inverse_transform(data['Prediksi_Kelayakan'])

# Menampilkan hasil analisa dan nasabah yang layak diberikan kredit
print("\nHasil Analisa Pemberian Kredit:")
print(data[['ID', 'Nama', 'Umur', 'Pendapatan', 'Status_Pekerjaan', 'Jumlah_Pinjaman', 'Lama_Pinjaman', 'Riwayat_Pembayaran', 'Prediksi_Kelayakan']])

# Menampilkan nasabah yang layak diberikan kredit
nasabah_layak = data[data['Prediksi_Kelayakan'] == 'Layak']
print("\nNasabah yang Layak diberikan Kredit:")
print(nasabah_layak[['ID', 'Nama', 'Umur', 'Pendapatan', 'Status_Pekerjaan', 'Jumlah_Pinjaman', 'Lama_Pinjaman', 'Riwayat_Pembayaran']])

# Render Decision Tree menggunakan matplotlib
feature_names = X.columns
class_names = le_kelayakan.inverse_transform([0, 1])

plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=feature_names, class_names=class_names, filled=True, rounded=True, fontsize=12)
plt.title("Decision Tree")
plt.show()

# Function for user input
def input_nasabah():
    umur = int(input("Masukkan Umur: "))
    pendapatan = int(input("Masukkan Pendapatan: "))
    status_pekerjaan = input("Masukkan Status Pekerjaan (Karyawan Tetap/Pengusaha/Karyawan Kontrak): ")
    jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
    lama_pinjaman = int(input("Masukkan Lama Pinjaman (dalam bulan): "))
    riwayat_pembayaran = input("Masukkan Riwayat Pembayaran (Baik/Cukup Baik/Buruk): ")
    
    # Check if the input is in the label encoder's known classes
    if status_pekerjaan not in le_status.classes_:
        print(f"Status Pekerjaan tidak dikenal. Pilihan yang valid adalah: {list(le_status.classes_)}")
        return
    if riwayat_pembayaran not in le_riwayat.classes_:
        print(f"Riwayat Pembayaran tidak dikenal. Pilihan yang valid adalah: {list(le_riwayat.classes_)}")
        return

    # Encode inputs
    status_pekerjaan_encoded = le_status.transform([status_pekerjaan])[0]
    riwayat_pembayaran_encoded = le_riwayat.transform([riwayat_pembayaran])[0]

    # Create DataFrame
    user_data = pd.DataFrame([[umur, pendapatan, status_pekerjaan_encoded, jumlah_pinjaman, lama_pinjaman, riwayat_pembayaran_encoded]],
                             columns=feature_names)
    
    # Predict using model
    prediksi = model.predict(user_data)
    kelayakan = le_kelayakan.inverse_transform(prediksi)[0]
    print(f"Prediksi Kelayakan Kredit: {kelayakan}")

# User input
input_nasabah()
