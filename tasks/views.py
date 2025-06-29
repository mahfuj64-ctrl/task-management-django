from django.shortcuts import render
from django.http import HttpResponse

# Create your views he

def manager_dashboard(request):
    return render(request, 'dashboard/manager_dashboard.html')

def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')
def test(request):
    context = {
        'names': ['Mahfuj','Karim','Habib','John'],
        'age': 27
    }
    return render(request, 'test.html',context)