# Importem les llibreries necessàries



from sympy import factorial






def combinacions(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))



def permutations(n, k):
    return factorial(n) / factorial(n-k)



def fer_combinacions():
    try:
    
        n = int(input("Introdueix el valor de n (n k): "))
        k = int(input("Introdueix el valor de k (n k): "))
        print(f"El resultat de C({n}, {k}) és {combinacions(n, k)}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre natural.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_permutacions():
    try:
    
        n = int(input("Introdueix el valor de n (n k): "))
        k = int(input("Introdueix el valor de k (n k): "))
        print(f"El resultat de P({n}, {k}) és {permutations(n, k)}")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre natural.")
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
    Com - Combinacions
    Per - Permutacions
    S - Sortir
Opció: ''').strip().lower()
    print("")

    opcio_valida = False
    if entrada == "com":
        fer_combinacions()
        opcio_valida = True
    elif entrada == "per":
        fer_permutacions()
        opcio_valida = True
    
    if opcio_valida:
        input("Prem enter per continuar")
    print("")

input("Prem enter per sortir")
exit()