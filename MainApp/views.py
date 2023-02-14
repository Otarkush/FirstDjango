from django.shortcuts import render, HttpResponse
from django.http import Http404

author = {
    'name': 'Andrew',
    'surname': 'Linkov',
    'email': 'andrelinkov@mail.ru'
}
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]
# Create your views here.
def home(request):
    return  render(request, 'index.html')

def about(request):
    context = {
        'author': author
    }
    return render(request, 'about.html', context)

def page_item(request, id):
    for item in items:
        if item['id'] == id:
            text = f'''
            Tovar {item['name']}<br>
            Quantity {item['quantity']}<br>
            '''
            return HttpResponse(text)
    raise Http404(f"There isn't such item # {id}")

def items_list(request):
    context = {
        'items': items
    }
    return render(request, 'items_list.html', context)
    # text = '<ol>'
    # for item in items:
    #     text += f"<a href='/item/{item['id']}'><li>{item['name']}</li> </a>"
    # text += '</ol>'
    # return HttpResponse(text)