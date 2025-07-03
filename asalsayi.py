Sayi = int(input("Bir sayı giriniz: ")) #Kullacının sayıyı girebilmesi için olan yer

prime = True         # gireceğimiz sayının asal sayı olduğunu varsayıyoruz
for a in range(2, Sayi):     # Bu iki satırda kullanıcının girdiği sayıya kadar bütün sayıları kullanıcının sayısına bölüyoruz
  if Sayi %a == 0:           # (2, sayi) kısmında 2 den başlattım çünkü 1 den başlatsaydım her sayı 1 e bölünebildiği için olmazdı
    prime = False         # bu satırda eğer sayımız sayımıza kadar olan sayılardan birine bölünebiliyorsa bu sayının asal sayı olmadığını bildiriyoruz
    break                # eğer sayımız sayımıza kadar olan sayılardan birine bölünebiliyorsa if komudunun içine giriyor ve break komudu sayesinde bitiriyoruz

if prime == True:              #bu komutla bu sayı if komuduna takılmamış ve prime == True ise bize sayının asal olduğunu bildir diyoruz
   print(f"{Sayi} sayisi asal")
else:   
   print(f"{Sayi} sayisi asal değildir")   #burada ise eğer prime == True den farklı bir şey yani prime == False ise sayımızın bize asal olmadığını bildir diyoruz ve kodumuz bitiyor.
