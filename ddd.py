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

def ogrenciekle():
    sql = "INSERT INTO ogrenciler" \
          "(numara,adsoy,bolum) VALUES (%d, '%s', '%s')" % (int(numara.get()), adsoy.get(), bolum.get())
    cursor.execute(sql)
    db.commit()
    print "Öğrenci bilgileri eklendi..."
    ogrencilistele()
    return True


def ogrenciguncelle(id, numara, adsoy, bolum):
    sql = "UPDATE ogrenciler" \
          " SET numara=%d, adsoy='%s', bolum='%s' WHERE Id= %d" % (int(numara), adsoy, bolum, int(id))
    print sql
    cursor.execute(sql)
    db.commit()
    print "Öğrenci bilgileri güncellendi"
    ogrencilistele()
    #gunc.destroy()
    return True

def sil(id):
    sql = "DELETE FROM ogrenciler WHERE Id = %d" % int(id)
    cursor.execute(sql)
    db.commit()
    print "Silindi"
    ogrencilistele()

def ogrencilistele():
    listbox.delete(0, END)
    sql = "SELECT * FROM ogrenciler"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        listbox.insert(END, row)

gunc = Tk()

def curselect(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    # id=(picked[0])

    Label(gunc, text="Id :").grid(row=3, sticky=W)
    Label(gunc, text="Numara :").grid(row=0)
    Label(gunc, text="Adı Soyadı :").grid(row=1)
    Label(gunc, text="Bölümü : ").grid(row=2)

    bolum2 = ttk.Combobox(gunc)
    bolum2.pack()
    bolum2['values'] = ('Bilgisayar', 'Makine', ' Elektronik', 'Endüstri')

    id2 = Entry(gunc, width=25)
    numara2 = Entry(gunc, width=25)
    adsoy2 = Entry(gunc, width=25)

    id2.insert(END, picked[0])
    numara2.insert(END, picked[2])
    adsoy2.insert(END, picked[1])
    bolum2.insert(END, picked[3])

    numara2.grid(row=0, column=1)
    adsoy2.grid(row=1, column=1)
    bolum2.grid(row=2, column=1)
    id2.grid(row=3, column=1)
    Button(gunc, text='Guncelle', command=lambda: ogrenciguncelle(id2.get(), numara2.get(), adsoy2.get(),
                                                                      bolum2.get())).grid(row=5, column=1, sticky=W, pady=4)
    Button(gunc, text='Sil', command=lambda: sil(id2.get())).grid(row=6, column=1, sticky=W, pady=4)


master = Tk()
Label(master, text="Numara :").grid(row=0)
Label(master, text="Adı Soyadı :").grid(row=1)
Label(master, text="Bölümü :").grid(row=2)



numara = Entry(master, width=25)
adsoy = Entry(master, width=25)
bolum = ttk.Combobox(master, width=25)
bolum.pack()
bolum['values'] = ('Bilgisayar', 'Elektronik', 'Makine', 'Endüstri')
listbox = Listbox(master, width=50, height=20)
listbox.pack()

numara.grid(row=0, column=1)
adsoy.grid(row=1, column=1)
bolum.grid(row=2, column=1)
listbox.grid(row=4, column=1)
listbox.bind('<<ListboxSelect>>', curselect)

Button(master, text='Çıkış', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Ekle', command=ogrenciekle).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Listele', command=ogrencilistele).grid(row=3, column=2, sticky=W, pady=4)

#ogrencilistele()
mainloop()
