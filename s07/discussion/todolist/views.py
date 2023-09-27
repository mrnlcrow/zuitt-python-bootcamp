from django.shortcuts import render

# Create your views here.
# The from keyword allows importing of necessary classes,methods and other items needed in out application from the "django.http"
# package while the "import" keyword defines what we are importing from the package
from django.http import HttpResponse 

def index(request):
	return HttpResponse("Hello from the views.py file");  