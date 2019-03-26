from django.db import models
from django.urls import reverse
from Classes.walmartScraper import Walmart


# Create your models here.
class Deals():
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


def get_absolute_url(self):
	return reverse('blog.views.deal', args=[])


my_test = Walmart().get_deals('TV')
