import requests 
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
from dash import Dash, dash_table

#Access the page using reuqest  
URL = 'https://www.tusboletos.mx/eventos'
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")

#Select the area of interest 
mydivs = soup.find_all("div", {"class": "col-sm-4 col-lg-3"})

#Create the lists to append the information 
title_events = []
date_events = []
host_events = []
location_events = []

#Start the cycle to save the relevant information in the HTML 

for mydiv in mydivs:
  
  title_event = mydiv.find('h4')
  title_events.append(title_event.text)

  detail = mydiv.find('div',{"class": "detail caption"})
  
  date_event = detail.find('p')
  date_events.append(date_event.text)

  host_event = detail.find('p',{"class": "hidden-xs"})
  host_events.append(host_event.text)

  if detail.find('b') == None: 
    location_events.append('N/A')
  else:
    location_event = detail.find('b')
    location_events.append(location_event.text)


print(len(title_events))
print(len(date_events))
print(len(host_events))
print(len(location_events))

#Create the array with all the lists 
array = np.column_stack((title_events, date_events, host_events, location_events))

#Create the dataframe with the info 
df = pd.DataFrame(data=array, columns=['Description','Date', 'Location', 'City'])

app = Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
    	{'name': 'Host City', 'id': 'City', 'type': 'text'},
        {'name': 'Event Date', 'id': 'Date', 'type': 'text'},
        {'name': 'Event Description', 'id': 'Description', 'type': 'text'},
        {'name': 'Event location', 'id': 'Location', 'type': 'text'},
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
