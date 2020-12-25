from django.http import HttpResponse, Http404
import django.shortcuts as sh
import datetime
from books.models import Book

def response(request, offset=2):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    name = "index.html"
    print(locals())
    print(request.META.items())
    return sh.render(request, 'index2.html', locals())

def search_form(request):
    return sh.render(request, 'searchform.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title=q)
        return sh.render(request, 'searchform.html', {'books':books, 'query':q})
    else:
        return HttpResponse('Нихуя нет')