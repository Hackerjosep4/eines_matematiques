# Immports




from math import gcd
from math import factorial
from functools import reduce
from sympy import divisors



# Funcions


def factoritzar_polinomi(polinomi):
    factors = []
    if son_integuers(polinomi):
        polinomi = convertir_a_int(polinomi)
        faccom = factor_comu(polinomi)
    else:
        faccom = 1
    if faccom != 1:
        factors.append([faccom])
        for i in range(0, len(polinomi)):
            polinomi[i] = polinomi[i] / faccom
    
    polinomi = convertir_a_int_condicional(polinomi)

    if polinomi[-1] == 0:
        factors.append([1, 0])
        polinomi_nou = []
        for i in range(0, len(polinomi)-1):
            polinomi_nou.append(polinomi[i])
        
        factors_nou = factoritzar_polinomi(polinomi_nou)
        for fac in factors_nou:
            factors.append(fac)
        
    elif len(polinomi) == 3:
        factors_nou = factoritzar_2_grau(polinomi)
        for fac in factors_nou:
            factors.append(fac)
        
    elif len(polinomi) > 3:

        
        divisor_exacto = divisivilitat(polinomi)
        if divisor_exacto == 0:
            factors.append(polinomi)
        else:
            factors.append([1, divisor_exacto])
            polinomi_nou, _ = rufini(polinomi, divisor_exacto)
            
            factors_nou = factoritzar_polinomi(polinomi_nou)
            for fac in factors_nou:
                factors.append(fac)
        
    elif len(polinomi) == 2:
        if polinomi[0] == 1:
            factors.append([1, polinomi[1]])
        else:
            factors.append([polinomi[0]])
            factors.append([1, polinomi[1]/polinomi[0]])
        

    return factors



def factor_comu(polinomi):
    faccom = reduce(gcd, polinomi)
    return faccom



def factoritzar_2_grau(polinomi):
    factors = []
    
    a = polinomi[0]
    b = polinomi[1]
    c = polinomi[2]

    delta = ((pow(b, 2)) - (4 * a * c))

    if delta < 0:
        factors = [polinomi]
    else:
        if polinomi[0] != 1:
            factors.append([polinomi[0]])

        sol1 = ((-1 * b) + (pow(delta, (1 / 2)))) / (2 * a)
        sol2 = ((-1 * b) - (pow(delta, (1 / 2)))) / (2 * a)

        factors.append([1, sol1 * -1])
        factors.append([1, sol2 * -1])

    return factors



def son_integuers(polinomi):
    for coef in polinomi:
        if coef % 1 != 0:
            return False
    return True



def convertir_a_int(polinomi):
    polinomi_int = []
    for coef in polinomi:
        polinomi_int.append(int(coef))
    return polinomi_int



def convertir_a_int_condicional(polinomi):
    polinomi_int = []
    for coef in polinomi:
        if coef % 1 == 0:
            polinomi_int.append(int(coef))
        else:
            polinomi_int.append(coef)
    return polinomi_int



def rufini(polinomi, a):
    a = a * (-1)
    polinomi_nou = []

    res_anterior = 0
    for i in range(0, len(polinomi)):
        res =  polinomi[i] + (res_anterior*a)
        polinomi_nou.append(res)
        res_anterior = res

    polinomi_nou.pop()

    return [polinomi_nou, res_anterior]



def residu(polinomi, a):
    a = a * -1
    residu = 0
    grau = len(polinomi)-1

    for i in range(0, grau+1):
        residu += polinomi[i] * (pow(a, (grau-i)))

    return residu



def divisivilitat(polinomi):
    divisores = []
    for divisor in divisors(polinomi[-1]):
        divisores.append(divisor)
        divisores.append(divisor * -1)
    
    divisor_exacto = 0
    for div in divisores:
        if residu(polinomi, div) == 0:
            divisor_exacto = div
            break
    return divisor_exacto



def sumar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    if len(polinomi_a) > len(polinomi_b):
        grau_superior = len(polinomi_a)-1
    else:
        grau_superior = len(polinomi_b)-1
    
    for i in range(0, grau_superior - (len(polinomi_a)-1)):
        polinomi_a.append(0)
    for i in range(0, grau_superior - (len(polinomi_b)-1)):
        polinomi_b.append(0)
    
    for i in range(0, grau_superior+1):
        polinomi_resultat.append(polinomi_a[i] + polinomi_b[i])
    
    return polinomi_resultat



