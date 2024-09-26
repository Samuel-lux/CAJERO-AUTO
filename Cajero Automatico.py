from tqdm import tqdm
import time
saldo = 1000
name = input("Ingrese su primer Nombre Por favor\n")
codigo = int(input("Bienvenido, ingrese su numero de tarjeta(ultimos 4 digitos)\n"))
cvv = int(input("Ingrese el codigo de tarjeta\n"))
carga = 100
print("NOMBRE ASOCIADA A LA TARJETA: " + name)
print("Numero de tarjeta que termina en ----" + str(codigo))

print(name + " Seleccione que desea realizar\n")
print("1.Retiro")
print("2.Depositar")
print("3.Ver Saldo")
seleccion = int(input())
if seleccion == 1:
    print("De acuerdo " + name  + " ¿Cuanto desea retirar? le recordamos que tiene un saldo de Q" + str(saldo) + ".00")
    retiro = int(input())
    operar = saldo - retiro
    print("ESTAMOS REALIZANDO LA SOLITUD")
    for i in tqdm(range(carga)):
        time.sleep(0.1)
    if retiro>saldo:
        print("NO PUEDE RETIRAR PORQUE TIENE SALDO INSUFICIENTE PARA RETIRAR ESA CANTIDAD DE Q" + str(retiro) + ".00")
    else:
        print("Su retiro a sido con exito, saldo acutal de Q" + str(operar) + ".00")
        print("Desea un recibo más detallado? 1)si / 2)no")
        recibo = int(input())
        if recibo == 1:
            print("Estamos detallando su recibo")
            for i in tqdm(range(carga)):
                time.sleep(0.1)
            
            print("Nombre: " + name)
            print("Saldo que tenia: Q" + str(saldo) + ".00")
            print("Monto a retirar: Q" + str(retiro) + ".00")
            print("Saldo que le queda: Q" + str(operar) + ".00" )
        else:
            print("Gracias por utilizar nuestro cajero  que pase un excelente día :D")
elif seleccion == 2:
    print("Ingrese el nombre del que va a recibir el deposito: \n")
    name2 = input()
    if name==name2:
        print("NO SE PUEDE DEPOSITAR ASI MISMO")
        
    cuenta_depo = int(input("Ingrese el número de cuenta de 5 digitos de la persona: "))
    print("ESTAMOS Validando la información")
    for i in tqdm(range(carga)):
        time.sleep(0.1)
    
    print("excelente, encontramos la cuenta de " + name2 + ", cuanto le desea depositar")
    depo = int(input())
    print("AGREGE ALGUNA DESCCRIPCIÓN PARA ESTE MONTO, SI NO QUIERE AGREGAR, DEJENLO EN BLANCO")
    monto = input()
    operar = saldo-depo
    print("DEPOSITANDO..")
    for i in tqdm(range(carga)):
        time.sleep(0.1)
    if depo>saldo:
        print("No podemos realizar el deposito porque no tiene saldo suficiente.")
    else:
        print("Su deposito de envio correctamente, ¿desea su factura detallada? 1) si / 2)no\n")
        desicir = int(input())
        if desicir == 1:
            print("Nombre de su cuenta : " + name)
            print("Nombre de la cuenta que recibie el dinero: " + name2)
            print("Saldo que tenia: Q" + str(saldo) + ".00" )
            print("Cantidad enviada Q" + str(depo) + ".00")
            print("Descripción: " + monto)
            print("Saldo Actual de su cuenta: Q" + str(operar) + ".00")
elif seleccion == 3:
    print("De acuerdo " + name )
    print("Saldo actual: Q" + str(saldo) + ".00")
else:
    print("Seleccione alguna de las opciones")
input("ENTER PARA SALIR")