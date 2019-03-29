from django.db import models
from django.urls import reverse
#from Classes.walmartScraper import Walmart


# Create your models here.
class Deals:
	title = "title"
	price = "price"
	url = "url"

	class Meta:

		def __unicode__(self):
			return u'%s' % self.title

	def __init__(self, title, price, url):
		self.title = title
		self.price = price
		self.url = url


class Deal(models.Model):
	url = models.CharField(max_length=1000)
	image_url = models.CharField(max_length=1000)
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	featured_product = models.BooleanField(default=False)
	store_id = models.IntegerField()
	product_id = models.CharField(max_length=50, unique=True)

	def get_absolute_url(self):
		return reverse('deals.views.deal', args=[])

	class Meta:

		def __unicode__(self):
			return u'%s' % self.title

# my_test = Walmart().get_deals('TV')
