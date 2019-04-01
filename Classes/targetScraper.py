from bs4 import BeautifulSoup
import requests

class Target():

    def __init__(self):
        print("The Target class was initialized.")




    def get_deals(self,this_keyword):
        url = "https://www.target.com/s?searchTerm=tv"

        # Make the request
        the_request = requests.get(url + this_keyword)

        # Parse the request
        soup = BeautifulSoup(the_request.text, 'html.parser')


        products_table = soup.find("div", attrs={'class': 'sc-htpNat'})

        products = products_table.find_all("div", class_="styles__StyledProductCardRow-sc-14k8w5n-1")


        # Initialize a dictionary object
        extracted_records = []

        # Loop through the the html products and extract key pieces of information.
        # title of product, price of the product, url to the product, etc
        for product in products:

            title = product.find("a", class_="flex-grow-one styles__StyledTitleLink-sc-14k8w5n-5")
            price = product.find("span", class_="styles__StyledPricePromoWrapper-sc-14k8w5n-13")
            url = product.find("a", class_="flex-grow-one styles__StyledTitleLink-sc-14k8w5n-5")
            #image_container = product.find("div", class_="search-result-productimage gridview")
            #image_url = image_container.find("img", src=True)['src']
            store_icon = "images/target-icon.png"

            if title != None and price != None and url != None:

                print("%s - %s" % (title.text, price.text))

                record = {
                    'title': title.text,
                    'price': price.text,
                    'url': "http://target.com" + url.get("href"),
                    #'image_url': image_url,
                    'store_icon': store_icon
                }

                # Append each new product and attributes to the dictionary object
                extracted_records.append(record)


        return extracted_records