def restar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    if len(polinomi_a) > len(polinomi_b):
        grau_superior = len(polinomi_a)-1
    else:
        grau_superior = len(polinomi_b)-1
    
    for i in range(0, grau_superior - (len(polinomi_a)-1)):
        polinomi_a.append(0)
    for i in range(0, grau_superior - (len(polinomi_b)-1)):
        polinomi_b.append(0)
    
    for i in range(0, grau_superior+1):
        polinomi_resultat.append(polinomi_a[i] - polinomi_b[i])
    
    return polinomi_resultat



def multiplicar_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    grau_a = len(polinomi_a)-1
    grau_b = len(polinomi_b)-1
    grau = len(polinomi_a) + len(polinomi_b) - 2

    for i in range(0, grau+1):
        polinomi_resultat.append(0)
    
    for i in range(0, grau_a+1):
        for j in range(0, grau_b+1):
            polinomi_resultat[grau - (grau_a - i) - (grau_b - j)] += polinomi_a[i] * polinomi_b[j]
    
    return polinomi_resultat



def dividir_polinomis(polinomi_a, polinomi_b):
    polinomi_resultat = []
    grau_resultat = len(polinomi_a) - len(polinomi_b)

    if grau_resultat < 0:
        raise Exception("El polinomi primer polinomi ha de ser de grau superior o igual al segon")

    for i in range(0, grau_resultat+1):
        polinomi_resultat.append(0)
    
    i = 0
    while i < len(polinomi_a) and len(polinomi_a)-1-i >= len(polinomi_b)-1:
        coef_a = polinomi_a[i]
        grau_a = len(polinomi_a) - 1 - i
        coef_b = polinomi_b[0]
        grau_b = len(polinomi_b) - 1

        polinomi_resultat[grau_resultat - (grau_a - grau_b)] = coef_a / coef_b

        for j in range(0, grau_b+1):
            polinomi_a[i+j] -= (coef_a / coef_b) * polinomi_b[j]
    
    return [polinomi_resultat, polinomi_a]



def punt_triangle_pascal(n, p):
    if p == 0 or p == n:
        return 1
    elif p == 1 or p == n-1:
        return n
    else:
        punt = factorial(n) / (factorial(p) * factorial(n-p))
        return punt



def binomi_de_newton(grau):
    coefs = []

    for i in range(0, grau+1):
        coefs.append(punt_triangle_pascal(grau, i))
    
    return coefs




def print_factors(factors):

    output = f"La factorització es: "

    if len(factors) > 0:
        output += f"({return_output_polinomi(factors[0])})"

        for i in range(1, len(factors)):
            output += f" * ({return_output_polinomi(factors[i])})"
    

    print(output)
    print("")



def return_output_polinomi(polinomi):
    grau = len(polinomi)-1
    output = ""

    if grau > -1:
        for i in range(0, grau+1):
            fac = polinomi[i]
            grau_actual = grau - i
            if fac != 0:
                if fac < -1:
                    output += f" - {fac*-1}"
                elif fac == -1:
                    if grau_actual == 0:
                        output += f" - 1"
                    else:
                        output += f" - "
                elif fac == 1:
                    if grau_actual == 0:
                        output += f" + 1"
                    else:
                        output += f" + "
                elif fac > 1:
                    output += f" + {fac}"
                
                if grau_actual == 0:
                    output += ""
                elif grau_actual == 1:
                    output += f"x"
                elif grau_actual > 1:
                    output += f"x^{grau_actual}"
    
    return output[3:]



def print_polinomi(polinomi):
    output = f"El polinommi es: "

    output += return_output_polinomi(polinomi)
    
    print(output)
    print("")



def print_bin_new(coefs):
    output = f"El polinomi resultant es: "

    output += f"{coefs[0]}(a^{len(coefs)-1})(b^0)"

    for i in range(1, len(coefs)):
        output += f" + {coefs[i]}(a^{len(coefs)-1-i})(b^{i})"
    
    print(output)
    print("")



def print_solucions(solucions):
    output = f"Les posibles solucions son: "

    output += f"{solucions[0]}"

    for i in range(1, len(solucions)):
        output += f" / {solucions[i]}"
    
    print(output)
    print("")



