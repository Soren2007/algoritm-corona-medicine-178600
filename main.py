# شکرستان 
n = int(input("")) #مبتلایان 
k = int(input("")) #فوتی‌ها

a = n - k # یهبود

# نمکستان 
p = int(input("")) #مبتلایان 
q = int(input("")) #فوتی‌ها

b = p - q # یهبود


if a > b:
    print("Shekarestan")
elif a < b:
    print("Namakestan")

else:
    print("Equal")