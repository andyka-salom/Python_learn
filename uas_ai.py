import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

# Membaca data dari file CSV
data = pd.read_csv('data_nasabah.csv')

# Encoding fitur kategori
le = LabelEncoder()
data['Status_Pekerjaan'] = le.fit_transform(data['Status_Pekerjaan'])
data['Riwayat_Pembayaran'] = le.fit_transform(data['Riwayat_Pembayaran'])
data['Kelayakan_Kredit'] = le.fit_transform(data['Kelayakan_Kredit'])

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
data['Prediksi_Kelayakan'] = le.inverse_transform(data['Prediksi_Kelayakan'])

# Menampilkan hasil analisa dan nasabah yang layak diberikan kredit
print("\nHasil Analisa Pemberian Kredit:")
print(data[['ID', 'Nama', 'Umur', 'Pendapatan', 'Status_Pekerjaan', 'Jumlah_Pinjaman', 'Lama_Pinjaman', 'Riwayat_Pembayaran', 'Prediksi_Kelayakan']])

# Menampilkan nasabah yang layak diberikan kredit
nasabah_layak = data[data['Prediksi_Kelayakan'] == 'Layak']
print("\nNasabah yang Layak diberikan Kredit:")
print(nasabah_layak[['ID', 'Nama', 'Umur', 'Pendapatan', 'Status_Pekerjaan', 'Jumlah_Pinjaman', 'Lama_Pinjaman', 'Riwayat_Pembayaran']])
