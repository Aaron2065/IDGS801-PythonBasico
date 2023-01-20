nombres = ["Juan", "Mario" , "Raul"]
numeros = [1,2,3,4,5]
datos = [1,2.5, "Mario", True]
nombres[0] = "Rberto"
print(nombres[:])
print(nombres[2])
print(nombres[1])
print(nombres[0])
nombres.append("Dario")
print(nombres)
nombres.insert(2, "Laura")
print(nombres)
nombres.extend(["Chencha", 2,23,5])
print(nombres)
nombres.remove("Chencha")
print(nombres)
nombres.pop()
print(nombres)

n = ["Juan"]
n2 = n * 5
print(n2)

del nombres[0]
print(nombres)