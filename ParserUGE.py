import requests
from bs4 import BeautifulSoup
import sqlite3
from Config import urlUGE
import time

def del_table():
	connect = sqlite3.connect('BDdiplom.db')
	cursor = connect.cursor()
	request = "DELETE FROM UGE"
	cursor.execute(request)
	connect.commit()
	connect.close()

def add_dir(direct, loc, exam, balf, balp, sf, sp, k1, k2, k3):
	connect = sqlite3.connect('BDdiplom.db')
	cursor = connect.cursor()
	request = "INSERT or REPLACE into UGE(name, loc, exam, balf, balp, sf, sp, k1, k2, k3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
	cursor.execute(request, (direct, loc, exam, balf, balp, sf, sp, k1, k2, k3))
	connect.commit()
	connect.close()

def funcf(bal1):
	r_bal = bal1.replace(' ', '')
	r_bal = r_bal.replace("\n", '')
	balf = r_bal.partition('/')[0]
	balf = balf.replace('-', '') 
	if balf != "\xa0"and balf != "\xa020\xa010" and balf != "\xa05\xa05" and balf != "\xa0100\xa0100":
		balf = int(balf)
	else:
		balf = None

	return balf

def funcp(bal1):
	r_bal = bal1.replace(' ', '')
	r_bal = r_bal.replace("\n", '')
	balp = r_bal.partition('/')[2]
	balp = balp.replace('-', '')
	if balp != "\xa0" and balp != "\xa020\xa010" and balp != "\xa05\xa05" and balp != "\xa0100\xa0100":
		balp = int(balp)
	else:
		balp = None

	return balp

def main(soup):
	del_table()
	f = open('buge.txt','w')
	f.write('1')
	f.close()
	main = soup.find_all('div', {'class': ['grid__row d-xl-flex align-items-center']})
	for m in main:
		i = []
		dir1 = m.find('a',{'class': ['programs__toggle']})
		loc1 = m.find('div',{'class': ['programs__city']})
		exam1 = m.find('div',{'class': ['w-50']})
		bal1 = m.find('span',{'class': ['programs__form-points d-block d-flex align-items-center']})
		seats = m.find('span',{'class': ['programs__form-value d-flex align-items-center mx-sm-2']})
		key = m.find_all('span',{'class': ['d-inline-block']})
		if dir1 != None:
			r_exam = exam1.text.replace(' ', '') 
			r_exam = r_exam.replace("\n", '') 
			for k in key:
				ks = k.text.replace(' ', '') 
				i.append(ks)
			if len(i) == 1:
				i.append(None)
				i.append(None)
			if len(i) == 2:
				i.append(None)
			add_dir(dir1.text, loc1.text, r_exam, funcf(bal1.text), funcp(bal1.text), funcf(seats.text),  funcp(seats.text), i[0], i[1], i[2])
			#mi = dir1.text+'___'+loc1.text+'___'+r_exam+'___'+balf+'___'+balp
	f = open('buge.txt','w')
	f.write('0')
	f.close()
		
r = requests.get(urlUGE)
soup = BeautifulSoup(r.text, features="html5lib")

# f = open('xyz.html','w')
# f.write(r.text)
#while True:

main(soup)
	#time.sleep(3600) 