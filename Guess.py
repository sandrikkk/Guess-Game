import random
from Art import logo

martivi_level = 10
rtuli_level = 5

def gansazgvra(sicocxle,pasuxi,shetanili_cifri):
    if(shetanili_cifri > pasuxi):
        print("შემოტანილი ციფრი პასუხზე დაბალია")
        return sicocxle-1
    elif(shetanili_cifri < pasuxi):
        print("შემოტანილი ციფრი პასუხზე დაბალია")
        return sicocxle-1
    else:
        print("გილოცავთ, თქვენ სწორად გამოიცანით ციფრი !")
def done():
    sicocxle = input("აირჩიეთ დონე ლათინური ასოებით : 'martivi' ან 'rtuli':")
    if(sicocxle == 'martivi'):
        return martivi_level
    else:
        return rtuli_level

def mtavari_panel():
    print(logo)
    print("მოგესამებით შემთხვევითი ციფრის გამოცნობის თამასში !")
    print("აირჩიეთ ციფრები 1 დან 100 - ის ინტერვალში !")
    pasuxi = random.randint(1,100)
    print("თამაშის პასუხია ! :", pasuxi)
    sicocxle = done()
    shetanili_cifri = 0
    while shetanili_cifri != pasuxi:
        print("თქვენ გაქვთ ", sicocxle, " სიცოცხლე")
        shetanili_cifri = int(input("შემოიტანეთ ციფრი ! :"))
        sicocxle = gansazgvra(sicocxle,pasuxi,shetanili_cifri)
        if sicocxle == 0:
            print("თქვენი აღარ გაქვთ სიცოცხლე !")
            return
        elif shetanili_cifri != pasuxi:
            print("გულს ნუ გაიტეხ თავიდან სცადე ! ")
mtavari_panel()