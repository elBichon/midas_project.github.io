import bs4 as bs
import urllib.request
import pandas as pd

def text_extractor(start,end,s):
    return (s.split(start))[1].split(end)[0]


link_list = ['https://www.boursorama.com/bourse/actions/palmares/dividendes/page-1?market=1rPCAC&sector=&variation=6&filter=&pagination_1995755903=','https://www.boursorama.com/bourse/actions/palmares/dividendes/page-2?market=1rPCAC&sector=&variation=6&filter=&pagination_1995755903=']
symbol = []

for link in link_list:
	source = urllib.request.urlopen(link).read()
	soup = bs.BeautifulSoup(source,'lxml')
	for tt in soup.find_all('tr','c-table__row'):
			try:		
				text = text_extractor('<tr class="c-table__row" data-ist="','" data-ist-init=',str(tt))
				symbol.append(text)
			except:
				pass

print(symbol)

name = []
advice = []
link = []
for sym in symbol:
	link = 'https://www.boursorama.com/cours/consensus/'+sym
	print(link)
	source = urllib.request.urlopen(link).read()
	soup = bs.BeautifulSoup(source,'lxml')
	try:
		for tt in soup.find_all('td','c-table__cell c-table__cell--dotted c-table__cell--color-1-inverse c-table__cell--shifted c-table__cell--bold'):
			text = text_extractor('<span class="c-table__content">','</span></div> </td>',str(tt))
			name.append(sym)
			print(text)
			advice.append(text)
	except:
		pass


data = {'name':name,'advice':advice}
print(data)
data_dict_offre = pd.DataFrame.from_dict(data)
data_dict_offre.to_csv('values.csv')
