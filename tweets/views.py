from django.shortcuts import render


# Create your views here.

def tweets(request):
    return render(request, 'index.html', {'tweets': 'tweets'})
