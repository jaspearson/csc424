from bs4 import BeautifulSoup
import requests

class Target():

    def __init__(self):
        print("The Target class was initialized.")

    def get_deals(self):

        url = 'https://www.target.com/c/electronics/-/N-5xtg6'

        the_request = requests.get(url)

        soup = BeautifulSoup(the_request.text, 'html.parser')

        products_table = soup.find("div", attrs={'id': 'searchProductResult'})

        products = products_table.find_all("div", class_="search-result-gridview-item-wrapper arrange")

        extracted_records = []


        for product in products:

            title = product.find("a", class_="product-title-link").text
            price = product.find("span", class_="price-group").text
            url = "https://www.target.com/" + product.find("a", class_="product-title-link").get('href')

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


    def get_deals(self,this_keyword):
        url = "https://www.target.com/search/?query="

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
            image_container = product.find("div", class_="search-result-productimage gridview")
            image_url = image_container.find("img", src=True)['src']
            store_icon = "images/target-icon.png"

            if title != None and price != None and url != None:

                print("%s - %s" % (title.text, price.text))

                record = {
                    'title': title.text,
                    'price': price.text,
                    'url': "http://target.com" + url.get("href"),
                    'image_url': image_url,
                    'store_icon': store_icon
                }

                # Append each new product and attributes to the dictionary object
                extracted_records.append(record)


        return extracted_records