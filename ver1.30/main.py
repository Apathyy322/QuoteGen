import json
import random
from pystyle import Colorate, Colors, Write
import os 
import ctypes
import requests
from colorama import Fore, init
import time
def titlo(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
titlo("Quote Generator 1.30")
quoteee = Write.Input("For Quotes press 1. For random advices press 2: ", Colors.white, interval=0).strip().lower()
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()
def getweather():
    url = 'https://wttr.in/?format=4' 
    resp = requests.get(url)
    resp.raise_for_status()  
    wthinf = resp.text.strip()  
    return wthinf

if __name__ == "__main__":
    weth = getweather()
    Write.Print(f"Current weather for you is:{weth}\n",Colors.white, interval=0)


if quoteee == "2":
    def advices():
        telo = requests.get("https://api.adviceslip.com/advice").json()
        advico = telo['slip']['advice']
        print("\n" +Fore.CYAN+ advico)
        wantnext = Write.Input(f"\nFor next advice type V: ",Colors.white, interval=0).strip().lower()
        if wantnext == "v":
            advices()
        else: 
            Write.Print(f"\nWrong Input!", Colors.red, interval=0)
            time.sleep(1.5)
            wantnext = Write.Input(f"\nFor next advice type V: ",Colors.white, interval=0).strip().lower()
            if wantnext == "v":
                advices()
                
            

    advices()
        

if quoteee == "1":
    lin = r'english.json'
    with open(lin, 'r') as listqts:
        qts = json.load(listqts)

    quotes = qts.get('quotes', [])

    if not quotes:
        print("No quotes found.")
        exit()

    prevqt = None
    curqt = random.choice(quotes)
    def pgetqt(quote, ifColEn):
        text = quote.get('text', 'No content')
        source = quote.get('source', 'No content')
        color = Colors.blue_to_cyan if ifColEn else Colors.white
        Write.Print(f'[+] Quote:"{text}", ©{source}', color, interval=0.015)
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
    color_choice = Write.Input("[?] Do you want gradient-colored text? (Y/N):~  ",Colors.white, interval=0.015).strip().upper()
    ifColEn = color_choice == 'Y'

    pgetqt(curqt, ifColEn)

    while True:
        prompt_color = Colors.blue_to_purple if ifColEn else Colors.white
        hadnler = Write.Input("\n[!] V for new quote, C for previous, Q to quit QuoteGen:~ ", prompt_color, interval=0.015).strip().upper()

        if hadnler == 'V':
            prevqt = curqt
            curqt = random.choice(quotes)
            pgetqt(curqt, ifColEn)

        elif hadnler == 'C':
            if prevqt is not None:
                pgetqt(prevqt, ifColEn)
                curqt, prevqt = prevqt, curqt
            else:
                Write.Print("No previous quote to show.", Colors.red_to_black if ifColEn else Colors.white, interval=0.015)

        elif hadnler == 'Q':
            exit()  

        else:
            Write.Print("Invalid input.", Colors.red_to_black if ifColEn else Colors.white, interval=0.015)
