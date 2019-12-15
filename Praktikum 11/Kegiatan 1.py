from tkinter import Tk, Label, Button

my_app = Tk(className="Kegiatan 1")
my_app.geometry("300x250")

L = Label (my_app, text = "Data diri", font=("Arial, 25"))
L.grid(row=0, column=0)

L1 = Label(my_app, text = "Nama")
L1.grid(row=1, column=0, sticky="w")
L6 = Label(my_app, text = "Muhammad Sofiyan Hadi ")
L6.grid(row=1, column=1, sticky="w")

L2 = Label(my_app, text = "NIM")
L2.grid(row=2, column=0, sticky="w")
L7 = Label(my_app, text = "L200190199 ")
L7.grid(row=2, column=1, sticky="w")

L3 = Label(my_app, text = "Buku Favorit")
L3.grid(row=3, column=0, sticky="w")
L8 = Label(my_app, text = "Senja di Warung Kopi")
L8.grid(row=3, column=1, sticky="w")

L4 = Label(my_app, text = "Idola di kalangan sahabat")
L4.grid(row=4, column=0, sticky="w")
L9 = Label(my_app, text = "Umar bin Khattab")
L9.grid(row=4, column=1, sticky="w")

L5 = Label(my_app, text = "Motto")
L5.grid(row=5, column=0, sticky="w")
L10 = Label(my_app, text ="Belajar dari kegagalan")
L10.grid(row=5, column=1, sticky="w")

def tutup():
    my_app.destroy()

B = Button(my_app, text = "Tutup", command = tutup)
B.grid(row=6, column=1, sticky="w")

my_app.mainloop()
           
