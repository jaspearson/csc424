from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from deals.models import my_test
from Demos.walmartScraper import Walmart

# Create your views here.
def index(request):
	deals = my_test
	return render(request, 'index.html', {'deals': my_test})


def deal(request):
	return HttpResponse("I am a single deal page...")

def search(requests):
	if requests.method == 'GET':
		search_id = requests.GET.get('Search')
		try:
			results = Walmart().get_deals(search_id)
			print("MJP TEST");
			# display the post.
			html = ("<h1>%s</h1>", results);
			return render(requests, 'search.html', {'deals': results})
		except results.DoesNotExist:
			return HttpResponse("No post meets your search criteria")

	else:

		return render(requests, 'search.html')
