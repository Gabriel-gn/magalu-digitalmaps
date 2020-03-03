from django.urls import path
from . import views

"""
Urls para acessar e fazer requerimentos às views do django.
Serão utlizadas pelo front end para receber e cadastrar novas localizações.
"""

app_name = 'locais'

urlpatterns = [
    path('', views.LocaisRoot.as_view(), name='locais_root'),
    path('user', views.LocaisUser.as_view(), name='locais_root'),
]
