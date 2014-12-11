from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timeit import default_timer as timer
 
j=-1
def läbi():
    raam6.destroy()
def läbi2():
    raam7.destroy()
valesti=0
def kontrolli(sisendvaartus2,küsitav,vastus,raam3,j,m):
 
    sisestatud = sisendvaartus2.get()
 
    j += 1 
    m+=1
    global valesti
 
    if sisestatud.lower() == vastus[j]:
         pass
    else:
        küsitav.append(küsitav[j])
        vastus.append(vastus[j])
        messagebox.showinfo(title="Läks valesti",message="Õige vastus: "+ vastus[j]+"\n" +\
            "Sisestati: "+ sisestatud+ "\n"+ "(Suur- ja väiketähed ei mängi rolli)")
        valesti+=1
       
    tühi=""
    raam3.destroy()
   
    tõlk(m, küsitav, vastus,tühi,j)
               
def tõlk(n,küsitav, vastus,raam2,j):
   
##    if len(küsitav) == 0:
##            messagebox.showinfo(title="Viga",message="Oled jätnud sõnade faili tühjaks, lisa sõnad!")
##            algus(j,0)
           
    if n >= len(küsitav):
       
        global valesti
 
        end=timer()
        x=str(round(end-start,2))
            
        protsent= str(round(int(int(valesti)/len(küsitav)*100),0))
        global raam6
        raam6 = Tk()
        raam6.title("Läbi sai")
 
        j2=-1
       
        lõpp = ttk.Button(raam6, text="Uuesti!", command=lambda: algus(j2,0))
        lõpp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        
        kõik = ttk.Button(raam6, text="Kõik", command=lambda: läbi())
        kõik.grid(column=0, row=3, padx=5, pady=5, sticky=(N, S, E))
        misedasi = ttk.Label(raam6, text="Kui soovid uuesti, vajuta nuppu: 'Uuesti!'"+"\n"+\
        "\n"+"Valesid vastuseid: "+str(valesti)+"\n" +"Valesti oli: "+protsent+"% -i kõikidest sõnadest"+ "\n" +\
        "Aega kulus: " +x+ " sekundit"
                             )
        misedasi.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
        #messagebox.showinfo(title="Tulemus", message="Valesid vastuseid: "+str(valesti)+\
                     #       "\n" +"Valesti oli: "+protsent+"% -i kõikidest sõnadest"+ "\n" + \
                      #      "Aega kulus: " +x+ " sekundit")
            
    else:     
        if n==0:
             
            raam3 = Tk()
            raam3.title("Tõlkeprogramm")
            küsitav2 = ttk.Label(raam3, text=küsitav[n])
            küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
           
            sisendvaartus = ttk.Entry(raam3)
            #jou.set(sisendvaartus)
            sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
            raam3.bind("<Return>", lambda event: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            raam3.focus_set()             
            nupp1 = ttk.Button(raam3, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
            raam2.destroy()
        
        else:
            raam3 = Tk()
            raam3.title("Tõlkeprogramm")
            küsitav2 = ttk.Label(raam3, text=küsitav[n])
            küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
           
            sisendvaartus = ttk.Entry(raam3)
            #jou.set(sisendvaartus)
            sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
            raam3.bind("<Return>", lambda event: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            raam3.focus_set()
            nupp1 = ttk.Button(raam3, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        
def proov(j, küsibfailinime, esteng1,n):
   
    raam2 = Tk()
    raam2.title("oled valmis?")
    #raam2.geometry("400x100")
    
    tahvel2 = Canvas(raam2,  background="lightblue")
    tahvel2.grid()
    #raam2 = ttk.Label(tahvel2,text="Ole valmis!")
    #raam2.grid(column=0, row=0,padx=100, pady=200,  sticky=(E,N,W))
    failinimi=küsibfailinime.get()
    f=open(failinimi)
 
    mispidi=esteng1.get()
 
    küsitav=[]
    vastus=[]
    n=0
    for rida in f:
        sõna=rida.strip().split("-")
 #       if rida=="":
#            messagebox.showinfo(title="Viga",message="Oled jätnud sõnade faili tühjaks!")
#            break
                
        if mispidi=="ING-EST":
            küsitav.append(sõna[0].lower())
            vastus.append(sõna[1].lower())
           
        elif mispidi=="EST-ING":
            küsitav.append(sõna[1].lower())
            vastus.append(sõna[0].lower())
    
    #raam2.bind("<Return>", lambda event: tõlk(n,küsitav,vastus, raam2,j))
    #raam2.focus_set()
    nupp2 = ttk.Button(tahvel2, text="TEST", command=lambda: tõlk(n,küsitav,vastus, raam2,j))
    nupp2.grid(column=1, row=1, padx=100, pady=50, sticky=(N, S, W, E))

    
    #.pack()
    if len(küsitav) == 0:
        global raam7
        raam7=Tk()
        raam7.title("Viga!")
        tahvel7 = Canvas(raam7, background="green")

        tahvel7.place(anchor=CENTER)
        tahvel7.grid()
       # messagebox.showinfo(title="Viga",message="Oled jätnud sõnade faili tühjaks, lisa sõnad!")
        veateade = ttk.Label(tahvel7, text="Oled jätnud sõnade faili tühjaks, lisa sõnad!")
        veateade.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))

        lõpp = ttk.Button(tahvel7, text="Uuesti!", command=lambda: algus(-1,0))
        lõpp.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, W, E))

        panenkinni = ttk.Button(tahvel7, text="Sule aken", command= läbi2)
        panenkinni.grid(column=1, row=0, padx=5, pady=5, sticky=(N, S, E))
        raam2.destroy()    
 
    raam.destroy()
   
    global start
    start=timer()   
    #.pack()
    #nupp.grid(column=1, row=3, padx=200, pady=60, sticky=(N, S, W, E))
       
 #       raam.mainloop()                  
