from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
j=-1
m=0
def kontrolli(sisendvaartus2,küsitav,vastus,raamlala):
 
    global j
    sisestatud = sisendvaartus2.get()
    print(vastus)
    print(küsitav)
 
    j += 1
    global m
    m+=1
 
    if sisestatud.lower() == vastus[j]:
        print("õige")    
    else:
        küsitav.append(küsitav[j])
        vastus.append(vastus[j])
        print("vale")
        print("Õige vastus on: " + vastus[j])
       
    raamlala.destroy()
    tõlk(m, küsitav, vastus,raam5)
               
def tõlk(n,küsitav, vastus,raam):
 
    if n >= len(küsitav):
        print("Kõik")
    else:
        raam3 = Tk()
        raam3.title("Tõlkeprogramm")
        küsitav2 = ttk.Label(raam3, text=küsitav[n])
        küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
       
        sisendvaartus = ttk.Entry(raam3)
        #jou.set(sisendvaartus)
        sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
                     
        nupp1 = ttk.Button(raam3, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus,raam3))
        nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        raam2.destroy()
 
 
def proov():
    raam2 = Tk()
    raam2.title("oled valmis?")
    raam2.geometry("400x100")
 
    failinimi=küsibfailinime.get()    
    f=open(failinimi)
 
    mispidi=esteng1.get()
 
    küsitav=[]
    vastus=[]
 
    for rida in f:
        sõna=rida.strip().split("-")
       
        if mispidi=="ING-EST":
            küsitav.append(sõna[0].lower())
            vastus.append(sõna[1].lower())
 
        elif mispidi=="EST-ING":
            küsitav.append(sõna[1].lower())
            vastus.append(sõna[0].lower())
    nupp = ttk.Button(raam, text="TEST", command=lambda: tõlk(0,küsitav,vastus, raam2))
    #.pack()
    nupp.grid(column=1, row=3, padx=200, pady=60, sticky=(N, S, W, E))
 
   
       
 #       raam.mainloop()
                     
#sõnade küsimine
   
raam = Tk()
raam.title("Tõlkeprogramm")
kuidasSisestada = ttk.Label(raam, text="Sisesta sõnad faili vastavalt: cat-kass dog-koer, kõik väikeste tähtedega")
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
nupp = ttk.Button(raam, text="Hakkame pihta!", command= proov)
nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
 
 
#Nupp suureneb/laieneb kui liigutatakse akent
raam.columnconfigure(1, weight=1)
raam.rowconfigure(3, weight=1)
#Aken tuleb ekraanile
#raam.mainloop()
