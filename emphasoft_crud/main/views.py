from django.shortcuts import render


#Стартовая страница с описанием api

def start_view(request):
    return render(request, 'main/start_page.html', {})