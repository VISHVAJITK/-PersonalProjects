from bs4 import BeautifulSoup
import requests
import  pandas as pd
import os

data = {"Rating":[],'Review':[]}
for i in range(2,479):
    url = "https://www.flipkart.com/sheqe-women-solid-straight-kurta/product-reviews/itmf882gxzyzgrqm?pid=KTAF86VJQTZTYTEC&lid=LSTKTAF86VJQTZTYTECEO9HNK&marketplace=FLIPKART&page={}".format(i)

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        page = soup.find('div', class_ = "_1YokD2 _3Mn1Gg col-9-12")
    except:
        continue
    try:
        reviews = page.find_all('div', class_ = "_1AtVbE col-12-12")
    except:
        continue
    for review in reviews[:-1]:
        try:
            rating = review.find('div',class_= "row").div.div.div.text
        except:
            continue
        try:
            text = review.find('div', class_ = "_6K-7Co").text
        except:
            continue
        data["Rating"].append(rating)
        data["Review"].append(text)
# print(data)


dataframe = pd.DataFrame(data)
parent_path ="E:\Projects\IMPACT OF E-WOM ON PURCHASE INTENTION OF KURTIS"
path = os.path.join(parent_path,"data","file8.csv")

dataframe.to_csv(path)
