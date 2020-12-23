"""urlconf for the base application"""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('data/', views.data, name='data'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('result/<int:algorithm>/<int:dataset>', views.result, name='result'),
]
