from ast import If
num = input("Ingrese una hora: ")
lista = list(num)

hora = lista[0]
hora1 = lista[1]
horaF = hora + hora1

if lista[8] == "P" and lista[9] == "M":
    if int(horaF) > 12 and int(horaF) < 25:
        if int(horaF) == 13:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,1)
        elif int(horaF) == 14:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,2)
        elif int(horaF) == 15:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,3)
        elif int(horaF) == 16:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,4)
        elif int(horaF) == 17:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,5)
        elif int(horaF) == 18:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,6)
        elif int(horaF) == 19:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,7)
        elif int(horaF) == 20:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,8)
        elif int(horaF) == 21:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,9)
        elif int(horaF) == 22:
            lista.pop(0)
            lista.insert(0,1)
            lista.pop(1)
            lista.insert(1,0)
        elif int(horaF) == 23:
            lista.pop(0)
            lista.insert(0,1)
            lista.pop(1)
            lista.insert(1,1)
        elif int(horaF) == 24:
            lista.pop(0)
            lista.insert(0,0)
            lista.pop(1)
            lista.insert(1,0)
        
        print(''.join(map(str, lista)))
    else:
        print("número mayor en PM")

elif lista[8] == "A" and lista[9] == "M":
    if int(horaF) > 00 and int(horaF) < 13:
        print(''.join(map(str, lista)))
    else:
        print("no coincide la hora con AM")
