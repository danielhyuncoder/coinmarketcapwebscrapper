from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app=FastAPI()

@app.get('/data/{coin_name}')
def data(coin_name):
  req=requests.get('https://coinmarketcap.com/currencies/bitcoin/')
  parser=BeautifulSoup(req.text, "html.parser")
  price =parser.find("span", class_="sc-f70bb44c-0 jxpCgO base-text")
  data=parser.find_all("dd", class_="sc-f70bb44c-0 bCgkcs base-text")
  return {"price": price.text,"marketcap": data[0].text.split("%")[1], "volume24": data[1].text.split("%")[1], "circulatingsupply":data[3].text.split("%")[0], "maxsupply":data[5].text.split("%")[0], "fullydilutedcap":data[6].text.split("%")[0]}
