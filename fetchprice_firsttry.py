import requests, bs4
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)

page = requests.get('https://store.google.com/product/nexus_6p')
page.raise_for_status()
bsobj = bs4.BeautifulSoup(page.text, 'html.parser')


element = bsobj.select('.break-text-hide')

text = element[0].getText()

print("Current Price : " + text.split()[2]);