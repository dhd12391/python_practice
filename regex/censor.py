#censor(), replacing bad words with asterisks 
import re

def censor(text,word):
    asterisks= "*" * len(word)
    
    text = re.sub(word,asterisks,text)
    
    return text