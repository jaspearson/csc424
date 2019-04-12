from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Deal
from django.db.models import Q

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

def deal(request):
	return HttpResponse("I am a single deal page...")

def search(requests):
	if requests.method == 'GET':
		search_id = requests.GET.get('Search')
		try:

			print("Search function occurred with " + search_id + " as an input.");

			results = Deal.objects.filter(Q(title__icontains=search_id)).order_by('price')

			if results.exists():
				return render(requests, 'search.html', {'deals': results})
			else:
				print('No results matched your criteria.')

				return custom_error(requests, 'No results matched the search criteria...')
		except Deal.DoesNotExist:

			return render(requests, 'error.html', 'Opps...Something went wrong with your search.')

	else:

		return render(requests, 'search.html')


def custom_error(requests, the_errors):
	return render(requests, 'error.html', {'error': the_errors})
