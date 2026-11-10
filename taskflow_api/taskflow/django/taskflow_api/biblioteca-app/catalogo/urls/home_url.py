from django.urls import path
from catalogo.views.home_views import home_views
urlpatterns = [
    path('', home_views, name='home')
]