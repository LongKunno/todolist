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
    path('', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('test/',views.test.as_view(),name='test'),
    # path('chat/<int:receiver_id>/', views.ChatView.as_view(), name='chat_view'),

    path('chat/<int:receiver_id>/', views.IndexView.as_view(), name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<int:receiver_id>/', views.GetMessagesView.as_view(), name='get_messages'),
    path('statistics/', views.StatisticsView.as_view(), name='statistics'), 
    path('get_table/', views.GetTable.as_view(), name='get_table'), 
    path('get_todolist/', views.GetTodolist.as_view(), name='get_todolist'), 


    
    
]
