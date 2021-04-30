
from django.urls import path
from . import views
from .views import MethodView, ObavestiView
from .views import EditVakcinisanView

urlpatterns = [
    #path('', views.index ,name='index'),
    path('lista/', MethodView.as_view(), name='lista'), #ovde je get metoda za stranu "lista"
    path('obavesti_korisnika/', ObavestiView.as_view(), name='obavesti'),
    path('', views.home, name='home'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('lista/', views.lista, name='lista'),
    path('novi_pacijent/', MethodView.as_view(template_name='novi_pacijent.html'), name='novi'),
    # path('vakcinisan/<str:pk>', views.vakcinisan, name='vakcinisan'),
    # path('edit/<str:pk>', views.edit, name='edit'),
    path('vakcinisan/<str:pk>', EditVakcinisanView.as_view(), name='vakcinisan'),
    path('edit/<str:pk>', EditVakcinisanView.as_view(template_name='edit.html'), name='edit'),
    # path('lista/bolest/', views.bolest, name='lista_bolest'), #ovo je ajax
    path('bolest/', views.dodaj_bolest, name='bolest'),
    path('bolest/<str:pk>', views.detalji_bolest, name="detalji_bolest"),
    path('bolest_edit/<str:pk>', views.izmeni_bolest, name='izmeni_bolest'),
    # path('bolest/dodaj-novu-bolest/', views.bolest, name="dodaj-novu-bolest"), ovo je ajax isto
]
