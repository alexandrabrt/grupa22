from bs4 import BeautifulSoup
import requests
import pandas


r = requests.get("https://www.bnr.ro/Cursul-de-schimb-524.aspx", verify=False)
link = BeautifulSoup(r.text, 'html.parser')

table = link.find_all('table', attrs={"class": "cursTable"})[0]
header = []
dataset = []
for tr_index in table.find_all('tr'):
    td_list = []
    if tr_index.find_all('th'):
        for th_index in tr_index.find_all('th'):
            header.append(th_index.get_text())
    for index, td_value in enumerate(tr_index.find_all('td')):
        print(index, td_value)
        if index == 0 or index == 1:
            td_list.append(td_value.get_text())
        elif index != 7:
            td_list.append(float(td_value.get_text().replace(',', '.')))
    dataset.append(td_list)
print(header)
print(dataset)

df = pandas.DataFrame(dataset, columns=header)
df.to_csv("CursBNR.csv", header=header)
