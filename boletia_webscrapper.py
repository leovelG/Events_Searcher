from selenium import webdriver
import urllib
import numpy as np 
import pandas as pd 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

days_info = []
months_info = []
titles_info = []
locations_info = []
hrefs = []
prices = []

for i in range(21):
	page_lov = 81+int(i)
	PATH = "C:\Program Files (x86)\chromedriver.exe" #
	driver = webdriver.Chrome(PATH)
	page = "&page={}".format(page_lov)
	url = "https://boletia.com/search?q="+page


	driver.get(url)
	driver.implicitly_wait(2) #Waits for 5 seconds to load the page
	postings=driver.find_elements(By.XPATH,".//div[@class='o-event-card is-event js-search']")

	for posting in postings:
		href_loc = posting.find_element(By.XPATH,".//a[@class='o-event-card__banner']")
		href= href_loc.get_attribute('href')
		event_info=posting.find_element(By.XPATH,".//div[@class='o-event-card__info']")
		day_info = event_info.find_element(By.XPATH,".//span[@class='o-event-card__day']")
		month_info = event_info.find_element(By.XPATH,".//span[@class='o-event-card__month']")
		title_info = event_info.find_element(By.XPATH,".//h3[@class='o-event-card__title']")
		location_info = event_info.find_element(By.XPATH,".//span[@class='o-event-card__venue']")
		price = posting.find_element(By.XPATH,".//div[@class='o-event-card__price']")

		prices.append(price.text)
		hrefs.append(href)
		days_info.append(day_info.text)
		months_info.append(month_info.text)
		titles_info.append(title_info.text)
		locations_info.append(location_info.text)

		
array = np.column_stack((days_info, months_info, titles_info, locations_info, hrefs, prices))
res = pd.DataFrame(data=array, columns=['Day','Month', 'Description', 'Location', 'Link', 'Price'])
file_name = 'C://Users//Oswaldo//Documents//Leonel//Leo//Master//Webscraping//Events//{}.csv'.format(page_lov)
res.to_csv(file_name, encoding='utf-8')
driver.quit() 
