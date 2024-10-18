from django.urls import path
from .views import IndexView #tá com erro porque ainda não existe


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]