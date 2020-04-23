from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import RedirectView


from . import views


app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_in, name='sign_in'),
    path('register/', views.register, name='register'),
    path('logout/', include('django.contrib.auth.urls')),
    path('profile/<int:profile_id>/', views.show_profile, name='show_profile'),
    path('profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
] 