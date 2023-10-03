from django.urls import path
from . import views
# Create your models here.


urlpatterns = [
    path('', views.home,name="home"),
    path('add/', views.add,name="add"),
    path('formEdit/<int:id>/', views.formEdit,name="formEdit"),
    path('edit/', views.edit,name="edit"),
    path('delete/<int:id>/', views.delete,name="delete"),
    path('search/', views.search,name="search"),
    # path('search/<str:str>/', views.search,name="search"),
]
