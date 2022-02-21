import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)


def search():
    q2=q.get()
    query = "SELECT * FROM rubber_compounds WHERE ID LIKE '%"+q2+"%' "
    cur.execute(query)
    rows = cur.fetchall()
    update(rows)


def clear():
    sql = "SELECT * FROM rubber_compounds"
    cur.execute(sql)
    rows = cur.fetchall()
    update(rows)
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent8.delete(0, END)
    ent9.delete(0, END)
    ent10.delete(0, END)
    ent11.delete(0, END)
    ent12.delete(0, END)
    ent13.delete(0, END)
    ent14.delete(0, END)


def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    rowidv.set(rowid)
    #print(rowid)
    #print(rowidv)
    tid.set(item['values'][0])
    t1.set(item['values'][1])
    t2.set(item['values'][2])
    t3.set(item['values'][3])
    t4.set(item['values'][4])
    t5.set(item['values'][5])
    t6.set(item['values'][6])
    t7.set(item['values'][7])
    t8.set(item['values'][8])
    t9.set(item['values'][9])
    t10.set(item['values'][10])
    t11.set(item['values'][11])
    t12.set(item['values'][12])
    t13.set(item['values'][13])
    t14.set(item['values'][14])
    #t15.set(item['values'][15])

def update_rubber():
    rubber_id = tid.get()
    t1 = ent1.get()
    t2 = ent2.get()
    t3 = ent3.get()
    t4 = ent4.get()
    t5 = ent5.get()
    t6 = ent6.get()
    t7 = ent7.get()
    t8 = ent8.get()
    t9 = ent9.get()
    t10 = ent10.get()
    t11 = ent11.get()
    t12 = ent12.get()
    t13 = ent13.get()
    t14 = ent14.get()
    if messagebox.askyesno("Confirm Update?", "Are you sure you want to update this rubber compound?"):
        cur.execute('''UPDATE rubber_compounds SET 'ID' = ?,'SSBR(phr)' = ?, 'N330' = ?, 'Silica' = ?, 
        'TESPD'=?, 'ZnO'=?, 'S Acid'=?, '6PPD'=?, 'Sulfur'=?,'DPG'=?, 'CBS'=?,'T90(hr:min)'=?, 
        'Cost per KG'=?, 'Volume per KG'=? WHERE sl = ?''',
                    (t1, t2, t3, t4, t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,rubber_id))

        con.commit()
        clear()
    else:
        return True


def add_new():
    t1 = ent1.get()
    t2 = ent2.get()
    t3 = ent3.get()
    t4 = ent4.get()
    t5 = ent5.get()
    t6 = ent6.get()
    t7 = ent7.get()
    t8 = ent8.get()
    t9 = ent9.get()
    t10 = ent10.get()
    t11 = ent11.get()
    t12 = ent12.get()
    t13 = ent13.get()
    t14 = ent14.get()

    cur.execute("insert into rubber_compounds ('ID','SSBR(phr)','N330','Silica','TESPD','ZnO', 'S Acid',"
                " '6PPD','Sulfur','DPG','CBS','T90(hr:min)','Cost per KG', 'Volume per KG')"
                "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (t1, t2, t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14))

    con.commit()
    clear()
    return True

def delete_rubber():
    rubber_id=t1.get()
    if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this compound?"):
        query = "DELETE  FROM rubber_compounds WHERE rubber_compounds.ID = "+'"'+rubber_id+'"'
        cur.execute(query)
        #print(rubber_id)
        con.commit()
        clear()

    else:
        return True


con = sqlite3.connect('/home/rubber.db')
cur = con.cursor()
sql = "SELECT * FROM rubber_compounds"
cur.execute(sql)

root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()
t14 = StringVar()
t15 = StringVar()
rowidv = StringVar()
tid = StringVar()

wrapper1 = LabelFrame(root, text="Rubber Compounds")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Rubber Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv= ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), show="headings", height=8)
trv.pack()
trv.column(1, anchor=CENTER,width=30)
trv.column(2, anchor=CENTER,width=100) # This will center text in rows
trv.column(3, anchor=CENTER, width=100)
trv.column(4, anchor=CENTER, width=70)
trv.column(5, anchor=CENTER, width=70)
trv.column(6, anchor=CENTER, width=70)
trv.column(7, anchor=CENTER, width=70)
trv.column(8, anchor=CENTER, width=70)
trv.column(9, anchor=CENTER, width=70)
trv.column(10, anchor=CENTER, width=70)
trv.column(11, anchor=CENTER, width=70)
trv.column(12, anchor=CENTER, width=70)
trv.column(13, anchor=CENTER, width=120)
trv.column(14, anchor=CENTER, width=120)
trv.column(15, anchor=CENTER, width=140)

