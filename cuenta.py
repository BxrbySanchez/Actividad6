class Cuenta:
    pass    
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def mostrar(self):
        print("TITULAR: ", self.titular)
        print("\nCANTIDAD: ", self.cantidad)
    def ingresar(self,cantidad):       
        if cantidad<0:
            print("")
        else:
            self.cantidad += cantidad
            print("\nINGRESÓ EN LA CUENTA: ", cantidad, "EN TOTAL HAY $",self.cantidad, "EN LA CUENTA")    
    def retirar(self,cantidad):
        self.cantidad -= cantidad
        print("\nSE RETIRARON $",cantidad, "EL SALDO TOTAL ES $", self.cantidad)
cuenta1 = Cuenta("JOSÉ PEREZ", 10800)
print(cuenta1.mostrar())
cuenta1.ingresar(-500)
print(cuenta1.ingresar)
cuenta1.ingresar(10000)
print(cuenta1.ingresar)
cuenta1.retirar(15000)
print(cuenta1.retirar)