from django.urls import path, include
from django.conf.urls import url
from . import views

# app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]