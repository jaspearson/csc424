from bs4 import BeautifulSoup
import requests

class Staples():

	# Does not seem to work for pages that rely on JavaScript to render some of the page elements.
	# Currently researching how to make it work for those pages as well.

	# The number for the store_id will change most likely when we
	# get the database setup.

	store_id = 10
	url = ""
	base_url = ""

	def __init__(self):
		self.store_id = 10
		self.base_url = "https://www.staples.com/"
		self.url = "https://www.staples.com/%replaceME%/directory_%replaceME%?"
		print("The Staples class was initialized.")

	def get_deals(self, search_word):

		# Replace the parts of the URL with the search_word.
		search_URL = self.url.replace('%replaceME%', search_word)
		print("Search URL: " + search_URL)

		# Make the request
		the_request = requests.get(search_URL)

		# Parse the request
		soup = BeautifulSoup(the_request.text, 'html.parser')

		# Get the table that holds the products
		products_table = soup.find("div", attrs={'class', 'productView__productTileRows'})

		#print(products_table) # Used for Debugging

		# Get all product container divs
		products = products_table.find_all("div", class_="standard-type__tile_wrapper")

		# print(products) # Used for debugging

		# Initialize a dictionary object
		extracted_records = []

		# Loop through the html products and extract key peices of information.
		# title, product, price of the product, url to the product, etc.
		for product in products:
			title = product.find("a", class_="standard-type__product_title")
			price = product.find("span", class_="standard-type__price")
			url = product.find("a", class_="standard-type__product_title")
			actual_url = self.base_url + url.get("href")
			image_url = product.find("img", class_="standard-type__product_image")['src']
			store_icon = "images/staples-icon.png"

			if title != None and price != None and url != None:

				# Get the product ID of the item from the URL.
				# The product ID is usually encoded into the URL to make it unique
				# We will use this value to keep things unique in our database.
				# In the staples' case the product ID was at the URL.
				# Other Stores might be in the middle of the URL and a different
				# method for stripping it out may be needed.

				# Use the / character as the delimiter to split the url into pieces and store it in an
				# array.
				split_url = actual_url.split('/')

				# Get the number of elements in the split_url array.
				array_size = len(split_url)

				# Get the position of the product ID.
				# In the case of Staples, it stores the item id at the end of the URL.
				# Therefore, it will be the last element in the array when the URL is split up.
				product_id_element = array_size - 1

				# Get the product_id
				product_id = split_url[product_id_element]

				# This part is specific to Staples.
				# The item ID is in the format of the string "product_<itemNumber>"
				# Example: product_653186
				# Strip the string "product_" from the product_id

				product_id = product_id.strip("product_")

				# dealio_id will be the store_id - product_id
				# Example: 10-653186
				dealio_id = str(self.store_id) + "-" + product_id

				print("%s - %s, %s" % (title.text, price.text.strip('$'), dealio_id))

				record = {
					'title': title.text,
					'price': price.text.strip('$'),
					'url': actual_url,
					'image_url': image_url,
					'store_icon': store_icon,
					'product_id': dealio_id
				}

				# Append each new product and attributes to the dictionary object.
				extracted_records.append(record)
				# print(record) # used for debugging only.

		print("The get_deals method of the Staples class has finished executing.")

		# Return the extracted records to the calling program
		return extracted_records


# This line is used for testing purposes only.
Staples().get_deals('iphone')