#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import ttk
import MySQLdb

# Open database connection
server = "localhost"
user = "root"
password = ""
database = "mysql"
db = MySQLdb.connect(server, user, password, database)
cursor = db.cursor()
if cursor:
    print "Baglanti Saglandi"
else:
    print "Baglanti Saglanamadi"

def ekle():
    sql = "INSERT INTO ogrenciler" \
          "(numara,adsoy,bolum) VALUES (%d, '%s', '%s')" % (int(numara.get()), adsoy.get(), bolum.get())
    cursor.execute(sql)
    db.commit()
    print "Öğrenci bilgileri eklendi..."
    listele()
    return True

def sil(id):
    sql = "DELETE FROM ogrenciler WHERE Id = %d" % int(id)
    cursor.execute(sql)
    db.commit()
    listele()

def guncelle(id, numara, adsoy, bolum):
    sql = "UPDATE ogrenciler" \
          " SET numara = %d, adsoy = '%s', bolum = '%s' WHERE Id = %d" % (int(numara), adsoy, bolum, int(id))
    cursor.execute(sql)
    db.commit()
    listele()

    return True

def listele():
    listbox.delete(0, END)
    sql = "SELECT * FROM ogrenciler"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        listbox.insert(END, row)


master = Tk()

def curselect(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    #id = (picked[0])

    id.insert(END, picked[0])
    numara.insert(END, picked[2])
    adsoy.insert(END, picked[1])
    bolum.insert(END, picked[3])


Label(master, text='id', width=25).grid(row=3)
Label(master, text='İsim Soyisim', width=25).grid(row=1)
Label(master, text='Numara', width=25).grid(row=2)
Label(master, text='Bölüm', width=25).grid(row=3)

id = Entry(master, width=25)
adsoy = Entry(master, width=25)
numara = Entry(master, width=25)
bolum = ttk.Combobox(master, width=25)
bolum['values'] = ('Bilgisayar', 'Otomotiv')
bolum.pack()

id.grid(row=0, column=1)
adsoy.grid(row=1, column=1)
numara.grid(row=2, column=1)
bolum.grid(row=3, column=1)

Button(master, text='Çıkış', command=master.quit).grid(row=4, column=0)
Button(master, text='Ekle', command=ekle).grid(row=4, column=1)
Button(master, text='Sil', command=lambda: sil(id.get())).grid(row=4, column=2)
Button(master, text='Güncelle', command=lambda: guncelle(id.get(), numara.get(), adsoy.get(), bolum.get())).grid(
                                                row=4, column=3)
Button(master, text='Listele', command=listele).grid(row=4, column=4, sticky=W, pady=4)

listbox = Listbox(master, width=50, height=20)
listbox.pack()
listbox.grid(row=6, column=1)

listbox.bind('<<ListboxSelect>>', curselect)



mainloop()


