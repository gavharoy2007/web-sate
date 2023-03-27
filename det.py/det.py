# 1 
# son = float(input("Son kiriting: "))
# if son < 0:
#     print("manfiy")
# elif son > 0:
#     print("musbat")
# else:
#     print("son 0 ga teng")

# 2 
# car = {
#     "nomi" : "nexia",
#     "year" : "2020"
# }
# if car.keys():
#     print(True)
# else:
#     print(False)

# 3
# son = [1, 2, 3, 4]
# if 4 in son:
#     print(True)
# else:
#     print(False)

# 4
# meva = ['olma', 'nok', 'anor']
# for i in meva:
#     print(i, end="/")
# else:
#     print("\nPython is good")

# 5

# son = int(input("Son kiriting: "))
# for i in range(son, -100, -1):
 
#    print(i, end=" ")

# 6
# for i in range(100):
#     if i == 3 or i ==13 or i==25 or i ==75:
#         continue
#     print(i, end=" ")

# 7
# son = int(input(":"))
# son = str(son)
# if len(son) == 4:
#     print("4 honali son")
# else:
#     print("unaqa emas")
# print(len(son))

# 8
# son = [100, 20, 0, 90, 1]
# son.sort()
# print(son)

# 9
# a = {1, 2, 3, 4}
# b ={1, 2,5, 6, 7}
# a.intersection_update(b)
# print(a)

# 10
# a = int(input("A "))
# b = int(input("B "))
# d = a + b

# if a >= 0 and b >= 0 and d >= 100:
#     print(a / b)
# elif a >= 0 and b >= 0 and d < 100:
#     print(a * b)
# else:
#     print("a yoki b manfiy son")


a = "dollar"
b = "so`m"

print("bankamatimizga xush kelibsiz")
print("dollarni tanlash uchun a ni bosing")
print("so`mni tanlash uchun b ni bosing")
tanlov = input(">>>  ").strip()
if tanlov == "a":
    x = int(input("dollar miqdorini kiriting"))
    print(x * 10000,"som")
    print("tashrifingiz uchun rahmat")
elif tanlov == "b":
    x = int(input("so`m miqdorini kiriting"))
    print(x / 10000,"dollars")
    print("tashrifingiz uchun rahmat")
else:
    print("tanlovda adashdingiz")
    print("qaytadan urinib ko`ring")


