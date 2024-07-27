import json
import random
from pystyle import Colorate, Colors, Write
lin = r'c:\Users\User\Documents\!CODE\quotes\english.json'
import os 
with open(lin, 'r') as listqts:
    qts = json.load(listqts)

quotes = qts.get('quotes', [])

if not quotes:
    print("No quotes found.")
    exit()

prevqt = None
curqt = random.choice(quotes)

def pgetqt(quote):
    text = quote.get('text', 'No content')
    source = quote.get('source', 'No content')
    Write.Print(f'Quote:\n"{text}", ©{source}', Colors.blue_to_cyan, interval=0.025)

pgetqt(curqt)

def cls():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

while True:
    hadnler = Write.Input("\nV for new quote, C for previous, Q to quit QuoteGen: ",Colors.blue_to_purple, interval=0.025).strip().upper()
    cls()
    if hadnler == 'V':
        prevqt = curqt
        curqt = random.choice(quotes)
        pgetqt(curqt)
        cls()
        
    elif hadnler == 'C':
        if prevqt is not None:
            pgetqt(prevqt)
            curqt, previqt = prevqt, curqt
            cls()
        else:
            Write.Print("No previous quote to show.",Colors.red_to_black,interval=0.025)
            cls()
    
    elif hadnler == 'Q':
        break
    
    else:
        Write.Print("Invalid input.",Colors.red_to_black, interval=0.025)
        cls()
