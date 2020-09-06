# Presentación del menú con los tipos de cafe
tipo=1
while tipo!="3":
  print("Bienvenido a CafeUV.\nSelecciona el tipo de cafe\n\t1- Americano\n\t2- Capuccino\n 3.- Salir\n")
  tipo = input ("Introduce el ingrediente extra correspondiente al tipo de cafe:")
  # Decisión sobre el tipo de cafe
  if tipo == "1":
      print("Selecciona \n\t 1- Crema chantilly \n\t2- Canela\n\t 3- Ninguno de los anteriores")
      ingrediente = input("Introduce el ingrediente que deseas: ")
      print("Cafe Americano ", end="")
      if ingrediente == "1":
          print ("Crema chantilly")
      if ingrediente == "2":
        print ("Canela")    
      else: 
          print ("ninguno de los anteriores")
  if tipo=="2":
      print("Ingredientes de Cafe Capucciono\n\t1- Leche Deslactosada\n\t2- Entera \n\t3 Light \n")
      ingrediente = input("Introduce el ingrediente que deseas: ")
      print("Cafe Americano ", end="")
      if ingrediente == "1":
          print("Leche Deslactosada\n\n")
      elif ingrediente == "2":
          print("Leche Entera\n\n")
      else:
          print("Leche Light\n\n")
print("Gracias por su compra")