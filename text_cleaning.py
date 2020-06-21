import string
import re
import emoji

text = open('text.txt', encoding='utf-8').read()
text = text.lower()
"""make text url free"""
text = re.sub(r'http\S+',"",text)

"""changing emoji to text"""
for word in text:
    if word in emoji.UNICODE_EMOJI:
        text = re.sub(r'('+word+')', emoji.demojize(word).replace('_',' ')+' ', text)

"""removing punctuations like  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
cleaned_text = text.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)