
from . import views
from django.urls import path

urlpatterns = [
    path('drugoe_govno/', views.drugoe_govno, name='drugoe_govno'),
    #path('huy/', views.huy, name="huy")
]
