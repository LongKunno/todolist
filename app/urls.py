from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# Create your models here.
app_name = 'app'

urlpatterns = [
    #todolist
    path('home/', views.HomeListView.as_view(),name="home"),
    path('add/', views.postAdd,name="add"),
    path('delete/<int:pk>/', views.DeleteView.as_view(),name="delete"),
    path('formEdit/<int:pk>/', views.FormEditView.as_view(), name='formEdit'),
    path('edit/', views.postUpdate,name="edit"),
    path('search/', views.SearchView.as_view(),name="search"),
    path('sort/', views.SortView.as_view(),name="sort"),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('test/',views.test.as_view(),name='test'),
    # path('chat/<int:receiver_id>/', views.ChatView.as_view(), name='chat_view'),
    path('get_todolistview/', views.GetTodolistView.as_view(), name='get_todolistview'),

    #Message
    path('chat/<int:receiver_id>/', views.IndexView.as_view(), name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<int:receiver_id>/', views.GetMessagesView.as_view(), name='get_messages'),

    #Statistics
    path('statistics/', views.StatisticsView.as_view(), name='statistics'), 
    path('get_table/', views.GetTable.as_view(), name='get_table'), 
    path('get_todolist/', views.GetTodolist.as_view(), name='get_todolist'), 

    #Statistics button
    path('message_xoa2day/', views.message_xoa2day.as_view(), name='message_xoa2day'), 
    path('message_add50tin/', views.message_add50tin.as_view(), name='message_add50tin'), 
    path('todolist_xoaTaskQuaHan/', views.todolist_xoaTaskQuaHan.as_view(), name='todolist_xoaTaskQuaHan'), 
    path('todolist_xoaTaskHoanThanh/', views.todolist_xoaTaskHoanThanh.as_view(), name='todolist_xoaTaskHoanThanh'), 
    path('todolist_cong1day/', views.todolist_cong1day.as_view(), name='todolist_cong1day'), 
    path('todolist_tru1day/', views.todolist_tru1day.as_view(), name='todolist_tru1day'), 
    path('todolist_cong1dayQuaHan/', views.todolist_cong1dayQuaHan.as_view(), name='todolist_cong1dayQuaHan'), 
    path('todolist_cong50taskRandom/', views.todolist_cong50taskRandom.as_view(), name='todolist_cong50taskRandom'), 
    path('todolist_xoaTaskRandom/', views.todolist_xoaTaskRandom.as_view(), name='todolist_xoaTaskRandom'), 

]
