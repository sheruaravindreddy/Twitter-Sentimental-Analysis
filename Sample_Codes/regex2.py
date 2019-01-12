import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://www.talkenglish.com/vocabulary/top-50-prepositions.aspx")
soup = BeautifulSoup(page.content, 'lxml')

text = soup.find_all('table')
text = str(text[1])

pattern_list = re.findall("[^A-Za-z]", text)
pattern_list = list(set(pattern_list))

def remove(pattern, replacement,text):
    r = re.findall(pattern,text)
    for index in r:
        re.sub(index, replacement, text)

start = 'target="_blank">'
end = '</a>'
prepositions = re.findall(start + '(.*?)' + end, text)
print (prepositions)
