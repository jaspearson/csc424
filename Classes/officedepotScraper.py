from bs4 import BeautifulSoup
import requests

class OfficeDepot():
    def __init__(self):
        print("The class is ready")

    def get_info(self, new_search):
        url = "https://www.officedepot.com/a/browse/tvs/N=5+509465/?hijack= "
        new_request = requests.get(url + new_search + "&type=Search")
        soup = BeautifulSoup(new_request.text, 'html.parser')



        results = soup.find("ol" , {"id": "b_results"})

        items_table = soup.find("div",attrs={'class': 'jqQuickView grid_view'})

        items = items_table.find_all("div", class_= "sku_item")



        list_result = []
        #print(items)

        for item in items:

            title = item.find("div", class_= "desc_text")
            price = item.find("span" , class_= "price_column")
            #price = price.text.strip('each')
            url = item.find("a", class_= "med_txt")
            image_container = item.find("div", class_="photo_no_QV flcl")
            image_url = image_container.find("img", src=True)['src']
            store_icon = ""



            if title != None and price != None and url != None:

                record = {
                    'title': title.text,
                    'price': price.text,
                    'url':"https://www.officedepot.com" + url.get("href"),
                    'image_url': image_url,
                    'store_icon': store_icon
                }
                print(record)

                print(title.text+price.text)

                list_result.append(record)


        return list_result

my_test = OfficeDepot().get_value('tv')











