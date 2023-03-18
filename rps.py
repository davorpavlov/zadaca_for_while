import random
import os


pieces = {
    1 : 'Kamen',
    2 : 'Skare',
    3 : 'Papir'
}

def menu() -> None:
    os.system('cls')
    print('*'*50)
    print()
    for key, value in pieces.items():
        print(f'{key}. {value}')
    print()
    print('*'*50)


def message(message: str, destination: str):
    match destination:
        case 'console':
            print(message)
        case 'txt_file':
            pass
        case 'db_sql':
            #save_to_db(message)
            pass
        case 'db_mongodb':
            pass


# Funkcija za unos
# Funkcija za provjeru str
# Funkcija za provjeru int
def user_input_validator(user_input: str) -> int:
    while not user_input.isnumeric():
        print('Morate unijeti brojke, ne tekst, odnosno slova!')
        user_input = input('Pokusajte ponovno unijeti ispravna broj iz izbornika: ')

    user_input = int(user_input)
    while user_input < 1 or user_input > 3:
        print('Krivi unos!')
        print('Upisite jedan od brojeva iz izbornika (1, 2 ili 3)!')
        user_input = int(input('Pokusajte ponovno unijeti ispravan broj iz izbornika: '))

    return int(user_input)
def check_game_status(computer_choice: int, user_choice: int) -> None:
    destination = 'console'

    if computer_choice == user_choice:
        message(
            f'Nerijeseno - Vas izbor {pieces[user_choice]} je isti kao {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 1 and user_choice == 2:
        message(
            f'Izgubili ste - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 1 and user_choice == 3:
        message(
            f'Pobijedili ste - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 2 and user_choice == 1:
        message(
            f'Pobijedili ste - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 2 and user_choice == 3:
        message(
            f'Izgubili ste - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 3 and user_choice == 1:
        message(
            f'Izgubili ste - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}.',
            destination
        )

    elif computer_choice == 3 and user_choice == 2:
        message(
            f'Pobijedili ste - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}.',
            destination
        )


while True:
    menu()

    computer_choice = random.randint(1, 3)
    user_choice = user_input_validator(input('Izaberite jedan broj iz izbornika: '))

    check_game_status(computer_choice, user_choice)

    next_round = input('Zelite li jos jednu igru? (Da/Ne) ')
    if next_round[ : 2].lower() != 'da':
        break


# Pozdravna poruka