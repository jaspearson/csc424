from bs4 import BeautifulSoup
import requests
from deals.models import Deal
from decimal import *

class Walmart():

    store_id = 1

    def __init__(self):
        self.store_id = 1
        print("The wal-mart class was initialized.")

    def get_deals(self):

        url = 'https://www.walmart.com/browse/electronics/3944/?cat_id=3944&facet=special_offers%3AClearance%7C%7Cspecial_offers%3ARollback%7C%7Cspecial_offers%3ASpecial+Buy'

        # Make the request
        the_request = requests.get(url)

        # Parse the request
        soup = BeautifulSoup(the_request.text, 'html.parser')

        # Get the table that holds the products
        products_table = soup.find("div", attrs={'id': 'searchProductResult'})

        # Get all product container divs
        products = products_table.find_all("div", class_="search-result-gridview-item-wrapper arrange")

        # Initialize a dictionary object
        extracted_records = []

        # Loop through the the html products and extract key pieces of information.
        # title of product, price of the product, url to the product, etc
        for product in products:

            title = product.find("a", class_="product-title-link").text
            price = product.find("span", class_="price-group").text
            url = "http://walmart.com" + product.find("a", class_="product-title-link").get('href')

            print("%s - %s" % (title, price))
            record = {
                'title': title,
                'price': price,
                'url': url
            }

            # Append each new product and attributes to the dictionary object
            extracted_records.append(record)

        # Return the extracted records to the calling program
        return extracted_records

    def get_deals(self, this_keyword):

        url = "https://www.walmart.com/search/?query="

        # Make the request
        the_request = requests.get(url + this_keyword)

        # Parse the request
        soup = BeautifulSoup(the_request.text, 'html.parser')

        # Get the table that holds the products
        products_table = soup.find("div", attrs={'id': 'searchProductResult'})

        # Get all product container divs
        products = products_table.find_all("div", class_="search-result-gridview-item-wrapper")

        # Initialize a dictionary object
        extracted_records = []

        # Loop through the the html products and extract key pieces of information.
        # title of product, price of the product, url to the product, etc
        for product in products:

            title = product.find("a", class_="product-title-link")
            price = product.find("span", class_="price-group")
            url = product.find("a", class_="product-title-link")
            actual_url = "http://walmart.com" + url.get("href")
            image_container = product.find("div", class_="search-result-productimage gridview")
            image_url = image_container.find("img", src=True)['src']
            store_icon = "images/walmart-icon.png"



            if title != None and price != None and url != None:

                # Get the product ID of the item from the URL.
                # The product ID is usually encoded into the URL to make it unique.
                # We will use this value to keep things unique in our database.
                # In Wal-mart's case the product ID was at the end of the URL.
                # Other stores might be in the middle of the URL and a different
                # method for stripping it out may be needed.

                # Use the / character as the delimiter to split the url in to different pieces and store it in an
                # array.
                split_url = actual_url.split('/')

                # Get the number of elements in the splitURL array.
                array_size = len(split_url)

                # Get the position of the product ID.
                # In the case of Wal-mart, it is stores the item id at the end of the URL.
                # Therefore, it will be the last element in the array when the URL is split up.
                product_id_element = array_size-1

                # Get the product_id
                product_id = split_url[product_id_element]

                # dealio_id will be the store_id - product_id
                # Example: 1-19758129
                dealio_id = str(self.store_id) + "-" + product_id

                print("%s - %s, %s" % (title.text, price.text.strip(' - $'), dealio_id))

                record = {
                    'title': title.text.strip('...'),
                    'price': price.text,
                    'url': actual_url,
                    'image_url' : image_url,
                    'store_icon': store_icon,
                    'product_id': dealio_id
                }

                # jaspearson's attempt to save records to the mysql database.
                # Will continue work on this part later. Commenting out for now.
                """r = Deal(url="http://walmart.com" + url.get("href"),
                         image_url=image_url, title=title.text,
                         price=Decimal(price.text.strip(' - $')),
                         featured_product=False,
                         store_id=self.store_id,
                         product_id=dealio_id)

                r.save()
                """
                # Append each new product and attributes to the dictionary object
                extracted_records.append(record)

        # Return the extracted records to the calling program
        return extracted_records


