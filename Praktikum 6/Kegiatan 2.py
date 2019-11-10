## Program Akun
## Dibuat oleh Sofiyan L200190199
import random
angka = random.randint(0,1000)

Nama = 'Muhammad Sofiyan Hadi'
TanggalLahir = '05 Agustus 2001'
NamaSingkat = Nama[0] + '.' + Nama[9] + '.' + Nama[17:]
Username = Nama[9] + TanggalLahir[0:2] + TanggalLahir[11:]
Password = Nama[0:3] + str(angka)
