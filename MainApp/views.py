from django.shortcuts import render, HttpResponse

author = {
    'name': 'Andrew',
    'surname': 'Linkov',
    'email': 'andrelinkov@mail.ru'
}


# Create your views here.
def home(request):
    return HttpResponse('Main page')

def about(request):
    text = f'''
    Имя: <b>{author['name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    Email: <b>{author['email']}</b><br>
    '''
    return HttpResponse(text)

