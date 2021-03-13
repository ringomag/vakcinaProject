
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index ,name='index'),
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('lista/', views.lista, name='lista'),
    path('novi_pacijent/', views.novi, name='novi'),
]
