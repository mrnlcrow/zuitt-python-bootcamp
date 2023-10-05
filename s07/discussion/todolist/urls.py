from django.urls import path
# . means all
from . import views

urlpatterns=[
	# the path() fxn will receive four arguments
	# We'll focus on the two arguments that are required, "route"&"view",and the third, "name" which allows us to make global changes
	# to the URL patters of your project while only touching a single file
	# Syntax: path(route,view,name)
	path('', views.index, name='index'), # we have defined this in views.py, views.index means index fxn inside views.py
	path('<int:todoitem_id>/',views.todoitem, name='viewtodoitem'),
	path('register',views.register, name="register"),
	path('change_password',views.change_password,name="change_password"),
	path('login',views.login_view, name="login"),
	path('logout',views.logout_view,name="logout")
]
 
