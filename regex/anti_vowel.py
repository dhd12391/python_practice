#anti_vowel() using regex 

import re

def anti_vowel(text):
	text = re.sub('[aeiouAEIOU]','',text)
	return text
