from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
	#classify the fields that we are going to use
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	status=models.CharField(max_length=50, default="pending..")
	date_created = models.DateTimeField('date created')
	user= models.ForeignKey(User,on_delete=models.CASCADE,default="") #migrate after adding in model, use both the migrate commands
	
