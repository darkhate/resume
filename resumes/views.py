from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Resume(request):
    return render(request, 'index.html')

def About(request):
	if request == "about":
		return render(request, 'index.html')
def Experience(request):
	if request == "experience":
		return render(request, 'index.html')
