from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_app,name='MainApp'),
    path('ajax/evaluate/',views.evaluate , name ='Evaluate')
]
