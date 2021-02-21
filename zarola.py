import json
import random
def kul_girisi():
    print("Lütfen 5'e tam bölünebilen bir tam sayı giriniz.")
    while 1:
        try:
            us=int(input("Şifre için atılacak zar sayısını giriniz :"))
        except ValueError:
            print("Lütfen bir sayı giriniz.")
        if us%5==0:
            return us
        else:
            print("Lütfen 5'e tam bölünebilen bir sayi giriniz.")
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
    with open("zarola.json") as f:
        data=json.load(f)
    print("\n\n\n")
    for i in range(0,len(x)):
        for j in data:
            if x[i]==str(j["numara"]):
                print(j["kelime"],end=" ")
                break

x=sifre_cevir(zar_at(kul_girisi()))