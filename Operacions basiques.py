def fer_suma():
    try:
    
        a = int(input("Introdueix el valor de a (a + b): "))
        b = int(input("Introdueix el valor de b (a + b): "))
        print(f"El resultat és {a+b}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_resta():
    try:
    
        a = int(input("Introdueix el valor de a (a + b): "))
        b = int(input("Introdueix el valor de b (a + b): "))
        print(f"El resultat és {a+b}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_multiplicacio():
    try:
    
        a = int(input("Introdueix el valor de a (a * b): "))
        b = int(input("Introdueix el valor de b (a * b): "))
        print(f"El resultat és {a*b}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_divisio():
    try:
    
        a = int(input("Introdueix el valor de a (a / b): "))
        b = int(input("Introdueix el valor de b (a / b): "))
        print(f"El resultat és {a/b}, el resultat sencer és {a//b} i el residu és {a%b}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_potencia():
    try:
    
        a = int(input("Introdueix el valor de a (a ^ b): "))
        b = int(input("Introdueix el valor de b (a ^ b): "))
        print(f"El resultat és {pow(a, b)}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_arrel():
    try:
    
        a = int(input("Introdueix el valor de a (m√(a^n)) (m es arrel quadrada, qubica, ...) : "))
        n = int(input("Introdueix el valor de n (m√(a^n)) (m es arrel quadrada, qubica, ...) : "))
        m = int(input("Introdueix el valor de m (m√(a^n)) (m es arrel quadrada, qubica, ...) : "))
        print(f"El resultat és {pow(a, m/n)}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")







# Codi d'interaccio amb l'usuari / Codi d'iniciació del programa

entrada = ""

while entrada != "s":
    entrada = input('''
Menu:
    Sum - Suma
    Res - Resta
    Mul - Multiplicació
    Div - Divisió
    Pot - Potència
    Rad - Radical/Arrel
    S - Sortir
Opció: ''').strip().lower()
    print("")

    opcio_valida = False
    if entrada == "sum":
        fer_suma()
        opcio_valida = True
    elif entrada == "res":
        fer_resta()
        opcio_valida = True
    elif entrada == "mul":
        fer_multiplicacio()
        opcio_valida = True
    elif entrada == "div":
        fer_divisio()
        opcio_valida = True
    elif entrada == "pot":
        fer_potencia()
        opcio_valida = True
    elif entrada == "rad":
        fer_arrel()
        opcio_valida = True
    
    if opcio_valida:
        input("Prem enter per continuar")
    print("")

input("Prem enter per sortir")
exit()