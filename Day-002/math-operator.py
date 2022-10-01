# Urutan eksekusi operator matemarika
# 1. Tanda kurung ()
# 2. Pemangkatan (**)
# 3. Perkalian (*), Pembagian (/) => diurutkan dari paling kiri
# 3. Penjumlahan (+), Pengurangan (-) => diurutkan dari paling kiri

print(3 * 3 + 3 / 3 - 3) # = 7.0

print(3 * (3 + 3) / 3 - 3) # = 3.0