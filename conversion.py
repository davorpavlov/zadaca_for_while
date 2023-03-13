def km_to_miles(km):
    return round(km * 0.6214, 2)

def miles_to_km(miles):
    return round(miles / 0.6214, 2)

def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

def kg_to_pounds(kg):
    return round(kg * 2.2046, 2)

def pounds_to_kg(pounds):
    return round(pounds / 2.2046, 2)

def liter_to_gallon(liter):
    return round(liter * 0.2642, 2)

def gallon_to_liter(gallon):
    return round(gallon / 0.2642, 2)

def kw_to_hp(kw):
    return round(kw * 1.3596, 2)

def hp_to_kw(hp):
    return round(hp / 1.3596, 2)

while True:
    print("Odaberite vrstu pretvorbe:")
    print("1. km u milje")
    print("2. milje u km")
    print("3. Celzijus u Fahrenheit")
    print("4. Fahrenheit u Celzijus")
    print("5. kg u funte")
    print("6. funte u kg")
    print("7. litra u galon")
    print("8. galon u litru")
    print("9. kW u ks")
    print("10. ks u kW")

    choice = input("Odabir: ")

    if choice == '1':
        km = float(input("Unesite broj kilometara: "))
        print(km, "km =", km_to_miles(km), "milja")
    elif choice == '2':
        miles = float(input("Unesite broj milja: "))
        print(miles, "milja =", miles_to_km(miles), "km")
    elif choice == '3':
        celsius = float(input("Unesite temperaturu u Celzijusima: "))
        print(celsius, "°C =", celsius_to_fahrenheit(celsius), "°F")
    elif choice == '4':
        fahrenheit = float(input("Unesite temperaturu u Fahrenheitima: "))
        print(fahrenheit, "°F =", fahrenheit_to_celsius(fahrenheit), "°C")
    elif choice == '5':
        kg = float(input("Unesite broj kilograma: "))
        print(kg, "kg =", kg_to_pounds(kg), "funti")
    elif choice == '6':
        pounds = float(input("Unesite broj funti: "))
        print(pounds, "funti =", pounds_to_kg(pounds), "kg")
    elif choice == '7':
        liter = float(input("Unesite broj litara: "))
        print(liter, "litara =", liter_to_gallon(liter), "galona")
    elif choice == '8':
        gallon = float(input("Unesite broj galona: "))
        print(gallon, "galona =", gallon_to_liter(gallon), "litara")
    elif choice == '9':
        kw = float(input("Unesite snagu u kW: "))
        print(kw, "kW =", kw_to_hp(kw), "ks")
    elif choice == '10':
        hp = float(input("Unesite snagu u konjskim snagama (hp): "))
        print(hp, "ks =", hp_to_kw(hp), "kW")
    else:
        print("Nevažeći odabir")
    nastavak = input("Želite li nastaviti s korištenjem programa? (da/ne): ")
    if nastavak.lower() != "da":
        break
