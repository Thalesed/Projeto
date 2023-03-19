from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('signin/', views.signin, name='signin'),
    path('logout/', LogoutView.as_view(next_page="signin"), name='logout'),
    path('send/', views.send, name="send")
]
