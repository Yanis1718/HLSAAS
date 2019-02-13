from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/base.html', {'title': 'Home'})

def myprojects(request):
    return render(request, 'home/projects.html', {'title': 'Projects'})
