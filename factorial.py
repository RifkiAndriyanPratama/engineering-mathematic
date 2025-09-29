n = 18 # kita mau cari factorial 18 yang kita simpen di varibel n
fact = 1 # varibel buat nyimpen hasil perkalian faktorial kenapa mulai dari 1? because klo 0 hasilnya bakal 0 semua

for i in range(1, n+1):
    fact = fact * i

print(fact)
