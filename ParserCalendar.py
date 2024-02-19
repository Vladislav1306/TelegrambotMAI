import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Config import urlCal, chromedriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import re
from ICSgen import *
import time

def create_browser(webdriver_path):
    #create a selenium object that mimics the browser
    browser_options = Options()
    #headless tag created an invisible browser
    #browser_options.add_argument("--headless")
    #browser_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(webdriver_path, options=browser_options)
    print("Done Creating Browser")

    return browser

def get_soup(browser):
	ph = browser.page_source
	soup = BeautifulSoup(ph, features="html5lib")

	return soup

def event_days(browser):
	ed = []
	day_list = get_soup(browser).find('div', {'class': 'swiper-container cal2-navDays'})
	days = day_list.find_all('a', {'class': ['cal2-navItem today swiper-slide', 'cal2-navItem swiper-slide']})
	for day in days:
		ad = day.get('data-date')
		event = day.find('span',{'class': ['cal-catItem']})

		if event != None:
			ed.append(ad)
			# print (ad)
	#print (ed)
	return ed

def extra_days(browser):
	l = 0
	extra_list = get_soup(browser).find('div', {'class': 'swiper-container cal2-navDays'})
	extra = extra_list.find_all('a', {'class': ['cal2-navItem cal2-navItemPad']})
	for e in extra:
		m = re.findall(r'\d+',e.find('span', {'class': 'cal2-navItemDay'}).text)
		#print (m)
		if int(m[0]) > 15:
			l=l+1
	#print(l)
	return l

def click_ed(browser, ed):
	f = open('bcal.txt','w')
	f.write('1')
	f.close()
	for i in ed:
		browser.implicitly_wait(10)
		j = int(i) + extra_days(browser)
		browser.find_element(By.XPATH, '//*[@id="cal2-navDays"]/div/a['+str(j)+']').click()

		# ph = browser.page_source
		# f = open('xyz.html','w')
		# f.write(ph)

		day_inf = get_soup(browser).find_all('div', {'class': 'cal2-noteSlideContent'})

		for day1 in day_inf:

			if day1.find('div', {'class': 'cal2-note-msgHeader'}).text != '':

				day_time = day1.find('span', {'class': 'cal2-note-time'}).text
				day_inf_event = day1.find('div', {'class': 'cal2-note-msgHeader'}).text
				day_loc = day1.find('span', {'class': 'cal2-note-location'}).text
				day_text = day1.find('div', {'class': 'cal2-note-msgText'}).text

				if day_time[0:2] != '':
					dtb1 = int(day_time[0:2]) - 3
					dtb = str(dtb1)
					if len (dtb) != 2:
						dtb = '0'+dtb
				else:
					dtb = "21"

				if day_time[6:8] != '':
					dte1 = int(day_time[6:8]) - 3
					dte = str(dte1)
					if len (dte) != 2:
						dte = '0'+dte
				else:
					dte = dtb

				#di = i+'-'+day_time+'-'+day_inf_event+'-'+day_loc
				month = get_soup(browser).find('button', {'class': 'text-larger btn btn-default btn-cal mx-1'}).text
				if month == 'Январь':
					#print (day_time[9:11])
					M = '01'
				elif month == 'Февраль':
					#print ('02м-' + di)
					M = '02'
				elif month == 'Март':
					#print ('03м-' + di)
					M = '03'
				elif month == 'Апрель':
					#print ('04м-' + di)
					M = '04'
				elif month == 'Май':
					#print ('05м-' + di)
					M = '05'
				elif month == 'Июнь':
					#print ('06м-' + di)
					M = '06'
				elif month == 'Июль':
					#print ('07м-' + di)
					M = '07'
				elif month == 'Август':
					#print ('08м - ' + di)
					M = '08'
				elif month == 'Сентябрь':
					#print ('09м-' + di)
					M = '09'
				elif month == 'Октябрь':
					#print ('10м-' + di)
					M = '10'
				elif month == 'Ноябрь':
					#print ('11м-' + di)
					M = '11'
				elif month == 'Декабрь':
					#print ('12м-' + di)
					M = '12'
				write_event (i, M, cy, dtb, dte, day_time, day_inf_event, day_loc, day_text)
		clickable = browser.find_element(By.XPATH, '//*[@id="mdl-itemContent"]/div/div/div[3]/button')
		ActionChains(browser)\
			.click(clickable)\
			.perform()
	f = open('bcal.txt','w')
	f.write('0')
	f.close()

def switch_month(browser):
	browser.execute_script("window.scrollTo(0, 300)") 
	while get_soup(browser).find('button', {'class': 'text-larger btn btn-default btn-cal mx-1'}).text != 'Январь':
		browser.implicitly_wait(10)
		browser.find_element(By.XPATH, '//*[@id="cal-mainbody"]/div[1]/div[1]/div/div[1]/a[1]').click()

	for i in range(12):
		click_ed(browser, event_days(browser))
		browser.find_element(By.XPATH, '//*[@id="cal-mainbody"]/div[1]/div[1]/div/div[1]/a[2]').click()

browser = create_browser(chromedriver)
browser.get(urlCal)

while True:

	switch_month(browser)
	time.sleep(3600) 
	browser.refresh()