Senahesap={
    'ad':'Sena Narin',
    'hesapNo':'123456780',
    'bakiye':3000,
    'ekhesap':2000
}

Ahmethesap={
    'ad':'Ahmet Kaya',
    'hesapNo':'103456789',
    'bakiye':2000,
    'ekhesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye']>=miktar:
        hesap['bakiye'] -=  miktar
        print('Paranızı çekebilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        print('Hesabınızdaki bakiye yetersiz')
        toplam=hesap['bakiye']+hesap['ekhesap']
        if toplam>=miktar:
            x = input('Ek hesap kullanılsın mı? (Evet/Hayır)')
            if x=='Evet':
                ekhesapkullanılacakmiktar = miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']-=ekhesapkullanılacakmiktar
                print('Paranızı ek hesabınızı kullanarak çekebilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
                print('Bakiyenizde yeterli miktar bulunursa paranızı çekebilirsiniz.İyi günler dileriz.')
        else:
            print('Üzgünüz bakiyeniz yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Ek hesap limitiniz ise {hesap['ekhesap']} TL dir.")


def paraYatır(hesap,para):
    z = input('Parnızı ek hesabınıza mı yoksa bakiye miktarınıza mı yatırmak istersiniz ? (Ek Hesap/Bakiye)')
    if z=='Ek Hesap':
        new_ekhesap = hesap['ekhesap']+para
        if 5000>=new_ekhesap:
            print('Paranızı yatırabilirsiniz.')
            print(f"{hesap['hesapNo']} nolu hesabınızda yeni ek hesap miktarınız {new_ekhesap} TL dir.")
        else:
            print('Ek hesap limitiniz 5000 TL dir.Lütfen limitinize uygun bir para miktarı yatırınız.')
    else:
        new_bakiye = hesap['bakiye']+para
        print(f"{hesap['hesapNo']} nolu hesabınızda yeni bakiye miktarınız {new_bakiye} TL dir.")

paraCek(Senahesap,3000)
print('********************************')
paraCek(Senahesap,2000)

#######################################################

paraYatır(Senahesap,5000)