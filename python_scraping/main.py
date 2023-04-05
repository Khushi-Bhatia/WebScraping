from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
html_text = requests.get('https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sa').text
soup = BeautifulSoup(html_text,'lxml')
product_name_list=[] #empty list for product name
product_name = soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal') #fetching product name


product_rating_list=[] #empty list for product rating
product_rating = soup.find_all('span',class_='a-icon-alt') #fetching product rating

product_price_list=[] #empty list for product prices
product_price = soup.find_all('span',class_='a-offscreen') #fetching product prices

#appending respective data to list
for pn in product_name:
    product_name_list.append(pn.get_text())
    
for pp in product_rating:
    product_rating_list.append(pp.get_text())
    
for pr in product_price:
    product_price_list.append(pr.get_text())
    
fields = ["product_name","product_price","product_rating"] #declaring column-names

filename = 'example.csv'
mode = 'w'
data=[]

for i in range(len(product_name_list)):
    lst = [product_name_list[i],product_price_list[i],product_rating_list[i]]
    data.append(lst)
    print(lst)
# Writing data to CSV file
with open(filename, mode, newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    
    writer.writerows(data)





    



