import random
from colorama import init, Fore, Style
init(autoreset=True)

def show(b):
    c = lambda x: (Fore.RED if x=='X' else Fore.BLUE if x=='O' else Fore.YELLOW)+x+Style.RESET_ALL
    print(f"{c(b[0])}|{c(b[1])}|{c(b[2])}\n-+-+-\n{c(b[3])}|{c(b[4])}|{c(b[5])}\n-+-+-\n{c(b[6])}|{c(b[7])}|{c(b[8])}")

def win(b, s): 
    return any(b[a]==b[b1]==b[c]==s for a,b1,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def move(b, s):
    while True:
        m = input(f"Your move (1-9): ")
        if m.isdigit() and 1<=int(m)<=9 and b[int(m)-1].isdigit(): b[int(m)-1]=s; break
        print("Invalid!")

def ai(b, ai, p):
    for i in range(9):
        if b[i].isdigit():
            for sym in (ai, p):
                t=b.copy(); t[i]=sym
                if win(t, sym): b[i]=ai; return
    b[random.choice([i for i,v in enumerate(b) if v.isdigit()])] = ai

def game():
    print(Fore.CYAN+"Welcome to Tic-Tac-Toe!"+Style.RESET_ALL)
    name=input("Name: ")
    while True:
        b=[str(i+1) for i in range(9)]
        p, ai_s = ('X','O') if input("X or O: ").upper()=='X' else ('O','X')
        turn="P"
        while True:
            show(b)
            if turn=="P": move(b,p)
            else: ai(b,ai_s,p)
            if win(b,p): show(b); print(f"Congrats {name}! You win!"); break
            if win(b,ai_s): show(b); print("AI wins!"); break
            if all(not x.isdigit() for x in b): show(b); print("It's a tie!"); break
            turn = "AI" if turn=="P" else "P"
        if input("Play again? (y/n): ").lower()!='y': break

if __name__=="__main__": game()
