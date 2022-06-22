import pyshorteners
from pyperclip import copy
from pystyle import Write, Colors
Write.Print("Welcome To Py URL Shortener\n", Colors.baby_blue, interval=0.0025)
while True:
    url = Write.Input("Enter URL: ", Colors.dap_blue, interval=0.025, hide_cursor=False)
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    copy( short_url)
    Write.Print(f"Shortened URL: {short_url}\nCopied short url to clipboard\n", Colors.dap_blue, interval=0.025)
    end = Write.Input("Press enter to continue or type 'exit' to exit: ", Colors.dap_blue, interval=0.025, hide_cursor=False)
    if end == "exit":
        break
    else:
        continue