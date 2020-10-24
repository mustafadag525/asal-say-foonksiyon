def asal_mı(sayı):
   if sayı==1:
    return False
   elif sayı==2:
       return True
   else:
       for i in range(2,sayı):
           if sayı%i==0:
               return False
       return True
while True:
    sayı=int(input("sayı gir:"))
    if asal_mı(sayı):
        print(sayı,"asal bir sayıdır.")

    else:
        print(sayı,"asal bir sayı değildir")
