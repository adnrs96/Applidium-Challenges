import requests
import sys
from bs4 import BeautifulSoup

print 'Ratings for app with name:',
app_name = raw_input()

# For Apple AppStore(Itunes)
sys.stdout.write('Fetching...')
sys.stdout.flush()
try:
    app_page_url = requests.get('https://itunes.apple.com/search?term=%s&entity=software'%('+'.join(app_name.split(' ')))).json()['results'][0]['trackViewUrl']
    app_page = requests.get(app_page_url)
    soup = BeautifulSoup(app_page.text, 'html.parser')
    ratings = soup.find_all('span','rating-count')
    print('\rApple App store Ratings:')
    print('Current Version : %s' % (ratings[0].get_text()))
    print('All Version : %s' % (ratings[1].get_text()))
except:
    print('App not available on Apple App Store')