#sõnade küsimine
def algus(j,n):
    
    global raam
    raam = Tk()
    raam.title("Tõlkeprogramm")

     #   pilt = PhotoImage(file="proov3.gif")
    #bg_img = PhotoImage(file='proov3.gif')
    #bg_lbl = Label(raam, image=bg_img)
    #bg_lbl.grid(column=0,row=0, padx=0, pady=0, sticky=(N,S,W,E))
    pilt=PhotoImage(file="proov3.gif")
    tahvel = Canvas(raam, background="pink")

    tahvel.place(anchor=CENTER)
    tahvel.grid()
    kuidasSisestada = ttk.Label(tahvel, text="Sisesta sõnad faili vastavalt: cat-kass dog-koer")
    kuidasSisestada.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
    #background_image=PhotoImage(file="taust.jpg")
    #background=Label(raam,image=background_image, bd=0)
    #background.pack()
    failinimi2 = ttk.Label(tahvel, text="Sisesta faili nimi, mis on samas kaustas käesoleva programmiga (NT:('sonad.txt')):")
    failinimi2.grid(column=0, row=1, padx=5, pady=5, sticky=(N, E, W))
 
    esteng = ttk.Label(tahvel, text="Kui soovid, et programm küsiks inglise keeles, sisesta: ING-EST ja vastupidi: EST-ING:")
    esteng.grid(column=0, row=2, padx=5, pady=5, sticky=(N, E, W))
 
#lahtrid
    küsibfailinime = ttk.Entry(tahvel)
    küsibfailinime.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))
 
    esteng1 = ttk.Entry(tahvel)
    esteng1.grid(column=1, row=2, padx=5, pady=5, sticky=(N, W, E))
   
#Teen nupu ning annan commandi talle selle, mis ta teeb kui vajutatakse nuppu, ehk siis funktsiooni

    nupp = ttk.Button(tahvel, text="Hakkame pihta!", command=lambda:proov(j,küsibfailinime,esteng1,n))
    nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))


#Nupp suureneb/laieneb kui liigutatakse akent
    nupp.columnconfigure(1, weight=1)
    nupp.rowconfigure(3, weight=1)
    #nupp.mainloop()

    
#Aken tuleb ekraanile
#raam.mainloop()
 
algus(j,0)
