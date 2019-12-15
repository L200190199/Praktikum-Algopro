from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Judul Aplikasi')

L0 = Label(app, text="Bangun Geometri", font=("Arial", 16))
L0.grid(row=0, column=0, sticky="W")

DESC = Label(app, text="Dalam geometri, prisma adalah bangun ruang tiga dimensi yang dibatasi oleh alas dan tutup identik berbentuk segi-n dan sisi-sisi tegak berbentuk persegi atau persegi panjang.", wraplength=250)
DESC.grid(row=1, sticky="W")

DIMENSI  = Label(app, text="Prisma merupakan geometri tiga dimensi")
DIMENSI.grid(row=2, sticky="W")

CONTOH = Label(app, text="Contoh Prisma adalah tenda ")
CONTOH.grid(row=3, sticky="W")

L3 = Label (app, text= "Luas Alas")
L3.grid(row = 4, column = 1, sticky = "w")

L4 = Label (app, text= "Luas Selimut")
L4.grid(row = 5, column = 1, sticky = "w")

LuasAlas = IntVar()
E3 = Entry(app, textvariable = LuasAlas)
E3.grid(row = 4, column = 2)

LuasSelimut = IntVar()
E4 = Entry(app, textvariable = LuasSelimut)
E4.grid(row = 5, column = 2)

H = Label(app, text = "Luas Prisma")
H.grid(row = 6, column = 1, sticky="w")

H1 = Label(app)
H1.grid(row = 6, column = 2, sticky="w")

def Hitung():
          hasil = 2*LuasAlas.get()+ LuasSelimut.get()

          H1.config(text = hasil)

B1 = Button(app, text = "Hitung", width="8", command = lambda:Hitung())
B1.grid(row = 7, column = 2)

app.mainloop()

