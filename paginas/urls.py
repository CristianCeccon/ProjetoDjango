from unicodedata import name
from django.urls import path
from .views import IndexView, SobreView, RoboView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('robos/', RoboView.as_view(), name="robos"),
]


