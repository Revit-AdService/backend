from django.shortcuts import render


def index(request):
    return render(request, 'temporary/temporary.html')
