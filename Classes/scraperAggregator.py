from decimal import *

# Import the Deal model.
from deals.models import Deal

# Import your scraper class here.
from Classes.walmartScraper import Walmart
from Classes.staplesScraper import Staples
from manage import *



# This Class aggregates all the data from all the scrapers together and saves the data to the database.

class DataAggregator:

	def save_data(self):


		print("got to save data method")

		walmart_records = Walmart().get_deals('TV') + Walmart().get_deals('ipad') + Walmart().get_deals('phone')

		print("got the walmart deals")

		staples_records = Staples().get_deals('TV') + Staples().get_deals('ipad') + Staples().get_deals('phone')

		print("got the staples deals")

		extracted_records = walmart_records + staples_records

		print("got the combined extracted records")

		print("Begin printout of aggregated data")


		for record in extracted_records:


			obj, created = Deal.objects.update_or_create(product_id= record['product_id'])
			obj.url = record['url']
			obj.image_url = record['image_url']
			obj.title = record['title']
			obj.price = Decimal(record['price'])
			obj.featured_product = record['featured_product']
			obj.store_id = record['store_id']
			obj.store_icon = record['store_icon']
			obj.product_id = record['product_id']
			obj.save()


			print (record)

		print("End printout of aggregated data")


DataAggregator().save_data()
