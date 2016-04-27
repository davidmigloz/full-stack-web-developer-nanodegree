"""
Scan the text of a file and translate it to Pirate speech
"""

import urllib

def read_text():
    quotes = open("./movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    translate(contents_of_file)
    

def translate(text):
    conn = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text)
    output = conn.read()
    conn.close()
    print(">Translation:")
    print(output)

read_text()
