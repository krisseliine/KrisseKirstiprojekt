from tkinter import *
from tkinter import ttk
from tkinter import messagebox

j=-1
m=0
def kontrolli(sisendvaartus2,küsitav,vastus):

 

    global j
    sisestatud = sisendvaartus2.get()
    print(vastus)
    print(küsitav)

    j += 1
    global m
    m+=1


    if sisestatud == vastus[j]:
        print("õige")

      
    else:
        küsitav.append(küsitav[j])
        vastus.append(vastus[j])
        print("vale")
        print("Õige vastus on: " + vastus[j])
        
    
    tõlk(m, küsitav, vastus)


                
def tõlk(n,küsitav, vastus):

    if n >= len(küsitav):
        print("Kõik")

    else:

        raam = Tk()
        raam.title("Tõlkeprogramm")
        küsitav2 = ttk.Label(raam, text=küsitav[n])
        küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
        
        sisendvaartus = ttk.Entry(raam)
        #jou.set(sisendvaartus)
        sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
         
              
        nupp1 = ttk.Button(raam, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus))
        nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))

def proov():
    raam = Tk()
    raam.title("oled valmis?")

    failinimi=küsibfailinime.get()    
    f=open(failinimi)
 
    mispidi=esteng1.get()
  
    küsitav=[]
    vastus=[]

    for rida in f:
        sõna=rida.strip().split("-")
       
        if mispidi=="ING-EST":
            küsitav.append(sõna[0])
            vastus.append(sõna[1])
 
        elif mispidi=="EST-ING":
            küsitav.append(sõna[1])
            vastus.append(sõna[0])
    nupp = ttk.Button(raam, text="TEST", command=lambda: tõlk(0,küsitav,vastus))
    nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        
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
nupp = ttk.Button(raam, text="Sisestatud!", command= proov)
nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))


 
 
#Nupp suureneb/laieneb kui liigutatakse akent
raam.columnconfigure(1, weight=1)
raam.rowconfigure(3, weight=1)
#Aken tuleb ekraanile
#raam.mainloop()

