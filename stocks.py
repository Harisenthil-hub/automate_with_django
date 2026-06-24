from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f'https://finance.yahoo.com/quote/{symbol}/'
    elif exchange == 'NSE':
        url = f'https://finance.yahoo.com/quote/{symbol}.NS/'
        
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    current_price = soup.find(class_='yf-1ommk34')
    print(current_price)
    print(current_price.get_text())
    
    previous_close = soup.find(f'fin-streamer', {"data-field": 'regularMarketPreviousClose'})['data-value']
    print('previous_close', previous_close)
    price_change_container = soup.find(class_='yf-z2uro5')
    price_change = price_change_container.find('span',{"data-testid": "qsp-price-change"})
    price_percentage_change = price_change_container.find('span',{"data-testid": "qsp-price-change-percent"})
    
    print("Price Change===>",price_change.get_text())
    print("Price Change Percentage===>",price_percentage_change.get_text())
    
    
    week_52_low, week_52_high = soup.find('fin-streamer', {"data-field": "fiftyTwoWeekRange"}).text.split('-')
    market_cap = soup.find('fin-streamer', {"data-field": "marketCap"}).text
    pe_ratio = soup.find('fin-streamer', {"data-field": "trailingPE"}).text
    dividend_yield_span = soup.find_all('span', {"title": "Forward Dividend & Yield"})[0]
    dividend_yield = dividend_yield_span.find_next_sibling('span').text

    
    
    print(dividend_yield)
    return
    
    
scrape_stock_data('TCS', 'NSE')