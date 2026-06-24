from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f'https://finance.yahoo.com/quote/{symbol}/'
    elif exchange == 'NSE':
        url = f'https://finance.yahoo.com/quote/{symbol}.NS/'
        
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        #print('response==>', response.content)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            current_price = soup.find(class_='yf-1ommk34').text
            
            previous_close = soup.find(f'fin-streamer', {"data-field": 'regularMarketPreviousClose'}).text
            
            price_change = soup.find('span',{"data-testid": "qsp-price-change"}).text
            price_percentage_change = soup.find('span',{"data-testid": "qsp-price-change-percent"}).text
            week_52_low, week_52_high = soup.find('fin-streamer', {"data-field": "fiftyTwoWeekRange"}).text.split('-')
            market_cap = soup.find('fin-streamer', {"data-field": "marketCap"}).text
            pe_ratio = soup.find('fin-streamer', {"data-field": "trailingPE"}).text
            dividend_yield_span = soup.find_all('span', {"title": "Forward Dividend & Yield"})[0]
            dividend_yield = dividend_yield_span.find_next_sibling('span').text
            
            
            stock_response = {
                'current_price': current_price,
                'previous_close': previous_close,
                'price_change': price_change,
                'price_percentage_change': price_percentage_change,
                'week_52_low': week_52_low,
                'week_52_high': week_52_high,
                'market_cap': market_cap,
                'pe_ratio': pe_ratio,
                'dividend_yield': dividend_yield
            }
            return stock_response
    except Exception as e:
        print(f'Error scrapping the data: {e}')
        return None
        
