from django.db import models

# Create your models here.
class ToDoItem(models.Model):
	#classify the fields that we are going to use
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	status=models.CharField(max_length=50, default="pending..")
	date_created = models.DateTimeField('date created')
	
