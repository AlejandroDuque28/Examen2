arreglo = []
cantidadElementos = int(input("Digite La Cantidad De Elementos Del Arreglo: "))

for i in range(cantidadElementos):
    arreglo.append(int(input("Escriba Su Digito: ")))

print("Su Lista Es: ",arreglo)
arreglo.reverse()
print("Su Lista Invertida Es: ",arreglo)

