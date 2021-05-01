from django.http import HttpResponse
from django.template.loader import get_template

from fbdemo.fb_data_helper import scrape_page_list
import os.path

FILE_NAME = "pages.txt"

def index(request):
    template = get_template('fbdemo/index.html')
    context = {
        'items': [],
    }

    if request.method == "POST":
        items = []
        search_token = request.POST.get('keyword')

        pages = []
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME) as f:
                contents = f.readlines()
            pages = [x.strip() for x in contents]

        pages.append(search_token)

        items = scrape_page_list(pages)

        context = {
            'items': items,
        }

    return HttpResponse(template.render(context, request))