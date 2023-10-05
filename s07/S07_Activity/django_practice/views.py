from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

# Create your views here.
def index(request):
	groceryitem_list =  GroceryItem.objects.all()
	context = {'groceryitem_list':groceryitem_list }
	return render(request,"django_practice/index.html",context)

def groceryitem(request,groceryitem_id):
	response="You are viewing the details of %s"
	return HttpResponse(response % groceryitem_id)