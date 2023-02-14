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
    text = f'''
    Имя: <b>{author['name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    Email: <b>{author['email']}</b><br>
    '''
    return HttpResponse(text)

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
    text = '<ol>'
    for item in items:
        text += f"<a href='/item/{item['id']}'><li>{item['name']}</li> </a>"
    text += '</ol>'
    return HttpResponse(text)