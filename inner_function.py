import requests
from bs4 import BeautifulSoup
url="https://www.amazon.com/product-reviews/B0CGY2KM7S/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar"
uesr_agents={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
r=requests.get(url,headers=uesr_agents)
soup1=BeautifulSoup(r.text,"html.parser")
# soup2=BeautifulSoup(soup1.prettify(),"html.parser")
# title=soup2.find_all("span",class_="navFooterDescText")
# print(title)
print(soup1.prettify())