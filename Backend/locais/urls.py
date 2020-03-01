from django.urls import path
from . import views

app_name = 'locais'
urlpatterns = [
    path('', views.LocaisRoot.as_view(), name='locais_root'),
]
