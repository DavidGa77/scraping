# import libraries
import urllib2
from bs4 import BeautifulSoup
import sys

# specify the url
pop_page = 'https://www.cia.gov/library/publications/the-world-factbook/rankorder/2119rank.html'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(pop_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
all_country_table = soup.find('table', attrs={'id': 'rankOrder'})
# Ignore header row
rows = all_country_table.find_all('tr', attrs={'id': True})

# open file to write data
f = open('worldStats.txt', 'w')

for row in rows:
    col = row.find_next('td')
    col1 = col.find_next_sibling('td')
    col2 = col1.find_next_sibling('td')
    col3 = col2.find_next_sibling('td')
    f.write(col.text + "  "),
    f.write(col1.text + "  "),
    f.write(col2.text + "  "),
    f.write(col3.text)
    f.write("\n")

f.close()
