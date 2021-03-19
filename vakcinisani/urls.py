
from django.urls import path
from . import views
from .views import MethodView
from django.views.generic import TemplateView

urlpatterns = [
    #path('', views.index ,name='index'),
    path('lista/', MethodView.as_view(), name='lista'), #ovde je get metoda za stranu "lista"
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('lista/', views.lista, name='lista'),
    path('novi_pacijent/', MethodView.as_view(template_name='novi_pacijent.html'), name='novi'),
]
