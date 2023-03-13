def multiplication_table(last_number):
    for a in range(1, last_number + 1):
        for b in range(1, last_number + 1):
            print(f"{a} x {b} = {a*b}")
        print() 

while True:
    last_number = input("Unesite zadnji broj u tablici množenja: ")
    if last_number.isdigit():
        last_number = int(last_number)
        multiplication_table(last_number)
        answer = input("Želite li nastaviti koristiti program? (da/ne) ")
        if answer.lower() != "da":
            print("Hvala što ste koristili program!")
            break
    else:
        print("Unesite cijeli broj.")
