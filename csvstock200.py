import csv
import requests
from bs4 import BeautifulSoup

filename = '시총top200.csv'

with open('./output/' + filename, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    
    title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
    writer.writerow(title)
    
    for page in range(1,5) :
        url = f'https://finance.naver.com/sise/sise_market_sum.naver?&page={page}' 
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }

        res = requests.get(url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'lxml')
        
        data_rows = soup.find('table', attrs={'class': 'type_2'}).find('tbody').find_all('tr')
        
        for row in data_rows :
            columns = row.find_all('td')
            if len(columns) <= 1 :
                continue
            
            data = [columns.get_text().strip() for columns in columns]
            
            writer.writerow((data))
            # title = stock.find('td').find('a', attrs ={'class' : 'title'})
            # print(title)
        