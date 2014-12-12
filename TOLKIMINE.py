from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timeit import default_timer as timer
import sys

def pilt():
    pildiraam=Tk()
    pildiraam.title("Olid tubli!")
    tahvelpilt = Canvas(pildiraam, width=700, height=400, background="white")
    tahvelpilt.grid()
    pall=PhotoImage(file="smile.gif")
    img = tahvelpilt.create_image(350, 200, image=pall)
    pildiraam.mainloop()

j=-1
global uus
uus=[]

def läbi():
    raam6.destroy()
    pildiraam=Tk()
    pildiraam.title("Olid tubli!")
    tahvelpilt = Canvas(pildiraam, width=700, height=400, background="white")
    tahvelpilt.grid()
    pall=PhotoImage(file="smile.gif")
    img = tahvelpilt.create_image(350, 200, image=pall)
    pildiraam.mainloop()
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
        
        uus.append(vastus[j])
        küsitav.append(küsitav[j])
        vastus.append(vastus[j])
        
        uus2 = uus.count(vastus[j])
        if uus2 < len(vastus[j]):
            if uus2 == 1:
                messagebox.showinfo(title="Läks valesti",message="Õige vastuse esimene täht on: "+ vastus[j][uus2-1]+"\n" +\
               "Sisestati: "+ sisestatud+ "\n"+ "(Suur- ja väiketähed ei mängi rolli)")
            else:
                messagebox.showinfo(title="Läks valesti",message="Õige vastuse esimesed tähed on: "+ vastus[j][0:uus2]+"\n" +\
               "Sisestati: "+ sisestatud+ "\n"+ "(Suur- ja väiketähed ei mängi rolli)")
 
        else:
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
        

        #lõpp3 = ttk.Button(pildiraam, text="Edu mulle!", command=lambda: algus(-1,0))
        #lõpp3.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        
        global valesti
 
        end=timer()
        x=str(round(end-start,2))
           
        protsent= str(round(int(int(valesti)/len(küsitav)*100),0))

        global raam6
        raam6 = Tk()
        raam6.resizable(width=FALSE, height=FALSE)
        raam6.title("Tulemus")
        tahvel6 = Canvas(raam6,  background="beige")
        tahvel6.grid()
        j2=-1
        
        lõpp = ttk.Button(tahvel6, text="Uuesti!", command=lambda: algus(j2,0))
        lõpp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
        k=str(len(küsitav))
        kõik = ttk.Button(tahvel6, text="Kõik", command=lambda: läbi())
        kõik.grid(column=0, row=3, padx=5, pady=5, sticky=(N, S, E))
        misedasi = ttk.Label(tahvel6, text="Valesid vastuseid: "+str(valesti)+", kokku küsiti: "+str(k)+"\n" +"Valesti oli: "\
                +protsent+"% -i kõikidest sõnadest"+ "\n" +\
        "Aega kulus: " +x+ " sekundit"+"\n"+"\n"+"Kui soovid uuesti, vajuta nuppu: 'Uuesti!'",background="beige")               
        misedasi.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
        
        #messagebox.showinfo(title="Tulemus", message="Valesid vastuseid: "+str(valesti)+\
                     #       "\n" +"Valesti oli: "+protsent+"% -i kõikidest sõnadest"+ "\n" + \
             #      "Aega kulus: " +x+ " sekundit")
   
    else:    
        if n==0:
             
            raam3 = Tk()
            raam3.resizable(width=FALSE, height=FALSE)
            raam3.title("Tõlgi")
            tahvel3 = Canvas(raam3,  background="beige")
            tahvel3.grid()
            küsitav2 = ttk.Label(tahvel3, text=küsitav[n],background="beige")
            küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
           
            sisendvaartus = ttk.Entry(tahvel3)
            #jou.set(sisendvaartus)
            sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
            raam3.bind("<Return>", lambda event: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            raam3.focus_set()            
            nupp1 = ttk.Button(tahvel3, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
            raam2.destroy()
       
        else:
 
            raam3 = Tk()
            raam3.resizable(width=FALSE, height=FALSE)
            raam3.title("Tõlgi")
            tahvel3 = Canvas(raam3,  background="beige")
            tahvel3.grid()
            küsitav2 = ttk.Label(tahvel3, text=küsitav[n],background="beige")
            küsitav2.grid(column=0, row=0, padx=5, pady=5, sticky=(E,N,W))
           
            sisendvaartus = ttk.Entry(tahvel3)
            #jou.set(sisendvaartus)
            sisendvaartus.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
            raam3.bind("<Return>", lambda event: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            raam3.focus_set()
            nupp1 = ttk.Button(tahvel3, text="Kontrolli!", command=lambda: kontrolli(sisendvaartus,küsitav,vastus,raam3,j,n))
            nupp1.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
       
def proov(j, küsibfailinime, esteng1,n):
   
    raam2 = Tk()
    raam2.resizable(width=FALSE, height=FALSE)
    raam2.title("TEST")
    #raam2.geometry("400x100")
   
    tahvel2 = Canvas(raam2,  background="grey")
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
    raam2.bind("<Return>", lambda event:tõlk(n,küsitav,vastus, raam2,j))
    nupp2 = ttk.Button(tahvel2, text="START", command=lambda: tõlk(n,küsitav,vastus, raam2,j))
    nupp2.grid(column=1, row=1, padx=80, pady=40, sticky=(N, S, W, E))
 
   
    #.pack()
    if len(küsitav) == 0:
        global raam7
        raam7=Tk()
        raam7.resizable(width=FALSE, height=FALSE)
        raam7.title("Viga!")
        tahvel7 = Canvas(raam7, background="beige")
 
        tahvel7.place(anchor=CENTER)
        tahvel7.grid()
       # messagebox.showinfo(title="Viga",message="Oled jätnud sõnade faili tühjaks, lisa sõnad!")
        veateade = ttk.Label(tahvel7, text="Oled jätnud sõnade faili tühjaks, lisa sõnad!",background="beige")
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
    raam.resizable(width=FALSE, height=FALSE)
    raam.title("Tõlkeprogramm")
 
     #   pilt = PhotoImage(file="proov3.gif")
    #bg_img = PhotoImage(file='proov3.gif')
    #bg_lbl = Label(raam, image=bg_img)
    #bg_lbl.grid(column=0,row=0, padx=0, pady=0, sticky=(N,S,W,E))
    tahvel = Canvas(raam, background="grey")
    #tahvel.place(anchor=CENTER)
   
    tahvel.grid(column=0, row=2, padx=5, pady=5, sticky=(N, E, W))
   
    #pilt=PhotoImage(file="proov3.gif")
    #tahvel=Label(raam,image=pilt)
    #tahvel.place(x=0,y=0)
    kuidasSisestada = ttk.Label(tahvel, text="Sisesta sõnad faili vastavalt: cat-kass dog-koer",background="white")
    kuidasSisestada.grid(column=0, row=0, padx=5, pady=5)
    #background_image=PhotoImage(file="taust.jpg")
    #background=Label(raam,image=background_image, bd=0)
    #background.pack()
    failinimi2 = ttk.Label(tahvel, text="Sisesta faili nimi, mis on samas kaustas käesoleva programmiga (NT:('sonad.txt')):",background="darkgrey")
    failinimi2.grid(column=0, row=1, padx=5, pady=5, sticky=(N, E, W))
 
    esteng = ttk.Label(tahvel, text="Kui soovid, et programm küsiks inglise keeles, sisesta: ING-EST ja vastupidi: EST-ING:",background="darkgrey")
    esteng.grid(column=0, row=2, padx=5, pady=5, sticky=(N, E, W))
 
#lahtrid
    küsibfailinime = ttk.Entry(tahvel)
    küsibfailinime.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))
 
    esteng1 = ttk.Entry(tahvel)
    esteng1.grid(column=1, row=2, padx=5, pady=5, sticky=(N, W, E))
   
#Teen nupu ning annan commandi talle selle, mis ta teeb kui vajutatakse nuppu, ehk siis funktsiooni
    raam.bind("<Return>", lambda event:proov(j,küsibfailinime,esteng1,n))
    nupp = ttk.Button(tahvel, text="Hakkame pihta!", command=lambda:proov(j,küsibfailinime,esteng1,n))
    nupp.grid(column=1, row=3, padx=5, pady=5, sticky=(N, S, W, E))
 
 
 
    #nupp.columnconfigure(1, weight=1)
    #nupp.rowconfigure(3, weight=1)
    #nupp.mainloop()
 
   
#Aken tuleb ekraanile
#raam.mainloop()
 
algus(j,0)
