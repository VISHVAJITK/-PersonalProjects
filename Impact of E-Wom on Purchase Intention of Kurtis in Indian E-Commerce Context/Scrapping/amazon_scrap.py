from bs4 import BeautifulSoup
import requests
import  pandas as pd
import os

data = {"Rating":[],'Review':[]}
for i in range(1,151):
    url = f"https://www.amazon.in/Yash-Gallery-Womens-Bandhej-Anarkali/product-reviews/B07RF8TF3Y/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    try:
        page =soup.find('div', id = "cm_cr-review_list")
    except:
        continue
    try:
        rows = page.find_all('div', {"data-hook":"review"})
    except:
        continue

    for row in rows:
        try:
            rating = row.find('a',class_="a-link-normal")['title'][:3]
        except:
            continue
        try:
            text = row.find('span',{"data-hook":"review-body"}).text
        except:
            continue
        data["Rating"].append(rating)
        data["Review"].append(str(text).strip())
print(data)
    
dataframe = pd.DataFrame(data)
parent_path ="E:\Projects\IMPACT OF E-WOM ON PURCHASE INTENTION OF KURTIS"
path = os.path.join(parent_path,"data","file12.csv")
dataframe.to_csv(path)






