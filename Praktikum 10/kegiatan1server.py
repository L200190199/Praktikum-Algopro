import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 20009))
s.listen(5)
print "Server Program Komunikasi Tentang Data Diri"
data = ""
kamus = {"nama" : "Muhammad Sofiyan Hadi",
         "NIM" : "L200190199",
         "angkatan" : "2019",
         "keluar" : "Siap!!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, perintah tidak dimengerti")
