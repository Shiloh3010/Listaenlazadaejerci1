print ("Bienvenido a la asignación de habitaciones del Hotel")
si_no= str(input (print ("Va a agregar un cliente nuevo? s/n")))
cent= ("s")
if si_no == "s" or si_no == "S":
   
    cedula= int(input (print ("Agrega el número de cédula: ")))
    name= str(input (print ("Agrega el nombre ")))
    hab= int(input(print ("Agregue el número de la habitación")))
    
    class clientes:
            def __init__(self,cedula, name, hab):
                self.data = cedula, name , hab #cliente 1
                self.siguiente = None
    class clientes: 
        def __init__(self):
            nodo_primero= clientes(cedula,name,hab)
            self.cabeza = nodo_primero

    cent= str(input(print ("Desea agregar a otro cliente? s/n")))
    if cent == "s":
         class clientes:
            def __init__(self):
                 nodo_segundo= clientes(cedula, name, hab)
                 self.siguiente= nodo_segundo
    


                 


        


