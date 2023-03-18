'''
racunalo bira izmedju kamena, skara i papira i pohranimo u neku varijablu
pitamo korisnika da on odabere kamen, škare ili papir i pohranimo u neku varijablu

usporedimo izbore i ovisno o izboru prikazemo rezultat
'''
import random

# pieces = ['kamen', 'škare', 'papir']
computer_choice = random.randint(1, 3)
print(computer_choice)
user_choice = int(input('Izaberite Kamen, škare ili papir(1, 2 ili 3): '))

if user_choice == computer_choice:
    print("Izjednačeno!")
elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
    print("Pobijedili ste!")
else:
    print("Računalo je pobijedilo!")
    

try:
    user_choice = int(input('Izaberite Kamen, škare ili papir(1, 2 ili 3): '))
except ValueError:
    print('Unesite jedan od brojeva (1, 2 ili 3)')
    user_choice = int(input('Izaberite Kamen, škare ili papir(1, 2 ili 3): '))