from bs4 import BeautifulSoup
import requests


class Amazon():

    store_id = 2

    def __init__(self):
        self.store_id = 2
        print("Amazon class initialized")

    def my_deals(self, search_keyword):

        url = "https://www.amazon.com/slp/search-and-find/br8ehoh8wnnt93b"

        my_request = requests.get(url + search_keyword)
        soup = BeautifulSoup(my_request.text, 'html.parser')
        my_products = soup.find("div", attrs={'id': 'searchProductResult'})
        products = my_products.find_all("div", class_="search-result-gridview-item-wrapper")
        search_items = []

        for product in products:

            title = product.find("a", class_="product-title-link")
            price = product.find("span", class_="price-group")
            url = product.find("a", class_="product-title-link")
            actual_url = "http://amazon.com" + url.get("href")
            image_container = product.find("div", class_="search-result-productimage gridview")
            image_url = image_container.find("img", src=True)['src']
            store_icon = "images/amazon-icon.png"


            if title != None and price != None and url != None:

                record = {
                    'title': title.text,
                    'price': price.text,
                    'url': actual_url,
                    'image_url' : image_url,
                    'store_icon': store_icon,

                }

                search_items.append(record)

        return search_items
