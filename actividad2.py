opc = 0
while opc < 5:
    opc = int(input("Escoge una opcion\n1. suma\n2. resta\n3. multiplicacion\n4. division\n5. salir\n"))
    if(opc == 1):
        num1 = int(input('Escoge el primer numero: '))
        num2 = int(input('Escoge el segundo numero: '))
        print(" El resultado de la suma {} + {} = {}".format(num1,num2,(num1+num2)))
    if(opc == 2):
        num1 = int(input('Escoge el primer numero: '))
        num2 = int(input('Escoge el segundo numero: '))
        print(" El resultado de la resta {} - {} = {}".format(num1,num2,(num1-num2)))
    if(opc == 3):
        num1 = int(input('Escoge el primer numero: '))
        num2 = int(input('Escoge el segundo numero: '))
        print(" El resultado de la multiplicacion {} * {} = {}".format(num1,num2,(num1*num2)))
    if(opc == 4):
        num1 = int(input('Escoge el primer numero: '))
        num2 = int(input('Escoge el segundo numero: '))
        print(" El resultado de la division {} / {} = {}".format(num1,num2,(num1/num2)))
    