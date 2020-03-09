import requests
from bs4 import BeautifulSoup
import json
import re
import pandas

#Used headers/agent as the request timed out and asking for agent. Using following code you can fake the agent.
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get("https://www.zomato.com/bangalore/south-bangalore-restaurants",headers=headers)
# content = response.content
# soup = BeautifulSoup(content,"html.parser")
# print(soup.get_text())
#soup


#SCRAPING MULTIPLE PAGES#

count = 10000
list_rest = []
for i in range(1,301):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    response = requests.get("https://www.zomato.com/bangalore/south-bangalore-restaurants?page={}".format(i),headers=headers)
    content = response.content
    soup = BeautifulSoup(content,"html.parser")

    south_bang = soup.find_all("div",attrs={"class": "ui cards"})
    list_tr = south_bang[0].find_all("div",attrs={"class":"content"}) 
    # list_rest=[]
    for tr in list_tr:
        count = count+1
        dataframe={
            "ResturantId" : count,
            "ResturantName" : tr.find('a', attrs={"class":"result-title hover_feedback zred bold ln24 fontsize0"}).text.replace('\n', ' '),
            # "ResturantType" : tr.find('a', attrs={"class": "col-s-11 col-m-12 nowrap pl0"}).text.encode('utf-8').text.replace('\n',' '),
            "ResturantZone" : tr.find('a', attrs={"ln24 search-page-text mr10 zblack search_result_subzone left"}).text.replace('\n',' '),
            "ResturanantAddress" : tr.find('div', attrs={"class":"col-m-16 search-result-address grey-text nowrap ln22"}).text.replace('\n', ' '),
            "ResturantTiming" : tr.find('div', attrs={"class": "col-s-11 col-m-12 pl0 search-grid-right-text"})
            }
        list_rest.append(dataframe)            
    print(list_rest)

    
df = pandas.DataFrame(list_rest)
df.to_csv("zomato.csv",index=False)  
