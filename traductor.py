mnenmonicos_sin = [
    "ABA", "END"
]


class traductor():
    # funcion para leer la
    def leer(self):
        with open("prueba.asm", "r") as archivo:
            a = archivo.readlines()
            l = []
            for lineas in a:
                l.append(lineas.split())
            print(l)
            Imne = l[0][0]
            startC = l[0][1]
            startC = int(startC[1:])
            print(startC, Imne)
            cont = 0
            while cont < len(l):
                mne = l[cont][0]
                if mne in mnenmonicos_sin:
                    None
                else:
                    num = l[cont][1]
                tam = len(num[1:])
                if tam > 2:
                    startC += 3
                else:
                    startC += 2
                cont += 1
                print(startC, mne)
