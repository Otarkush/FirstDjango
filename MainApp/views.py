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
    Имя: {author['name']}
    Фамилия: {author['surname']}
    Email: {author['email']}
    '''
    return HttpResponse(text)


