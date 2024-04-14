
from django.shortcuts import render

def homepage(request):
    return render(request, 'myfirstapp/homepage.html', {'message': 'Welcome to my website!'})

def form_page(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    else:
        return render(request, 'myfirstapp/form_page.html')
# Create your views here.
