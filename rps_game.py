import random

while True:
    print('Dobro došli u igru kamen-škare-papir!')
    print('Odaberite vaš izbor: ')

    options = ['kamen', 'škare', 'papir']
    player_move = input('Kamen, škare ili papir? ')
    computer_move = random.choice(options)
    
    if player_move not in options:
        print('Unijeli ste pogrešan izbor. Pokušajte ponovno.')
        continue
    
    print('Računalo je odabralo:', computer_move)
    
    if player_move == computer_move:
        print('Rezultat je neriješen!')
    elif player_move == 'kamen':
        if computer_move == 'škare':
            print('Pobjedili ste! Kamen tuče škare!')
        else:
            print('Izgubili ste! Papir prekriva kamen!')
    elif player_move == 'škare':
        if computer_move == 'papir':
            print('Pobjedili ste! Škare režu papir!')
        else:
            print('Izgubili ste! Kamen tuče škare!')
    elif player_move == 'papir':
        if computer_move == 'kamen':
            print('Pobjedili ste! Papir prekriva kamen!')
        else:
            print('Izgubili ste! Škare režu papir!')
    play_again = input("Želite li ponovno igrati? (da/ne) ")
    if play_again.lower() != "da":
        break
