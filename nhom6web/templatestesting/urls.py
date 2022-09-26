import imp
from django.urls import path
from templatestesting import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.homePage, name='home'),
]
urlpatterns += staticfiles_urlpatterns()