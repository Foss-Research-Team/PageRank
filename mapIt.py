#! /usr/bin/env python3
import webbrowser, sys, pyperclip
  
sys.argv  # example ['mapit.py', '870', 'Valencia', 'St.']
address = 'Home'
if len(sys.argv) > 1 :
   address = ' '.join(sys.argv[1:]) # ['870', 'Valencia', 'St.']
else :
    # Get address from clipboard
    address = pyperclip.paste()
  
# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)
