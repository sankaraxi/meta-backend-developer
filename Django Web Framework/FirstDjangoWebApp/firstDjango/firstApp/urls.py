from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('parameters/<name>', views.parameters, name='parameters'),
    path('queryStrings/', views.queryStrings, name='queryStrings'),
] 