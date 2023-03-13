import random

def rock_paper_scissors():
    potezi = ['kamen', 'škare', 'papir']
    computer_move = random.choice(potezi)
    player_move = input("Unesite svoj potez (kamen, škare, papir): ").lower()
    
    while player_move not in potezi:
        player_move = input("Unesite svoj potez (kamen, škare, papir): ").lower()
    
    print(f"Računalo igra {computer_move}.")
    print(f"Vi igrate {player_move}.")
    
    if computer_move == player_move:
        print("Neriješeno!")
    elif (computer_move == "kamen" and player_move == "škare") or (computer_move == "škare" and player_move == "papir") or (computer_move == "papir" and player_move == "kamen"):
        print("Računalo pobjeđuje!")
    else:
        print("Vi pobjeđujete!")
        
while True:
    rock_paper_scissors()
    odgovor = input("Želite li igrati ponovo? (da/ne) ").lower()
    if odgovor != "da":
        break
