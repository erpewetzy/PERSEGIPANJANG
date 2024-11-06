#fungsi untuk memeriksa apakah input adalah bilangan positif
def input_positif(prompt):
    while true:
        try:
            nilai = float(input(prompt))
            if nilai > 0:
                return nilai
            else:
                print("nilai harus lebih dari 0,coba lagi")
        except ValueError:
            print("input tidak valid ,masukan angka.")

#meminta input panjang dan lebar dari pengguna
Panjang = float(input("masukan panjang persegi panjang:"))
Lebar = float(input("masukan lebaprint(f"Keliling persegi panjang adalah: {Keliling} satuan")r persegi panjang:"))

#menghitung luas
Luas = Panjang * Lebar

#menghitung keliling

#menampilkan hasil luas
keliling = 2 * (Panjang + Lebar )

#menampilkan hasil luas dan keliling
print(f"Luas persegi panjang: {Luas} satuan persegi")
print(f"keliling persegi panjang adalah:{keliling}satuan")
