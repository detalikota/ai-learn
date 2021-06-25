from django.shortcuts import render
from . import learn

def home(request):
    
    return render(request,'home.html')
def about(request):
    user_input = request.GET['user_input'] 
    learn.y(user_input)
    return render(request,'about.html', {'home_input':user_input})
 