trv.heading(1, text="Sl")
trv.heading(2, text="ID")
trv.heading(3, text="SSBR(phr)")
trv.heading(4, text="N330")
trv.heading(5, text="Silica")
trv.heading(6, text="TESPD")
trv.heading(7, text="ZnO")
trv.heading(8, text="S Acid")
trv.heading(9, text="6PPD")
trv.heading(10, text="Sulfur")
trv.heading(11, text="DPG")
trv.heading(12, text="CBS")
trv.heading(13, text="T90(hr:min)")
trv.heading(14, text="Cost per KG")
trv.heading(15, text="Volume per KG")
trv.bind('<Double 1>', getrow)

sql = "SELECT * FROM rubber_compounds"
cur.execute(sql)
rows=cur.fetchall()
update(rows)


# search section
lbl = Label(wrapper2, text="Search ID")
lbl.pack(side=tk.LEFT, padx=10)
ent=Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Clear", command=clear)
btn.pack(side=tk.LEFT, padx=6)

# user Data section
lbl1 = Label(wrapper3, text="ID",width=7)
lbl1.grid(row=0, column=0, pady=3)
ent1= Entry(wrapper3, textvariable=t1,width=7)
ent1.grid(row=1, column=0, pady=3)

lbl2 = Label(wrapper3, text="SSBR(phr)",width=10)
lbl2.grid(row=0, column=1, padx=5, pady=3)
ent2= Entry(wrapper3, textvariable=t2,width=10)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="N 330", width=7)
lbl3.grid(row=0, column=2, pady=3)
ent3= Entry(wrapper3, textvariable=t3,width=7)
ent3.grid(row=1, column=2, pady=3)

lbl4 = Label(wrapper3, text="Silica",width=7)
lbl4.grid(row=0, column=3, pady=3)
ent4= Entry(wrapper3, textvariable=t4, width=7)
ent4.grid(row=1, column=3, pady=3)

lbl5 = Label(wrapper3, text="TESPD",width=7)
lbl5.grid(row=0, column=4, pady=3)
ent5= Entry(wrapper3, textvariable=t5,width=7)
ent5.grid(row=1, column=4, pady=3)

lbl6 = Label(wrapper3, text="ZnO", width=7)
lbl6.grid(row=0, column=5, pady=3)
ent6= Entry(wrapper3, textvariable=t6, width=7)
ent6.grid(row=1, column=5, pady=3)

lbl7 = Label(wrapper3, text="S Acid", width=7)
lbl7.grid(row=0, column=6, pady=3)
ent7= Entry(wrapper3, textvariable=t7, width=7)
ent7.grid(row=1, column=6, pady=3)

lbl8 = Label(wrapper3, text="6PPD", width=7)
lbl8.grid(row=0, column=7, pady=3)
ent8= Entry(wrapper3, textvariable=t8, width=7)
ent8.grid(row=1, column=7, pady=3)

lbl9 = Label(wrapper3, text="Sulfur", width=7)
lbl9.grid(row=0, column=8, pady=3)
ent9= Entry(wrapper3, textvariable=t9,width=7)
ent9.grid(row=1, column=8, pady=3)

lbl10 = Label(wrapper3, text="DPG", width=7)
lbl10.grid(row=0, column=9, pady=3)
ent10= Entry(wrapper3, textvariable=t10, width=7)
ent10.grid(row=1, column=9, pady=3)

lbl11 = Label(wrapper3, text="CBS", width=7)
lbl11.grid(row=0, column=10, pady=3)
ent11= Entry(wrapper3, textvariable=t11, width=7)
ent11.grid(row=1, column=10, pady=3)

lbl12 = Label(wrapper3, text="T90(hr:min)",width=12)
lbl12.grid(row=0, column=11, pady=3)
ent12= Entry(wrapper3, textvariable=t12, width=12)
ent12.grid(row=1, column=11, pady=3)

lbl13 = Label(wrapper3, text="Cost per KG", width=12)
lbl13.grid(row=0, column=12, pady=3)
ent13= Entry(wrapper3, textvariable=t13, width=12)
ent13.grid(row=1, column=12, pady=3)

lbl14 = Label(wrapper3, text="Volume per KG", width=14)
lbl14.grid(row=0, column=13, pady=3)
ent14= Entry(wrapper3, textvariable=t14, width=14)
ent14.grid(row=1, column=13, pady=3)

up_btn = Button(wrapper3, text="Update", command=update_rubber)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_rubber)

add_btn.grid(row=6, column=3, pady=20)
up_btn.grid(row=6, column=7, pady=20)
delete_btn.grid(row=6, column=11, pady=20)


root.title("Rubber Data")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

root.mainloop()