def calc_solucions(factors):
    solucions = []

    for fac in factors:
        if len(fac) == 2:
            solucions.append((fac[1] * -1)/fac[0])

    return solucions



def demanar_polinomi():
    grau = int(input("Siusplau introdueix el grau del polinomi: "))
    polinomi = []
    for i in range(0, grau + 1):
        a = input(f"Introdueix el coeficient de grau {grau-i} : ").strip()
        polinomi.append(int(a))
    print("")
    
    return polinomi



def factoritzador():

    try:

        print("Hola, a continuacio factoritzarem polinomis")
        
        polinomi = demanar_polinomi()

        factors = factoritzar_polinomi(polinomi)

        for i in range(0, len(factors)):
            factors[i] = convertir_a_int_condicional(factors[i])

        print_factors(factors)
        print_solucions(convertir_a_int_condicional(calc_solucions(factors)))

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def teorema_del_residu():

    try:

        polinomi = demanar_polinomi()

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a) : ")) * -1

        resultat = residu(polinomi, a)

        print(f"El residu es: {resultat}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def trobar_divisor():

    try:

        polinomi = demanar_polinomi()

        resultat = divisivilitat(polinomi)

        print(f"El divisor exacte es: {resultat}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_rufini():

    try:

        polinomi = demanar_polinomi()

        a = int(input("Introdueix el terma \"a\" del binomi divisor (x - a) : ")) * -1

        resultat, residu = rufini(polinomi, a)

        resultat = convertir_a_int_condicional(resultat)

        print_polinomi(resultat)
        print(f"El residu es: {residu}")
        print("")

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def fer_suma():

    try:

        print("Introdueix el polinomi que vols sumar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols sumar")
        polinomi_b = demanar_polinomi()

        resultat = sumar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

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

        print("Introdueix el polinomi que vols restar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols restar")
        polinomi_b = demanar_polinomi()

        resultat = restar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

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

        print("Introdueix el polinomi que vols multiplicar")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols multiplicar")
        polinomi_b = demanar_polinomi()

        resultat = multiplicar_polinomis(polinomi_a, polinomi_b)

        print_polinomi(resultat)

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

        print("Introdueix el polinomi que vols dividir")
        polinomi_a = demanar_polinomi()
        print("Introdueix el polinomi pel qual vols dividir")
        polinomi_b = demanar_polinomi()

        resultat, resta = dividir_polinomis(polinomi_a, polinomi_b)

        print("El cuocient es: ")
        print_polinomi(resultat)
        print("El residu es: ")
        print_polinomi(resta)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre racional.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def  fer_binomi_de_newton():

    try:

        grau = int(input("Introdueix el grau n del binomi ( (a+b)^n ) : "))

        resultat = binomi_de_newton(grau)

        print_bin_new(resultat)

    except ValueError:
        print("")
        print("S'ha produit un error inesperat: Entrada inválida. Has de ingresar un nombre natural.")
        print("")

    except Exception as e:
        print("")
        print(f"S'ha produit un error inesperat: {e}")
        print("")



def  fer_punt_triangle_pascal():

    try:

        n = int(input("Introdueix la fila n del triangle: "))
        p = int(input("Introdueix la columna p del triangle: "))

        resultat = punt_triangle_pascal(n, p)

        print(f"Aquest punt del triangle de Pascal es: {resultat}")
        print("")

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
    Operacions basiques:
        Sum - Sumar polinomis
        Res - Restar polinomis
        Mul - Multiplicar polinomis
        Div - Dividir polinomis
    Factorització:
        Fac - Factoritzar polinomi
        Teo - Teorema del residu
        Exa - Trobar divisor exacte
        Ruf - Rufini
    Binomi de Newton:
        Bin - Binomi de Newton
        Pas - Punt triangle de Pascal
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
    elif entrada == "fac":
        factoritzador()
        opcio_valida = True
    elif entrada == "teo":
        teorema_del_residu()
        opcio_valida = True
    elif entrada == "exa":
        trobar_divisor()
        opcio_valida = True
    elif entrada == "ruf":
        fer_rufini()
        opcio_valida = True
    elif entrada == "bin":
        fer_binomi_de_newton()
        opcio_valida = True
    elif entrada == "pas":
        fer_punt_triangle_pascal()
        opcio_valida = True
    
    if opcio_valida:
        input("Prem enter per continuar")
    print("")

input("Prem enter per sortir")
exit()