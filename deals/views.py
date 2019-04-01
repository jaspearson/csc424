from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from deals.models import my_test
from Classes.walmartScraper import Walmart

# Create your views here.
def index(request):
	deals = my_test
	return render(request, 'index.html', {'deals': my_test})

def terms(request):
	return render(request, 'terms.html', {})


def deal(request):
	return HttpResponse("I am a single deal page...")

def search(requests):
	if requests.method == 'GET':
		search_id = requests.GET.get('Search')
		try:
			results = Walmart().get_deals(search_id)
			print("Search function occured with " + search_id + " as an input.");
			# display the post.
			html = ("<h1>%s</h1>", results);
			return render(requests, 'search.html', {'deals': results})
		except :
			return error(requests, ["No search results matched your criteria."])
			#return error(requests, {"error": "No search results matched your criteria."})

	else:

		return render(requests, 'search.html')


def error(requests, the_error):
	return render(requests, 'error.html', {'error': the_error})
