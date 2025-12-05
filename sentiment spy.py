import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}★ Welcome to Sentiment Spy! ★{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip() or "Friendly Agent"
print(f"{Fore.CYAN}Hello Agent {user_name}! Type 'exit' to quit, 'reset' to clear, or 'history' to view chat.{Style.RESET_ALL}")

history = []

while True:
    text = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
    if not text:
        print(f"{Fore.RED}Please enter valid text or command.{Style.RESET_ALL}")
        continue

    # Commands
    if text.lower() == "exit":
        print(f"{Fore.BLUE}Exiting... Goodbye Agent {user_name}!{Style.RESET_ALL}")
        break
    if text.lower() == "reset":
        history.clear()
        print(f"{Fore.CYAN}Conversation history cleared!{Style.RESET_ALL}")
        continue
    if text.lower() == "history":
        if not history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for i, (msg, pol, sent) in enumerate(history, 1):
                color = { "Positive": Fore.GREEN, "Negative": Fore.RED, "Neutral": Fore.YELLOW }[sent]
                print(f"[{i}] {color}{msg} ({pol:.2f}, {sent}){Style.RESET_ALL}")
        continue

    # Sentiment analysis
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        sentiment, color = "Positive", Fore.GREEN
    elif polarity < -0.05:
        sentiment, color = "Negative", Fore.RED
    else:
        sentiment, color = "Neutral", Fore.YELLOW

    history.append((text, polarity, sentiment))
    print(f"{color}Sentiment detected → {sentiment} ({polarity:.2f}){Style.RESET_ALL}")
