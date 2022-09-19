from selenium import webdriver
import urllib
import numpy as np 
import pandas as pd 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\Program Files (x86)\chromedriver.exe" #
driver = webdriver.Chrome(PATH)

df = pd.read_csv(r'C:\Users\Oswaldo\Documents\Leonel\Leo\Master\Webscraping\Events\101.csv')

dates = []
locations_1 = []
locations_2 = []

c=1
for i in range(24):
	u=i+0
	url = df.Link.iloc[u]
	driver.get(url)
	driver.implicitly_wait(2)

	dates.append(int(0))
	locations_1.append(int(0))
	locations_2.append(int(0))

	try:
		place = driver.find_element(By.XPATH,".//div[@class='c-place']")
		date = driver.find_element(By.XPATH,".//span[@class='c-event-info__date']")
		dates[c-1] = date.text

		place_1 = place.find_element(By.XPATH,".//h4")
		locations_1[c-1] = place_1.text

		place_2 = place.find_element(By.XPATH,".//p")
		locations_2[c-1] = place_2.text
	
		place_1 = place.find_element(By.XPATH,".//b")
		locations_1[c-1] = place_1.text

	except NoSuchElementException:
		print("exception handled")
	c=c+1

	print(locations_1)

driver.quit()
array = np.column_stack((locations_1, locations_2, dates))
res = pd.DataFrame(data=array, columns=['L1','L2', 'Date'])
file_name = 'C://Users//Oswaldo//Documents//Leonel//Leo//Master//Webscraping//Events//61_1.csv'
res.to_csv(file_name, encoding='utf-8')
 
