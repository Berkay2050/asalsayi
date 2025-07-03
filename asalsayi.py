Sayi = int(input("Bir sayı giriniz: "))

prime = True
for a in range(2, Sayi):
  if Sayi %a == 0:
    prime = False
    break

if prime == True:
   print(f"{Sayi} sayisi asal")
else:
   print(f"{Sayi} sayisi asal değildir")
