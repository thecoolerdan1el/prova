f = open("ARQUIVO PROVA.txt", "r")
print(f.readline())
set_1 = f.readline()
print(set_1)
set_2 = f.readline()
print(set_2)
set_1 = set_1.replace('\n', '').replace("'","")
set_2 = set_2.replace('\n', '').replace("'","")


set_3 = []
set_3.append(set_1)
set_4 = []
set_4.append(set_2)

v1 = set()
v2 = set()

for nums in set_3:
    v1.add(nums)

for num1 in set_4:
    v2.add(num1)


uniao = print(v1.union(v2))

print(f.readline())
set_5 = f.readline()
set_6 = f.readline()
print(set_5)
print(set_6)
set_5 = set_5.replace('\n', '').replace(",","")
set_6 = set_6.replace('\n', '').replace(",","")

set_7 = []
set_7.append(set_5)
set_8 = []
set_8.append(set_6)
v3 = set()
v4 = set()

for num2 in set_5:
    v3.add(num2)

for num3 in set_6:
    v4.add(num3)

inter = print(v3.intersection(v4))

print(f.readline())
set_9 = f.readline()
set_10 = f.readline()
print(set_9)
print(set_10)
set_9 = set_9.replace('\n', '')
set_10 = set_10.replace('\n', '')

set_11 = []
set_11.append(set_9)
set_12 = []
set_12.append(set_10)
v5 = set()
v6 = set()

for num4 in set_9:
    v5.add(num4)

for num5 in set_10:
    v6.add(num5)

dif = print(v5.difference(v6))

print(f.readline())
set_15 = f.readline()
set_16 = f.readline()
print(set_15)
print(set_16)
set_15 = set_15.replace('\n', '')
set_16 = set_16.replace('\n', '')

set_20 = []
set_20.append(set_15)
set_21 = []
set_21.append(set_16)
v10 = set()
v11 = set()

for num10 in set_15:
    v10.add(num10)

for num11 in set_16:
    v11.add(num11)

#produto cartesiano 
print(len(set_21))

set_cart1 = set()
set_cart2 = set()

listaCart = set_20.split(',')
listaCart2 = set_21.split(',')

for item in listaCart:
    set_cart1.add(item)
    print(listaCart)

for item2 in listaCart2:
    set_cart2.add(item2)
    print(listaCart2)

print

for i in len(set_21):
    for j in len(set_20):
        x = set_20[j]
        y = set_21[i]
        if (x*2 - 3 == y):
            print(f"O plano cartesiano é: ({x},{y})")
print("finalizado")
        

