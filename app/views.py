from django.shortcuts import render
# Create your views here.
def homess(request):
    return render(request,'home.html')