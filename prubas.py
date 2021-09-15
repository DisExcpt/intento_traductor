# ----------------------------------      posible forma 1
f = open("prueba.asm", "r")
l = []
for line in f:
    l.append(line.split())
# print(l)
aux = l[0][1]
print(aux[1:])
f.close()


# -----------------------------------         posible forma 2
# with open("prueba.asm", "r") as archivo:
#     a = archivo.readlines()
#     l = []
#     for lineas in a:
#         l.append(lineas.split())
#     print(l)
