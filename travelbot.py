import re, random
from colorama import Fore, init
init(autoreset=True)

# Data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don’t programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize(text): return re.sub(r"\s+", " ", text.strip().lower())

# Travel recommendations
def recommend():
    pref = normalize(input(f"{Fore.CYAN}TravelBot: Beaches, mountains, or cities?\n{Fore.YELLOW}You: "))
    if pref in destinations:
        while True:
            suggestion = random.choice(destinations[pref])
            print(f"{Fore.GREEN}TravelBot: How about {suggestion}?")
            ans = input(f"{Fore.YELLOW}You (yes/no): ").lower()
            if ans == "yes": return print(f"{Fore.GREEN}TravelBot: Awesome! Enjoy {suggestion}!")
            if ans == "no": continue
            return
    else:
        print(f"{Fore.RED}TravelBot: Sorry, I don’t have that type of destination.")

# Packing tips
def packing():
    loc = normalize(input(f"{Fore.CYAN}TravelBot: Where to?\n{Fore.YELLOW}You: "))
    days = input(f"{Fore.CYAN}TravelBot: How many days?\n{Fore.YELLOW}You: ")
    print(f"{Fore.GREEN}TravelBot: Packing tips for {days} days in {loc}:")
    print("- Pack versatile clothes\n- Bring chargers/adapters\n- Check the weather forecast")

# Jokes & Help
def tell_joke(): print(f"{Fore.GREEN}TravelBot: {random.choice(jokes)}")
def show_help():
    print(f"""{Fore.MAGENTA}\nI can:
{Fore.GREEN}- Suggest travel spots ('recommendation')
- Offer packing tips ('packing')
- Tell a joke ('joke')
- Show this menu ('help')
- Exit ('exit')\n""")

# Main Chat
def chat():
    print(f"{Fore.CYAN}Hello! I’m TravelBot.")
    name = input(f"{Fore.YELLOW}Your name? ")
    print(f"{Fore.GREEN}Nice to meet you, {name}!")
    show_help()

    while True:
        user = normalize(input(f"{Fore.YELLOW}{name}: "))
        if "recommend" in user or "suggest" in user: recommend()
        elif "pack" in user: packing()
        elif "joke" in user or "funny" in user: tell_joke()
        elif "help" in user: show_help()
        elif "exit" in user or "bye" in user:
            print(f"{Fore.CYAN}TravelBot: Safe travels! Goodbye!")
            break
        else: print(f"{Fore.RED}TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
