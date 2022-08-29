texto = input("ingrese el texto: ")

# metodo de cortar x::y, x es donde se corta el incio y yel ultimo, en este caso esta -1 ordenando desde el ultimo digito
def reversa_texto(text):
    return text[::-1]

print(reversa_texto(texto))