from django.urls import path
from . import views
urlpatterns = [
    path('List/',views.showAll,name='showAll')
]