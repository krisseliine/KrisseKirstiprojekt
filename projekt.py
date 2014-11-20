print("Sisesta sõnad faili vastavalt:"+"\n"+"cat-kass"+"\n"+ "dog-koer,kutsu"+"\n"+
      "vajuta ENTER, kui tehtud"+"\n")

try:
    failinimi=input("Sisesta faili nimi, mis on samas kaustas käesoleva programmiga (NT:('sõnad.txt')):")
except:
    print("Failinimega tekkis probleeme, proovi uuesti")
    

#edaspidi on nupud tkInteris

mispidi=input("Kui soovid, et programm küsiks inglise keeles, sisesta: ING-EST ja vastupidi: EST-ING")
