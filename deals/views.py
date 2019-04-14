from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Deal
from django.db.models import Q
from decimal import *

from Classes.walmartScraper import Walmart

# Create your views here.
def index(request):

	#deals = my_test
	return render(request, 'index.html', {})

def terms(request):
	return render(request, 'terms.html', {})

def help_page(request):
	return render(request, 'help_page.html', {})

def privacy_policy(request):
	return render(request, 'privacy_policy.html', {})

def about_us(request):
	return render(request, 'about_us.html', {})

def contact_us(request):
	return render(request, 'contact_us.html', {})

def deal(request):
	return HttpResponse("I am a single deal page...")

def search(requests):
	if requests.method == 'GET':
		search_id = requests.GET.get('Search')

		try:

			print("Search function occurred with " + search_id + " as an input.");

			# Base Query
			resultsBase = Deal.objects.filter(Q(title__icontains=search_id)).order_by('price')

			# Empty Query
			results = Deal.objects.none()

			price_filter_list = requests.GET.getlist('PriceFilter')

			if price_filter_list is not None:
				for price_filter in price_filter_list:

					# Filter by price range.

					if price_filter is not None:

						# If there is a range (i.e. in the format of [lowerBound-upperBound])
						if '-' in price_filter:
							results = results | resultsBase.filter(Q(price__gte=price_filter.split('-')[0]) & Q(price__lte=price_filter.split('-')[1]))

						# If it is just one value (i.e. 400+)
						else:
							results = results | resultsBase.filter(Q(price__gte=price_filter))

			if results.exists():
				return render(requests, 'search.html', {'deals': results})

			elif resultsBase.exists():
				return render(requests, 'search.html', {'deals': resultsBase})

			else:
				print('No results matched your criteria.')

				return custom_error(requests, 'No results matched the search criteria...')
		except Deal.DoesNotExist:

			return render(requests, 'error.html', 'Opps...Something went wrong with your search.')

	else:

		return render(requests, 'search.html')


def custom_error(requests, the_errors):
	return render(requests, 'error.html', {'error': the_errors})
