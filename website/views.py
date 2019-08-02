from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404_error.html', data)


def index(request):

    return render(request, 'glowna/index.html')

@login_required
def panel(request):
    return render(request, '404_error.html')
