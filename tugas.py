class ForwardChainingExpertSystem:
    def __init__(self):
        self.rules = {
            1: {'conditions': [1, 2, 3, 4], 'result': 1},
            2: {'conditions': [5], 'result': 2},
            3: {'conditions': [5, 6], 'result': 3},
            4: {'conditions': [5, 7, 8], 'result': 4},
            5: {'conditions': [9], 'result': 5},
            6: {'conditions': [5, 10, 11, 12], 'result': 6},
            7: {'conditions': [5, 10, 13, 14], 'result': 7},
            8: {'conditions': [5, 17], 'result': 8},
            9: {'conditions': [8, 6, 7], 'result': 9},
            10: {'conditions': [5, 18], 'result': 10},
            11: {'conditions': [3, 19], 'result': 11},
            12: {'conditions': [1, 11, 20], 'result': 12},
            13: {'conditions': [11, 21, 22, 25], 'result': 13},
            14: {'conditions': [13, 1, 23, 24], 'result': 14},
            15: {'conditions': [13, 25, 26], 'result': 15},
            16: {'conditions': [11, 27, 28, 29, 30], 'result': 16},
            17: {'conditions': [11, 27, 28, 31, 32, 33, 34], 'result': 17},
            18: {'conditions': [11, 35, 36], 'result': 18}
        }
        self.symptoms = {
            1: "Anak tidak bisa minum atau menyusu",
            2: "Anak memuntahkan makanan yang dimakan",
            3: "Anak menderita kejang",
            4: "Anak tampak letargis atau tidak sadar",
            5: "Napas Normal",
            6: "Napas cepat",
            7: "Tarikan dinding dada ke dalam",
            8: "Stridor",
            9: "Berak cair atau lembek",
            10: "Mata cekung",
            11: "Cubitan kulit perut kembali lambat",
            12: "Gelisah, rewel/mudah marah",
            13: "Haus, minum dengan lahap",
            14: "Cubitan kulit perut sangat lambat",
            15: "Anak tampak letargis atau tidak sadar",
            16: "Tidak bisa minum atau malas minum",
            17: "Diare 14 hari atau lebih",
            18: "Ada darah dalam tinja",
            19: "Suhu badan melebihi 37.5º C",
            20: "Kaku kuduk (anak tidak bisa menunduk hingga dagu mencapai dada)",
            21: "Ruam kemerahan di kulit",
            22: "batuk pilek atau mata merah",
            23: "Luka di mulut yang dalam atau luas",
            24: "Kekeruhan pada kornea mata",
            25: "Luka di mulut",
            26: "Mata bernanah",
            27: "Demam 2 - 7 hari",
            28: "Demam mendadak tinggi dan terus menerus",
            29: "Nyeri di ulu hati",
            30: "bintik bintik merah",
            31: "Muntah bercampur darah / seperti kopi",
            32: "Tinja berwarna hitam",
            33: "Perdarahan dihidung dan gusi",
            34: "Syok dan gelisah",
            35: "Infeksi",
            36: "Pilek"
        }
        self.diagnoses = {
            1: "Tanda Bahaya Umum",
            2: "Batuk",
            3: "Pneumonia",
            4: "Pneumonia Berat",
            5: "Diare",
            6: "Diare Dehidrasi Ringan",
            7: "Diare Dehidrasi Berat",
            8: "Diare Persisten",
            9: "Diare Persisten Berat",
            10: "Demam",
            11: "Demam dengan Tanda Bahaya Umum",
            12: "Campak",
            13: "Campak dengan komplikasi berat",
            14: "Demam Mungkin DBD",
            15: "DBD",
            16: "Demam bukan DBD"
        }
        self.facts = []

    def add_fact(self, symptom):
        self.facts.append(symptom)

    def diagnose(self):
        for rule_id, rule in self.rules.items():
            if all(cond in self.facts for cond in rule['conditions']):
                result = rule['result']
                return self.diagnoses[result]

    def print_symptoms(self):
        print("Gejala yang tersedia:")
        for code, symptom in self.symptoms.items():
            print(f"{code}. {symptom}")

    def get_symptom_description(self, code):
        return self.symptoms[code]


# Contoh penggunaan
expert_system = ForwardChainingExpertSystem()
expert_system.print_symptoms()

while True:
    symptom_code = input("Masukkan kode gejala yang dialami (atau ketik 'selesai' untuk mengakhiri): ")
    if symptom_code.lower() == 'selesai':
        break
    try:
        symptom_code = int(symptom_code)
        if symptom_code not in expert_system.symptoms:
            print("Kode gejala tidak valid. Silakan coba lagi.")
            continue
        symptom_description = expert_system.get_symptom_description(symptom_code)
        print(f"Gejala yang dipilih: {symptom_description}")
        expert_system.add_fact(symptom_code)
    except ValueError:
        print("Masukkan kode gejala dalam bentuk angka.")

diagnosis = expert_system.diagnose()
if diagnosis:
    print(f"\nDiagnosa: {diagnosis}")
else:
    print("\nTidak dapat membuat diagnosa dengan gejala yang diberikan.")
