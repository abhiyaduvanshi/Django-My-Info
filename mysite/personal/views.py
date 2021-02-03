from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content' :['if you will like to contact me','abhishekabhis0004@gmail.com']})
