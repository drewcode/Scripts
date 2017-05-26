# -*- coding: utf8 -*-

import re
import requests
from bs4 import BeautifulSoup

urls = ['http://www.flipkart.com/nexus-6p/p/itmecw7y9ashzgcg?pid=MOBEBZPFWGYVFTFD&ref=L%3A-3756255935687078533&srno=p_3&query=nexus+6p&otracker=from-search',
                    'http://www.flipkart.com/nexus-6p/p/itmecw7y9ashzgcg?pid=MOBEBZPF5PHGRKXT&ref=L%3A-3756255935687078533&srno=p_4&query=nexus+6p&otracker=from-search']

expected_results = [u'39,999', u'39,999']

def get_product_meta(url):
    reg = ur'^ ₹? (\d+)'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_name = soup.find('meta', {'property' : 'og:title'})['content']
        product_url = soup.find('meta', {'property' : 'og:url'})['content']
        product_img_url = soup.find('meta', {'property': 'og:image'})['content']
        product_price_tag_element = soup.find('span', {'id': 'hs18Price', 'itemprop': 'price'})
        product_price_match = re.match(reg, product_price_tag_element.text)
        if product_price_match:
            product_price = product_price_match.group(1)
        else:
            product_price = None
        return (product_url, product_name, product_img_url, product_price)
    return None

if __name__ == '__main__':
    assert(map(lambda x: x[3], map(get_product_meta, urls)) == expected_results)