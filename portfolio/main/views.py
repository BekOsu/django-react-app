from django.shortcuts import render


def home(request):
    # return render(request, 'index.html')
    # return render(request, 'home.html')
    return render(request, 'index2.html')
