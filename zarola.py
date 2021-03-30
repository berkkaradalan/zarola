import json
import random
def kul_girisi():
    print(''' _____               _       
|__  /__ _ _ __ ___ | | __ _ 
  / // _` | '__/ _ \| |/ _` |
 / /| (_| | | | (_) | | (_| |
/____\__,_|_|  \___/|_|\__,_|
                             
''')
    while 1:
        try:
            sayi=int(input("Şifre için atılacak zar sayısını giriniz :"))
            break
        except ValueError:
            print("Lütfen sadece sayı kullanınız.")
        except UnboundLocalError:
            print("Lütfen sadece sayı kullanınız.")
        else:
            sayi=int(input("Şifre için atılacak zar sayısını giriniz: "))
            break
    return sayi*5
def zar_at(x):
    ls=[]
    st=""
    for i in range(0,x):
        st+=str(random.randint(1,6))
        if int(len(st))==5:
            ls.append(st)
            st=""
    return ls
def sifre_cevir(x):
    with open('zarola.json') as f:
        data=json.load(f)
    print("\nŞifreniz : ",end="")
    for i in range(0,len(x)):
        for j in data:
            if x[i]==str(j["numara"]):
                print(j["kelime"],end=" ")
                break
    print("\n")

x=sifre_cevir(zar_at(kul_girisi()))
