from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# Create your models here.
# app_name = 'app'

urlpatterns = [

    path('home/', views.HomeListView.as_view(),name="home"),
    path('add/', views.AddView.as_view(),name="add"),
    path('delete/<int:pk>/', views.DeleteView.as_view(),name="delete"),
    path('formEdit/<int:pk>/', views.FormEditView.as_view(), name='formEdit'),
    path('edit/', views.EditView.as_view(),name="edit"),
    path('search/', views.SearchView.as_view(),name="search"),
    path('sort/', views.SortView.as_view(),name="sort"),
    # path('back/', views.BackView.as_view(),name="back"),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    # path('chat/<int:receiver_id>/', views.chat_view, name='chat_view'),
    path('chat/<int:receiver_id>/', views.ChatView.as_view(), name='chat_view'),
    path('test/', views.test.as_view(), name='test'),
    
]
