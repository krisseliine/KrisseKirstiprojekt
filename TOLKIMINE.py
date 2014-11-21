from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
def tõlk():
    failinimi=küsibfailinime.get()
    f=open(failinimi)
 
    mispidi=esteng1.get()
   
    sõnastik={}
    for rida in f:
        sõna=rida.strip().split("-")
 
         
        if mispidi=="ING-EST":
            küsitav=sõna[0]
            vastus=sõna[1]
            sõnastik[küsitav]=vastus
            keys=list(sõnastik.keys())
        elif mispidi=="EST-ING":
            küsitav=sõna[1]
            vastus=sõna[0]
            sõnastik[küsitav]=vastus
            keys=list(sõnastik.keys())
    raam = Tk()
    raam.title("Tõlkeprogramm")
    i=0
    for sõna in keys:
        keys2 = ttk.Label(raam, text=sõna)
        keys2.grid(column=0, row=i, padx=5, pady=5, sticky=(E,N,W))
        vaartus = ttk.Entry(raam)
        vaartus.grid(column=1, row=i, padx=5, pady=5, sticky=(N, W, E))
        #Teen nupu ning annan commandi talle selle, mis ta teeb kui vajutatakse nuppu, ehk siis funktsiooni
        i+=1
    nupp1 = ttk.Button(raam, text="Kontrolli!", command=kontrolli)
    nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
       
    raam.mainloop()
def kontrolli():
    messagebox.showinfo(message = "Loading...")
       
                   
#sõnade küsimine
   
raam = Tk()
raam.title("Tõlkeprogramm")
kuidasSisestada = ttk.Label(raam, text="Sisesta sõnad faili vastavalt: cat-kass dog-koer")
kuidasSisestada.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
 
failinimi2 = ttk.Label(raam, text="Sisesta faili nimi, mis on samas kaustas käesoleva programmiga (NT:('sonad.txt')):")
failinimi2.grid(column=0, row=1, padx=5, pady=5, sticky=(N, E, W))
 
 
esteng = ttk.Label(raam, text="Kui soovid, et programm küsiks inglise keeles, sisesta: ING-EST ja vastupidi: EST-ING:")
esteng.grid(column=0, row=2, padx=5, pady=5, sticky=(N, E, W))
 
#lahtrid
küsibfailinime = ttk.Entry(raam)
küsibfailinime.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))
 
esteng1 = ttk.Entry(raam)
esteng1.grid(column=1, row=2, padx=5, pady=5, sticky=(N, W, E))
 
#Teen nupu ning annan commandi talle selle, mis ta teeb kui vajutatakse nuppu, ehk siis funktsiooni
nupp = ttk.Button(raam, text="Sisestatud!", command=tõlk)
nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
 
 
#Nupp suureneb/laieneb kui liigutatakse akent
raam.columnconfigure(1, weight=1)
raam.rowconfigure(3, weight=1)
#Aken tuleb ekraanile
raam.mainloop()
